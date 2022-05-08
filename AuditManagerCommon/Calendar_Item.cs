using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace AuditManagerCommon
{
    public class Calendar_Item
    {
        public string FileName { get; set; }

        private DateTime _starttime;
        private DateTime _endtime;

        public Calendar_Item(string filename)
        {
            this.FileName = filename;
        }

        public bool IsValid()
        {
      
            
            string pattern = @"(^\d{4}-\d{2}-\d{2}.\d{4})|(^\d{4}\d{2}\d{2}.\d{4})";
            string input = FileName;
            RegexOptions options = RegexOptions.Multiline;

            foreach (Match m in Regex.Matches(input, pattern, options))
            {
                this._starttime=DateTime.Parse(m.Value.Substring(0,10));

                Console.WriteLine("'{0}' found at index {1}.", m.Value, m.Index);
            }
            return true;
        }
        public DateTime StartTime
        {
            get { return _starttime; }
            set { _starttime = value; }
        }

        public DateTime EndTime
        {
            get { return _endtime; }
        }

        public string Description { get; set; }

        public string Category { get; set; }
    }
}
