#Autogenerated by ReportLab guiedit do not edit
from reportlab.graphics.shapes import _DrawingEditorMixin, Drawing, Group, String, Line
from reportlab.lib.colors import Color, CMYKColor, PCMYKColor

class ExplodedDrawing_Drawing(_DrawingEditorMixin,Drawing):
	def __init__(self,width=200,height=100,*args,**kw):
		Drawing.__init__(self,width,height,*args,**kw)
		self.transform = (1,0,0,1,0,0)
		self.add(String(55.22,85.585,'RED',textAnchor='end',fontName='Helvetica',fontSize=12,fillColor=Color(0,0,0,1)))
		self.add(String(20,85.585,'red',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		self.add(String(55.22,65.585,'GREEN',textAnchor='end',fontName='Helvetica',fontSize=12,fillColor=Color(0,0,0,1)))
		self.add(String(20,65.585,'green',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		self.add(String(55.22,45.585,'BLUE',textAnchor='end',fontName='Helvetica',fontSize=12,fillColor=Color(0,0,0,1)))
		self.add(String(20,45.585,'blue',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		self.add(String(130.22,85.585,'YELLOW',textAnchor='end',fontName='Helvetica',fontSize=12,fillColor=Color(0,0,0,1)))
		self.add(String(95,85.585,'yellow',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		self.add(String(130.22,65.585,'PINK',textAnchor='end',fontName='Helvetica',fontSize=12,fillColor=Color(0,0,0,1)))
		self.add(String(95,65.585,'pink',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		self.add(String(130.22,45.585,'BLACK',textAnchor='end',fontName='Helvetica',fontSize=12,fillColor=Color(0,0,0,1)))
		self.add(String(95,45.585,'black',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		self.add(String(205.22,85.585,'WHITE',textAnchor='end',fontName='Helvetica',fontSize=12,fillColor=Color(0,0,0,1)))
		self.add(String(170,85.585,'white',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		self.add(Line(57.22,88,67.22,88,strokeColor=Color(1,0,0,1),strokeWidth=2,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(57.22,68,67.22,68,strokeColor=Color(0,.501961,0,1),strokeWidth=2,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(57.22,48,67.22,48,strokeColor=Color(0,0,1,1),strokeWidth=2,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(132.22,88,142.22,88,strokeColor=Color(1,1,0,1),strokeWidth=2,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(132.22,68,142.22,68,strokeColor=Color(1,.752941,.796078,1),strokeWidth=2,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(132.22,48,142.22,48,strokeColor=Color(0,0,0,1),strokeWidth=2,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(207.22,88,217.22,88,strokeColor=Color(1,1,1,1),strokeWidth=2,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))


if __name__=="__main__": #NORUNTESTS
	ExplodedDrawing_Drawing().save(formats=['pdf'],outDir='.',fnRoot=None)