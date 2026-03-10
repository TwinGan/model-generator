# LME Symbol Reference

> **Source**: LME Contract Specifications, FIX Specification v1.9.1 §3.1
> **Last Synced**: 2026-03-08

## LME Metals Symbol List

| Symbol | Metal Name | Contract Code | Lot Size | Tick Size | Price Unit |
|--------|------------|---------------|----------|-----------|------------|
| **AL** | Primary Aluminium | AH | 25 tonnes | $0.50/tonne | USD/tonne |
| **CU** | Copper (Copper A) | CA | 25 tonnes | $0.50/tonne | USD/tonne |
| **ZN** | Zinc (Special High Grade) | ZS | 25 tonnes | $0.50/tonne | USD/tonne |
| **PB** | Lead (Refined Pig Lead) | PB | 25 tonnes | $0.50/tonne | USD/tonne |
| **NI** | Nickel (Primary) | NI | 6 tonnes | $5.00/tonne | USD/tonne |
| **SN** | Tin (Refined) | SN | 5 tonnes | $5.00/tonne | USD/tonne |
| **AA** | Aluminium Alloy | AADF | 25 tonnes | $0.50/tonne | USD/tonne |
| **HN** | Steel HRC (Ferrous) | HN | 10 tonnes | $0.50/tonne | USD/tonne |

**Source**: LME Contract Specifications (lme.com), FIX Spec §3.1

## Symbol Field Usage

### FIX Protocol
- **Tag 55 (Symbol)**: Use contract code (e.g., `CA` for Copper)
- **Tag 48 (SecurityID)**: Use contract code
- **Tag 22 (SecurityIDSource)**: `8` = Exchange Symbol

### Binary Protocol
- **Field 4 (SecurityID)**: Use contract code
- Type: `String (20)`

## Contract Specifications

### Aluminium (AL/AH)
- **Lot Size**: 25 tonnes
- **Tick Size**: $0.50/tonne (outright), $0.01/tonne (carries)
- **Contract Months**: Daily to 3 months, weekly to 6 months, monthly to 123 months

### Copper (CU/CA)
- **Lot Size**: 25 tonnes
- **Tick Size**: $0.50/tonne (outright), $0.01/tonne (carries)
- **Contract Months**: Daily to 3 months, weekly to 6 months, monthly to 123 months

### Zinc (ZN/ZS)
- **Lot Size**: 25 tonnes
- **Tick Size**: $0.50/tonne (outright), $0.01/tonne (carries)
- **Contract Months**: Daily to 3 months, weekly to 6 months, monthly to 123 months

### Lead (PB/PB)
- **Lot Size**: 25 tonnes
- **Tick Size**: $0.50/tonne (outright), $0.01/tonne (carries)
- **Contract Months**: Daily to 3 months, weekly to 6 months, monthly to 123 months

### Nickel (NI/NI)
- **Lot Size**: 6 tonnes
- **Tick Size**: $5.00/tonne (outright), $0.01/tonne (carries)
- **Contract Months**: Daily to 3 months, weekly to 6 months, monthly to 123 months

### Tin (SN/SN)
- **Lot Size**: 5 tonnes
- **Tick Size**: $5.00/tonne (outright), $0.01/tonne (carries)
- **Contract Months**: Daily to 3 months, weekly to 6 months, monthly to 123 months

### Aluminium Alloy (AA/AADF)
- **Lot Size**: 25 tonnes
- **Tick Size**: $0.50/tonne (outright), $0.01/tonne (carries)

### Steel HRC (HN/HN)
- **Lot Size**: 10 tonnes
- **Tick Size**: $0.50/tonne (outright), $0.01/tonne (carries)

## Prompt Date Structure

| Type | Forward Range | Trading Frequency |
|------|---------------|-------------------|
| Daily | Cash to 3 months | Every business day |
| Weekly | 3 to 6 months | Every Wednesday |
| Monthly | 7 to 123 months | Third Wednesday of month |
| 2nd Business Day | 4 to 24 months | TOM prompt dates |

**Source**: LME Trading Calendar 2025-2035

## Clearable Currencies

| Currency | Code | Notes |
|----------|------|-------|
| US Dollar | USD | All contracts |
| Japanese Yen | JPY | Except Cash-Settled Futures, LMEmini, MAF, Premium |
| Sterling | GBP | Except Cash-Settled Futures, LMEmini, MAF, Premium |
| Euro | EUR | Except Cash-Settled Futures, LMEmini, MAF, Premium |

**Source**: Matching Rules §9

## Cross-References

- Trading Hours: See [trading-hours.md](./trading-hours.md)
- Validation Rules: See [validation-rules.md](./validation-rules.md)
