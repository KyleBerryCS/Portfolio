using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CS440DemoI.Database
{
    class CrimeType
    {
        public string CrimeName { get; set; }
        public int CrimeCount { get; set; }
        public float Percentage { get; set; }
        public int TotalCommCrimes { get; set; }
        public int TotalCrimes { get; set; }
        public float TotalCrimePercentage { get; set; }
    }
}
