var ec_center = echarts.init(document.getElementById("c2"));
var mydata = [{'name':'', 'value': 0}, {'name': '', 'value': 0}]

var ec_center_option = {
	title: {
		text:'',
		subtext:'',
		x:'left'
	},
	//工具栏
	tooltip: {
		trigger:'item'
	},
	//左侧小导航图标
	visualMap: {
		text: ["累计确诊", ""],
		show:true,
		x:'left',
		y:'bottom',
		textStyle:{
			fontSize: 8,
			color: '#ffffff',
			
		},
		showLabel:true,  
		splitList:[
			{start:0,end:0}, //'#700101'
			{start:1,end:9},
			{start:10,end:99},
			{start:100,end:999},
			{start:1000,end:9999},
			{start:10000}],
		color: ['#700101' ,'#9f3a12', '#C64918', '#E55B25', '#F2AD92', '#F9DCD1'] 
	},
	//配置属性
	series:[
		{
			// name: '累计确诊人数',
			color: '#ffffff',
			type: 'map',
			mapType: 'china',
			roam: false, //拖动和缩放
			itemStyle:{
				normal:{
					borderWidth:.5, //区域边框宽度
					borderColor:'#009fe8' ,//区域边框颜色
					areaColor:'#ffefd5',//区域颜色
				},
				emphasis:{ //鼠标滑过地图高度的相关设置
					borderWidth:.5, //区域边框宽度
					borderColor:'#4b0082' ,//区域边框颜色
					areaColor:'#fff',//区域颜色
				}
			},
			label: {
				normal: {
					show: true, //省份名称
					fontSize: 8,
				},
				emphasis:{ 
					show: true, 
					fontSize: 8,
				}
			},
			data: mydata
		}
	]
	
};

ec_center.setOption(ec_center_option)