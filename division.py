using System;

namespace GitPractice
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Калькулятор готов к работе!");
        }

        public static int Add(int a, int b)
        {
            return a + b;
        }

        public static int Multiply(int a, int b)
        {
            return a * b;
        }

        public static object Divide(int a, int b)
        {
            if (b == 0) 
                return "Error: division by zero"; 
            
            return (double)a / b; 
        }
    }
}
