var gJson;

function GotoPage(num, PageCount, type) { //��תҳ
	Page = num;
	OutputHtml(PageCount, type, gJson);
}

var PageSize = 50; //ÿҳ����
var Page = 1; //��ǰҳ��
//++++++++++++++++++++
//PageCount==����Դ����
//type==��ʾҳ������
//type=1ʱ��ʾ��Ա�б�
//++++++++++++++++++++

function OutputHtmlPerson(PageCount, type, json) {

	gJson = json;
	var Pages = Math.floor((PageCount - 1) / PageSize) + 1; //��ȡ��ҳ����
	if (Page < 1) Page = 1; //�����ǰҳ��С��1
	if (Page > Pages) Page = Pages; //�����ǰҳ���������
	var Temp = "";

	var BeginNO = (Page - 1) * PageSize + 1; //��ʼ���
	var EndNO = Page * PageSize; //�������
	if (EndNO > PageCount) EndNO = PageCount;
	if (EndNO == 0) BeginNO = 0;

	if (!(Page <= Pages)) Page = Pages;
	$("total").innerHTML = "Total:<strong class='f90'>" + json.length + "</strong>&nbsp;&nbsp;Show:<strong class='f90'>" + BeginNO + "-" + EndNO + "</strong>";

	//��ҳ
	if (Page > 1 && Page !== 1) {
		Temp = "<a href='javascript:void(0)' onclick='GotoPage(1," + PageCount + "," + type + ")'><< First</a> <a href='javascript:void(0)' onclick='GotoPage(" + (Page - 1) + "," + PageCount + "," + type + ")'>Previous</a>&nbsp;"
	} else {
		Temp = " <div class=\"pn\"><< First</div> <div class=\"pn\">Previous</div>&nbsp;"
	};

	//�����ķ�ҳ�б�
	var PageFrontSum = 3; //��ҳǰ��ʾ����
	var PageBackSum = 3; //��ҳ����ʾ����

	var PageFront = PageFrontSum - (Page - 1);
	var PageBack = PageBackSum - (Pages - Page);
	if (PageFront > 0 && PageBack < 0) PageBackSum += PageFront; //ǰ�ٺ�࣬ǰʣ���λ����
	if (PageBack > 0 && PageFront < 0) PageFrontSum += PageBack; //����ǰ�࣬��ʣ���λ��ǰ
	var PageFrontBegin = Page - PageFrontSum;
	if (PageFrontBegin < 1) PageFrontBegin = 1;
	var PageFrontEnd = Page + PageBackSum;
	if (PageFrontEnd > Pages) PageFrontEnd = Pages;

	if (PageFrontBegin != 1) Temp += '<a href="javascript:void(0)" onclick="GotoPage(' + (Page - 10) + ',' + PageCount + ',' + type + ')" title="ǰ10ҳ">..</a>';
	for (var i = PageFrontBegin; i < Page; i++) {
		Temp += " <a href='javascript:void(0)' onclick='GotoPage(" + i + "," + PageCount + "," + type + ")'>" + i + "</a>";
	}
	Temp += " <strong class='f90'>" + Page + "</strong>";
	for (var i = Page + 1; i <= PageFrontEnd; i++) {
		Temp += " <a href='javascript:void(0)' onclick='GotoPage(" + i + "," + PageCount + "," + type + ")'>" + i + "</a>";
	}
	if (PageFrontEnd != Pages) Temp += " <a href='javascript:void(0)' onclick='GotoPage(" + (Page + 10) + "," + PageCount + "," + type + ")' title='��10ҳ'>..</a>";

	if (Page != Pages) {
		Temp += "&nbsp;&nbsp;<a href='javascript:void(0)' onclick='GotoPage(" + (Page + 1) + "," + PageCount + "," + type + ");'>Next</a> <a href='javascript:void(0)' onclick='GotoPage(" + Pages + "," + PageCount + "," + type + ")'>Last>></a>"
	} else {
		Temp += "&nbsp;&nbsp; <div class=\"pn\">Next</div> <div class=\"pn\">Last>></div>"
	}

	document.getElementById("pagelist").innerHTML = Temp;
	//�������


	if (type == 1) {

		var html = "", info = gJson.result;
		for (var i = BeginNO - 1; i < EndNO; i++) {
			html += "<tr> \
                          <td>"+  info[i].name +"</td>\
                          <td><button class=\"btn btn-primary\" data-toggle=\"modal\" data-target=\"#modal-form\" onclick = \"reSetUserPwdRender('"+  info[i].name +"')\"> 修改密码</button></td>\
                          <td><button class=\"btn btn-primary\"onclick =\"deleteUser('"+ info[i].name +"') \">删除用户</button></td> \
                          </tr>"
			  }
		document.getElementById("user-list-content").innerHTML = html;
	}
	clickShow(); //����������¼�
}

//������¼�
//
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