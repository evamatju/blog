var gJson;

function GotoPage(num, PageCount, type) { //跳转页
	Page = num;
	OutputHtml(PageCount, type, gJson);
}

var PageSize = 50; //每页个数
var Page = 1; //当前页码
//++++++++++++++++++++
//PageCount==数据源总数
//type==表示页面类型
//type=1时表示人员列表
//++++++++++++++++++++

function OutputHtml(PageCount, type, json) {

	gJson = json;
	var Pages = Math.floor((PageCount - 1) / PageSize) + 1; //获取分页总数
	if (Page < 1) Page = 1; //如果当前页码小于1
	if (Page > Pages) Page = Pages; //如果当前页码大于总数
	var Temp = "";

	var BeginNO = (Page - 1) * PageSize + 1; //开始编号
	var EndNO = Page * PageSize; //结束编号
	if (EndNO > PageCount) EndNO = PageCount;
	if (EndNO == 0) BeginNO = 0;

	if (!(Page <= Pages)) Page = Pages;
	$("total").innerHTML = "Total:<strong class='f90'>" + siteList.EasyDarwin.Body.SessionCount + "</strong>&nbsp;&nbsp;Show:<strong class='f90'>" + BeginNO + "-" + EndNO + "</strong>";

	//分页
	if (Page > 1 && Page !== 1) {
		Temp = "<a href='javascript:void(0)' onclick='GotoPage(1," + PageCount + "," + type + ")'><< First</a> <a href='javascript:void(0)' onclick='GotoPage(" + (Page - 1) + "," + PageCount + "," + type + ")'>Previous</a>&nbsp;"
	} else {
		Temp = " <div class=\"pn\"><< First</div> <div class=\"pn\">Previous</div>&nbsp;"
	};

	//完美的翻页列表
	var PageFrontSum = 3; //当页前显示个数
	var PageBackSum = 3; //当页后显示个数

	var PageFront = PageFrontSum - (Page - 1);
	var PageBack = PageBackSum - (Pages - Page);
	if (PageFront > 0 && PageBack < 0) PageBackSum += PageFront; //前少后多，前剩余空位给后
	if (PageBack > 0 && PageFront < 0) PageFrontSum += PageBack; //后少前多，后剩余空位给前
	var PageFrontBegin = Page - PageFrontSum;
	if (PageFrontBegin < 1) PageFrontBegin = 1;
	var PageFrontEnd = Page + PageBackSum;
	if (PageFrontEnd > Pages) PageFrontEnd = Pages;

	if (PageFrontBegin != 1) Temp += '<a href="javascript:void(0)" onclick="GotoPage(' + (Page - 10) + ',' + PageCount + ',' + type + ')" title="前10页">..</a>';
	for (var i = PageFrontBegin; i < Page; i++) {
		Temp += " <a href='javascript:void(0)' onclick='GotoPage(" + i + "," + PageCount + "," + type + ")'>" + i + "</a>";
	}
	Temp += " <strong class='f90'>" + Page + "</strong>";
	for (var i = Page + 1; i <= PageFrontEnd; i++) {
		Temp += " <a href='javascript:void(0)' onclick='GotoPage(" + i + "," + PageCount + "," + type + ")'>" + i + "</a>";
	}
	if (PageFrontEnd != Pages) Temp += " <a href='javascript:void(0)' onclick='GotoPage(" + (Page + 10) + "," + PageCount + "," + type + ")' title='后10页'>..</a>";

	if (Page != Pages) {
		Temp += "&nbsp;&nbsp;<a href='javascript:void(0)' onclick='GotoPage(" + (Page + 1) + "," + PageCount + "," + type + ");'>Next</a> <a href='javascript:void(0)' onclick='GotoPage(" + Pages + "," + PageCount + "," + type + ")'>Last>></a>"
	} else {
		Temp += "&nbsp;&nbsp; <div class=\"pn\">Next</div> <div class=\"pn\">Last>></div>"
	}

	document.getElementById("pagelist").innerHTML = Temp;
	//输出数据


	if (type == 1) {

		var html = "";
		for (var i = BeginNO - 1; i < EndNO; i++) {
			html += "<tr> \
			  <td>" + gJson.EasyDarwin.Body.Sessions[i].name +  "</td> \
			  <td>"  + "<button class=\"btn btn-primary btn-lg\" data-toggle=\"modal\" data-target=\"#modal-form\" onclick = \" reSetUserPwd("+ gJson.EasyDarwin.Body.Sessions[i].name +") " +"\"> 修改密码</button></td>" + 
			  "<td><button onclick = \"deleteUserList(" + gJson.EasyDarwin.Body.Sessions[i].name + ") \">删除用户</button></td><tr>"			
		// html += "</tr>";
		document.getElementById("divload").innerHTML = html;
	}
	clickShow(); //调用鼠标点击事件
}

//鼠标点击事件

function clickShow() {
	var links = $("content").getElementsByTagName("a");
	for (var i = 0; i < links.length; i++) {
		var url = links[i].getAttribute("href");
		var title = links[i].getAttribute("title");
		links[i].onclick = function() {
			showLink(this);
			return false;
		}
	}
}