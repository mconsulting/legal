using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace CSFileManagerClient
{
    internal class Program
    {
        static void Main(string[] args)
        {

            var exec = new CSharpFileManager.Exec();
            exec.Execute(".");

        }
    }
}
