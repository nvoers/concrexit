from payments.models import Payment

def get_financial_account_id(api, name):
    for financial_account in api.get("financial_accounts"):
        if financial_account["identifier"] == name:
            return financial_account["id"]


def link_transaction_to_financial_account(api, instance, response, project_id):
    payment_identifiers = {
        Payment.TPAY: "ThaliaPay",
        Payment.CASH: "cashtanje",
        Payment.CARD: "pin"
    }

    if instance.payment.type != Payment.WIRE:
        account_id = get_financial_account_id(api, payment_identifiers[instance.payment.type])
        if account_id is not None:
            payment_response = api.post("external_sales_invoices/{}/payments".format(response["id"]), 
                {"payment": {
                    "payment_date": instance.payment.created_at.strftime("%Y-%m-%d"),
                    "price": str(instance.payment.amount),
                    "financial_account_id": account_id, 
                    "manual_payment_action": "payment_without_proof",
                    "invoice_id": response["id"],
                    }
                }
            )

            statement_response = api.post("financial_statements",
                {"financial_statement": {
                    "financial_account_id": account_id,
                    "reference": str(instance.payment.id),
                    "financial_mutations_attributes": [
                        {
                            "date": instance.payment.created_at.strftime("%Y-%m-%d"),
                            "amount": str(instance.payment.amount),
                            "message": instance.payment.topic,
                        }
                    ]}
                }
            )

            mutation_response = api.patch("financial_mutations/{}/link_booking".format(statement_response["financial_mutations"][0]["id"]),{
                "booking_type": "ExternalSalesInvoice",
                "booking_id": response["id"],
                "price": str(instance.payment.amount),
                "description": instance.payment.topic,
                "project_id": project_id,
            })