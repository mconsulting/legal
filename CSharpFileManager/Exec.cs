using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharpFileManager
{
    public class Exec
    {

        public Exec()
        {

            var evt = new Event()
        };

        public int Execute()
        {
            var i=0;
            string sourceDirectory = @"C:\current";
            string archiveDirectory = @"C:\archive";

            try
            {
                var txtFiles = Directory.EnumerateFiles(sourceDirectory, "*.txt", SearchOption.AllDirectories);

                foreach (string currentFile in txtFiles)
                {
                    i++;
                    string fileName = currentFile.Substring(sourceDirectory.Length + 1);
                    Directory.Move(currentFile, Path.Combine(archiveDirectory, fileName));
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            return i;
        }
    }
}
