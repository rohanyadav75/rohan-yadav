class Circle:
    def CalculateArea(self):
        print("Enter radius")
        self.s=float(input())
        area=3.14*self.s*self.s
        print("Area of square is=%f"%(area))
        return()
    def CalculatePerimeter(self):
        perimeter=2*3.14*self.s
        print("Perimeter of square is=%f"%(perimeter))
        return(perimeter)
c=Circle()
c.CalculateArea()
c.CalculatePerimeter()

