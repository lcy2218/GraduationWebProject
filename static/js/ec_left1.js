//<script type="text/javascript" src="dark.js"></script>
var ec_left1 = echarts.init(document.getElementById("l1"));
var ec_left1_option = {
	title: {
		text: '全国累计趋势',
		textStyle:{
			color:'white',
			fontSize: 16,
		}
	},
	tooltip: {
		trigger: 'axis',
		//指示器
		axisPointer:{
			type: 'line',
			lineStyle: {
				color: '#7171C6'
			}
		},
	},
	legend: {
		data: ['累计确诊', '现有疑似', '累计治愈', '累计死亡'],
		left: 'right',
		textStyle:{
			color:'white',
			//fontSize: 16,
		}
	},
	grid: {
		left: '4%',
		right: '6%',
		bottom: '4%',
		top: 50,
		containLabel: true
	},
	//保存为图片
	// toolbox: {
	// 	feature: {
	// 		saveAsImage: {}
	// 	}
	// },
	xAxis: {
		type: 'category',
		//boundaryGap: false,
		data: []//['01.20', '01.21', '01.22']
	},
	yAxis: [{
		type: 'value',
		//Y轴字体设置
		axisLabel: {
			show: true,
			color: 'white',
			fontSize: 12,
			formatter: function(value){
				if(value >= 1000) {
					value = value / 1000 + 'k';
				}
				return value;
			}
		},
		//y轴线设置显示
		axisLine: {
			show: true
		},
		//与x轴平行的样式
		splitLine: {
			show: true,
			lineStyle: {
				color: '#17273B',
				width: 1,
				type: 'solid',
			},
		},
		
	}],
	series: [{
			name: '累计确诊',
			type: 'line',
			smooth: 'true',
			//stack: '总量',
			data: []//[260, 406, 529]
		},
		{
			name: '现有疑似',
			type: 'line',
			smooth: 'true',
			data: []//[54, 37, 3935]
		},
		{
			name: '累计治愈',
			type: 'line',
			smooth: 'true',
			data: []//[25,25,25]
		},
		{
			name: '累计死亡',
			type: 'line',
			smooth: 'true',
			data: []//[6,9,17]
		},
	]
};

ec_left1.setOption(ec_left1_option);
