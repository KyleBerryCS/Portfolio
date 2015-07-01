using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CS440DemoI.Database
{
    class CommunityArea
    {
        public string CommunityName { get; set; }
        public int CommunityID { get; set; }

        public override string ToString()
        {
            return CommunityName;
        }
    }
}
