#!/usr/bin/env python3
"""
LME Options Trading Capabilities Analyzer
Analyzes converted markdown files and classifies capabilities into functional modules
"""

import re
import json
from pathlib import Path
from collections import defaultdict

class CapabilityAnalyzer:
    def __init__(self, specs_dir="docs/specs"):
        self.specs_dir = Path(specs_dir)
        self.capabilities = defaultdict(list)
        self.modules = {}
        
    def analyze_file(self, filepath):
        """Analyze a single specification file"""
        print(f"Analyzing: {filepath.name}")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract capabilities based on document type
        if "Order Entry" in filepath.name:
            self._analyze_order_entry(content, filepath.name)
        elif "Risk Management" in filepath.name:
            self._analyze_risk_management(content, filepath.name)
        elif "Matching Rules" in filepath.name:
            self._analyze_matching_rules(content, filepath.name)
        elif "Binary" in filepath.name:
            self._analyze_binary_protocol(content, filepath.name)
        elif "Examples" in filepath.name:
            self._analyze_examples(content, filepath.name)
    
    def _analyze_order_entry(self, content, filename):
        """Extract order entry capabilities"""
        # Session Management
        if "Session Management" in content or "Authentication" in content:
            self.capabilities["Session Management"].append({
                "source": filename,
                "capability": "FIX Session Establishment and Authentication",
                "description": "Logon, authentication, password management, session termination"
            })
        
        # Order Types
        order_types = self._extract_section(content, "Order Types")
        if order_types:
            self.capabilities["Order Management"].append({
                "source": filename,
                "capability": "Order Type Support",
                "description": "Market, Limit, Stop, Stop-Limit, Iceberg, Fill-or-Kill, Good-for-Day, Good-Till-Cancel, Good-Till-Date"
            })
        
        # Order Submission
        if "Order Submission" in content:
            self.capabilities["Order Management"].append({
                "source": filename,
                "capability": "Order Submission",
                "description": "New order placement with validation"
            })
        
        # Order Modification
        if "Order Modification" in content or "Cancel" in content:
            self.capabilities["Order Management"].append({
                "source": filename,
                "capability": "Order Modification and Cancellation",
                "description": "Amend order parameters, cancel orders, mass cancellation"
            })
        
        # Recovery
        if "Recovery" in content or "Resend Request" in content:
            self.capabilities["Reliability"].append({
                "source": filename,
                "capability": "Message Recovery",
                "description": "Gap fill, resend requests, duplicate detection"
            })
    
    def _analyze_risk_management(self, content, filename):
        """Extract risk management capabilities"""
        # Risk Limits
        if "Risk Limit" in content:
            self.capabilities["Risk Management"].append({
                "source": filename,
                "capability": "Pre-Trade Risk Limits",
                "description": "Per order quantity, notional value, gross position limits"
            })
        
        # Risk Groups
        if "Risk Group" in content:
            self.capabilities["Risk Management"].append({
                "source": filename,
                "capability": "Risk Group Management",
                "description": "User role-based risk controls, view-only access"
            })
    
    def _analyze_matching_rules(self, content, filename):
        """Extract matching rules capabilities"""
        # Price Validation
        if "price validation" in content.lower():
            self.capabilities["Matching Engine"].append({
                "source": filename,
                "capability": "Price Validation",
                "description": "Pre-execution price checks, failed check handling"
            })
        
        # Trading Hours
        if "Trading hours" in content or "deadline" in content.lower():
            self.capabilities["Matching Engine"].append({
                "source": filename,
                "capability": "Trading Hours and Deadlines",
                "description": "Session schedules, TOM deadlines, trade input deadlines"
            })
        
        # Matching Logic
        self.capabilities["Matching Engine"].append({
            "source": filename,
            "capability": "Order Matching Logic",
            "description": "Price-time priority, trade reporting, execution rules"
        })
    
    def _analyze_binary_protocol(self, content, filename):
        """Extract binary protocol capabilities"""
        self.capabilities["Connectivity"].append({
            "source": filename,
            "capability": "Binary Order Entry Protocol",
            "description": "Proprietary high-performance binary interface for order submission"
        })
    
    def _analyze_examples(self, content, filename):
        """Extract example-based capabilities"""
        if "FIX" in content:
            self.capabilities["Examples"].append({
                "source": filename,
                "capability": "FIX Message Examples",
                "description": "Sample FIX messages for all order types and scenarios"
            })
        if "Binary" in content or "BIN" in content:
            self.capabilities["Examples"].append({
                "source": filename,
                "capability": "Binary Message Examples",
                "description": "Sample binary messages for all order types and scenarios"
            })
    
    def _extract_section(self, content, section_title):
        """Extract a section from the content"""
        pattern = rf"{section_title}.*?(?=(?:\n\n[A-Z][a-zA-Z\s]+:|$))"
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        return match.group(0) if match else None
    
    def analyze_all(self):
        """Analyze all specification files"""
        md_files = list(self.specs_dir.glob("*.md"))
        
        print(f"\nAnalyzing {len(md_files)} specification files...\n")
        
        for md_file in md_files:
            self.analyze_file(md_file)
        
        print(f"\n{'='*60}")
        print(f"Analysis complete. Found {len(self.capabilities)} capability modules:\n")
        
        for module_name in sorted(self.capabilities.keys()):
            print(f"\n{module_name}:")
            for cap in self.capabilities[module_name]:
                print(f"  - {cap['capability']}")
    
    def generate_module_structure(self):
        """Generate OpenSpec module structure"""
        modules = {
            "session-management": {
                "name": "Session Management",
                "description": "FIX session establishment, authentication, and lifecycle management",
                "capabilities": self.capabilities.get("Session Management", [])
            },
            "order-management": {
                "name": "Order Management",
                "description": "Order submission, modification, cancellation, and status tracking",
                "capabilities": self.capabilities.get("Order Management", [])
            },
            "risk-management": {
                "name": "Risk Management",
                "description": "Pre-trade risk controls, limits, and compliance checking",
                "capabilities": self.capabilities.get("Risk Management", [])
            },
            "matching-engine": {
                "name": "Matching Engine",
                "description": "Order matching, price validation, and trade execution rules",
                "capabilities": self.capabilities.get("Matching Engine", [])
            },
            "reliability": {
                "name": "Reliability & Recovery",
                "description": "Message recovery, gap fill, and fault tolerance mechanisms",
                "capabilities": self.capabilities.get("Reliability", [])
            },
            "connectivity": {
                "name": "Connectivity",
                "description": "Protocol support (FIX and Binary) and message formats",
                "capabilities": self.capabilities.get("Connectivity", [])
            },
            "examples": {
                "name": "Message Examples",
                "description": "Sample messages and usage examples for all protocols",
                "capabilities": self.capabilities.get("Examples", [])
            }
        }
        
        return modules
    
    def save_analysis(self, output_dir="docs/analysis"):
        """Save analysis results"""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Save raw capabilities
        with open(output_path / "capabilities.json", 'w') as f:
            json.dump(dict(self.capabilities), f, indent=2)
        
        # Save module structure
        modules = self.generate_module_structure()
        with open(output_path / "modules.json", 'w') as f:
            json.dump(modules, f, indent=2)
        
        # Generate markdown summary
        self._generate_summary_markdown(modules, output_path / "capabilities-summary.md")
        
        print(f"\nAnalysis saved to {output_dir}/")
    
    def _generate_summary_markdown(self, modules, output_file):
        """Generate markdown summary of capabilities"""
        with open(output_file, 'w') as f:
            f.write("# LME Options Trading - Capability Modules\n\n")
            f.write("This document summarizes the functional capabilities extracted from LME specifications.\n\n")
            f.write("## Modules Overview\n\n")
            
            for module_id, module_data in modules.items():
                f.write(f"### {module_data['name']}\n\n")
                f.write(f"{module_data['description']}\n\n")
                
                if module_data['capabilities']:
                    f.write("**Capabilities:**\n\n")
                    for cap in module_data['capabilities']:
                        f.write(f"- **{cap['capability']}**\n")
                        f.write(f"  - *Source:* {cap['source']}\n")
                        f.write(f"  - *Description:* {cap['description']}\n")
                    f.write("\n")
                else:
                    f.write("*No capabilities identified in this module*\n\n")

def main():
    """Main function"""
    analyzer = CapabilityAnalyzer()
    analyzer.analyze_all()
    analyzer.save_analysis()
    
    print(f"\n{'='*60}")
    print("Next steps:")
    print("1. Review docs/analysis/capabilities-summary.md")
    print("2. Create OpenSpec modules based on the identified capabilities")
    print("3. Enrich with testing best practices")

if __name__ == "__main__":
    main()
