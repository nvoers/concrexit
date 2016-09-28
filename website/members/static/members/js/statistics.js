/* Render statistics on statistics page */
var pieOptions = {
    allowPointSlect: true,
    cursor: 'pointer',
    dataLabels : {
        enabled: true,
        formatter:function() { // Omit zero values
            if(this.y != 0) {
                return this.point.name + ": " + this.y; // TODO: add newline <br /> ?
            }
        },
        distance: -50
    }
};
$(function () {
    Highcharts.theme = {
        colors: ['#AE0046', '#E62272', '#E6478A', '#CC2482', '#8E1056', '#DC3472'],
        title: {
            style: {
                color: '#000',
                font: 'bold 16px "Trebuchet MS", Verdana, sans-serif'
            }
        },
        subtitle: {
            style: {
                color: '#666666',
                font: 'bold 12px "Trebuchet MS", Verdana, sans-serif'
            }
        },
        credits: false,  // Free for non-profit
        legend: {
            itemStyle: {
                font: '9pt Trebuchet MS, Verdana, sans-serif',
                color: 'black'
            },
            itemHoverStyle: {
                color: 'gray'
            }
        }
    };

    // Apply the theme
    Highcharts.setOptions(Highcharts.theme);

    $('#membersTypeChart').highcharts({
        chart: {
            type: 'pie'
        },
        title: {
            text: gettext('Members per member type'),
        },
        plotOptions: {
            pie: pieOptions
        },
        series: [{
            name: 'Thalianen',
            colorByPoint: true,
            data : [{
                name: gettext('Members'),
                y: total_stats_member_type.member
            },{
                name: gettext('Supporters'),
                y: total_stats_member_type.supporter
            },{
                name: gettext('Honorary Members'),
                y: total_stats_member_type.honorary
            }]
        }]
    });

    $('#totalYearChart').highcharts({
        chart: {
            type: 'pie'
        },
        title: {
            text: gettext("Total members per year"),
        },
        plotOptions: {
            pie: pieOptions
        },
        series: [{
            name: 'Thalianen',
            colorByPoint: true,
            data : [{
                name: gettext("1st year"),
                y: total_stats_year[0].member + total_stats_year[0].supporter + total_stats_year[0].honorary
            },{
                name: gettext("2nd year"),
                y: total_stats_year[1].member + total_stats_year[1].supporter + total_stats_year[1].honorary
            },{
                name: gettext("3rd year"),
                y: total_stats_year[2].member + total_stats_year[2].supporter + total_stats_year[2].honorary
            },{
                name: gettext("4th year"),
                y: total_stats_year[3].member + total_stats_year[3].supporter + total_stats_year[3].honorary
            },{
                name: gettext("5th year"),
                y: total_stats_year[4].member + total_stats_year[4].supporter + total_stats_year[4].honorary
            },{
                name: gettext(">5th year"),
                y: total_stats_year[5].member + total_stats_year[5].supporter + total_stats_year[5].honorary
            }]
        }]
    });

    $('#membersYearChart').highcharts({
        chart: {
            type: 'pie'
        },
        title: {
            text: gettext("Members per year"),
        },
        plotOptions: {
            pie: pieOptions
        },
        series: [{
            name: 'Thalianen',
            colorByPoint: true,
            data : [{
                name: gettext("1st year"),
                y: total_stats_year[0].member
            },{
                name: gettext("2nd year"),
                y: total_stats_year[1].member
            },{
                name: gettext("3rd year"),
                y: total_stats_year[2].member
            },{
                name: gettext("4th year"),
                y: total_stats_year[3].member
            },{
                name: gettext("5th year"),
                y: total_stats_year[4].member
            },{
                name: gettext(">5th year"),
                y: total_stats_year[5].member
            }]
        }]
    });


    $('#supportersYearChart').highcharts({
        chart: {
            type: 'pie'
        },
        title: {
            text: gettext("Supporters per year"),
        },
        plotOptions: {
            pie: pieOptions
        },
        series: [{
            name: 'Thalianen',
            colorByPoint: true,
            data : [{
                name: gettext("1st year"),
                y: total_stats_year[0].supporter
            },{
                name: gettext("2nd year"),
                y: total_stats_year[1].supporter
            },{
                name: gettext("3rd year"),
                y: total_stats_year[2].supporter
            },{
                name: gettext("4th year"),
                y: total_stats_year[3].supporter
            },{
                name: gettext("5th year"),
                y: total_stats_year[4].supporter
            },{
                name: gettext(">5th year"),
                y: total_stats_year[5].supporter
            }]
        }]
    });
});
