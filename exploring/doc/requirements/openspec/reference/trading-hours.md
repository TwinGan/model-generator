# LME Trading Hours Reference

**Source**: LME Matching Rules August 2022, FIX Specification v1.9.1
**Last Synced**: 2026-03-08

## Trading Venues

### LMEselect (Electronic)

| Parameter | Value | Source |
|-----------|-------|--------|
| Opening Time | 01:00 London time | Matching Rules §4 |
| Closing Time | 19:00 London time | Matching Rules §4 |
| Timezone | London (GMT/BST) | Matching Rules §4 |

### Ring (Open Outcry)

| Parameter | Value | Source |
|-----------|-------|--------|
| Opening Time | 11:40 London time | Matching Rules §4 |
| Closing Time | 17:00 London time | Matching Rules §4 |
| Sessions | Multiple sessions per metal | lme.com |
| Timezone | London (GMT/BST) | Matching Rules §4 |

### Inter-Office Telephone

| Parameter | Value | Source |
|-----------|-------|--------|
| Availability | 24 hours | Matching Rules §4 |
| Timezone | London (GMT/BST) | Matching Rules §4 |

## TOM (Trade Input Matching) Deadlines

| Deadline | Time | Source |
|----------|------|--------|
| TOM Trading Deadline | 12:30 London time | Matching Rules §4 |
| TOM Matching Deadline | 13:30 London time | Matching Rules §4 |
| Trade Input Deadline | 20:00 London time | Matching Rules §4 |

## Session States

### Pre-Open
- Orders can be entered but not matched until market opens
- Price discovery may occur

### Open
- Full order matching active
- All order types accepted

### Close
- Order entry may be restricted
- Existing orders remain active

### Closed
- No order entry
- Session may remain connected for next day

## Holiday Calendar

**Source**: lme.com (official LME calendar)

- New Year's Day
- Good Friday
- Easter Monday
- Early May Bank Holiday
- Late May Bank Holiday
- Summer Bank Holiday
- Christmas Day
- Boxing Day

**Note**: Exact dates vary by year. Consult lme.com for current year's calendar.

## Cross-References

- Matching Rules: See [matching-rules.md](./matching-rules.md) (when available)
- Session Management: See FIX Spec §1.4
