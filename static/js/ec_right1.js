var ec_right1 = echarts.init(document.getElementById("r1"));
var ec_right1_option = {
	title: {
		text: "城市现有确诊人数TOP5",
		textStyle: {
			color: 'white'
		},
		left: 'left'
	},
	color: ['#3398db'],
	tooltip: {
		trigger: 'axis',
		axisPointer: {
			type: 'shadow'
		}
	},
	xAxis: {
		type: 'category',
		data: []
	},
	yAxis: {
		type: 'value'
	},
	series: [{
		data: [],
		type: 'bar',
		barMaxWidth: '50%'
	}]
};

ec_right1.setOption(ec_right1_option);
