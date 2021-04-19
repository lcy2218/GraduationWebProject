function gettime() {
    $.ajax('', {
        url: "/time",
        data: {},
        /*dataType:'json',*/
        type: 'get',
        timeout: 10000,
        success: function (data) {
            $("#time").html(data)
        },
        error: function (xhr, type, errorThrown) {
        }
    });
}

function getc1(data) {
    $.ajax('', {
            url: "/c1",
            type: "get",
            success: function (data) {
                $(".num h1").eq(0).text(data.confirm);
                $(".num h1").eq(1).text(data.suspect);
                $(".num h1").eq(2).text(data.heal);
                $(".num h1").eq(3).text(data.dead)
            },
            error: function (xhr, type, errorThrown) {
            }
        }
    )
}

function getc2(data) {
    $.ajax('', {
    	url: "/c2",
		type: "post",
		data: {
			'se_value': "累计确诊"
		},
		success: function (data) {
			ec_center_option.visualMap.text[0] = data.text
			ec_center_option.series[0].data = data.data
			ec_center.setOption(ec_center_option)
		},
		error: function (xhr, type, errorThrown) {}
	})

}

function getl1(data) {
    $.ajax('', {
    	url: "/l1",
		type: "get",
		success: function (data) {
			
            ec_left1_option.xAxis.data = data.day
			ec_left1_option.series[0].data = data.confirm
			ec_left1_option.series[1].data = data.suspect
			ec_left1_option.series[2].data = data.heal
			ec_left1_option.series[3].data = data.dead
			
			ec_left1.setOption(ec_left1_option)
		},
		error: function (xhr, type, errorThrown) {}
	})

}

function getl2(data) {
    $.ajax('', {
        url: "/l2",
        type: "get",
        success: function (data) {
			
            ec_left2_option.xAxis.data = data.day
            ec_left2_option.series[0].data = data.confirm_add
            ec_left2_option.series[1].data = data.suspect_add

            ec_left2.setOption(ec_left2_option)
        },
        error: function (xhr, type, errorThrown) {}
    })

}

function getr1(data) {
    $.ajax('', {
        url: "/r1",
        type: "get",
        success: function (data) {
            //$("#r1").html(data);
            ec_right1_option.xAxis.data = data.city
            ec_right1_option.series[0].data = data.confirm

            ec_right1.setOption(ec_right1_option)
        },
        error: function (xhr, type, errorThrown) {}
    })
}

function getr2(data) {
    $.ajax('', {
        url: "/r2",
        type: "get",
        success: function (data) {
			ec_right2_option.series[0].data = data.kws
            ec_right2.setOption(ec_right2_option)
        },
        error: function (xhr, type, errorThrown) {}
    })
}

//setInterval(gettime, 1000)
// setInterval(getc1,10000)
// setInterval(getc2,10000*10)
// setInterval(getl1,10000*10)
// setInterval(getl2,10000*10)
// setInterval(getr1,10000*10)
// setInterval(getr2,10000*10)
getc1()
getc2()
getl1()
getl2()
getr1()
getr2()
