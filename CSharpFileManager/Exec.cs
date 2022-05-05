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
            
        }

        public int Execute(string source=@"C:\\Users\\mason\\Source\\Repos\\legal\\")
        {
            var i=0;
            source=@"C:\Users\mason\Source\Repos\legal\";
            string sourceDirectory = Path.Combine(source, "inbox");
            string archiveDirectory =Path.Combine(source, "files");

            try
            {
                var txtFiles = Directory.GetFiles(archiveDirectory, "*", SearchOption.AllDirectories);

                foreach (string currentFile in txtFiles)
                {
                    i++;
                    string date_string = Path.GetFileName(currentFile).Substring(0,15).Replace("_"," ").Insert(13,":");
                    DateTime dt=DateTime.Parse(date_string);
                  //  Directory.Move(currentFile, Path.Combine(archiveDirectory, fileName));
                    Console.WriteLine(dt.ToString());
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
