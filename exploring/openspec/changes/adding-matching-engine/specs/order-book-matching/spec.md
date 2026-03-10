# Order Book Matching

Implement price-time priority matching algorithm that matches buy and sell orders when prices cross, with time priority for same-price orders.

## ADDED Requirements

### Requirement: Price-Time Priority Matching

The matching engine SHALL match orders using price-time priority algorithm.

#### Scenario: Buy order crosses best ask

- **WHEN** a buy order is submitted with price >= best ask price
- **THEN** the order SHALL match against the best ask(s) in time priority order

#### Scenario: Sell order crosses best bid

- **WHEN** a sell order is submitted with price <= best bid price
- **THEN** the order SHALL match against the best bid(s) in time priority order

#### Scenario: Same price orders matched in time order

- **WHEN** multiple orders exist at the same price level
- **THEN** orders SHALL be matched in first-in-first-out (FIFO) order

### Requirement: Matching Trigger Conditions

The matching engine SHALL only match orders when valid crossing conditions exist.

#### Scenario: No match when buy price below ask

- **WHEN** a buy order is submitted with price < best ask price
- **THEN** the order SHALL NOT match and SHALL be added to the order book

#### Scenario: No match when sell price above bid

- **WHEN** a sell order is submitted with price > best bid price
- **THEN** the order SHALL NOT match and SHALL be added to the order book

#### Scenario: No match when opposite side empty

- **WHEN** an order is submitted and the opposite side of the book is empty
- **THEN** the order SHALL NOT match and SHALL be added to the order book

### Requirement: Partial Fill Handling

The matching engine SHALL support partial fills when order quantities don't align.

#### Scenario: Aggressor order larger than passive

- **WHEN** an aggressor order quantity > passive order quantity
- **THEN** the passive order SHALL be fully filled
- **AND** the aggressor order SHALL be partially filled
- **AND** the aggressor's remaining quantity SHALL continue matching against next price level

#### Scenario: Aggressor order smaller than passive

- **WHEN** an aggressor order quantity < passive order quantity
- **THEN** the aggressor order SHALL be fully filled
- **AND** the passive order SHALL be partially filled
- **AND** the passive order's remaining quantity SHALL stay on the book

#### Scenario: Aggressor order equals passive

- **WHEN** an aggressor order quantity == passive order quantity
- **THEN** both orders SHALL be fully filled

### Requirement: Fill Price Determination

The matching engine SHALL determine fill prices using passive order price.

#### Scenario: Fill at passive order price

- **WHEN** an aggressor order matches a passive order
- **THEN** the fill price SHALL be the passive order's price

#### Scenario: Buy aggressor matches at ask price

- **WHEN** a buy order with price 100 crosses an ask at price 99
- **THEN** the fill price SHALL be 99 (the passive ask price)

#### Scenario: Sell aggressor matches at bid price

- **WHEN** a sell order with price 98 crosses a bid at price 99
- **THEN** the fill price SHALL be 99 (the passive bid price)

### Requirement: Order Book State Updates

The matching engine SHALL maintain order book state after each match.

#### Scenario: Remove fully filled orders from book

- **WHEN** an order is fully filled
- **THEN** it SHALL be removed from the order book

#### Scenario: Update partially filled order quantity

- **WHEN** an order is partially filled
- **THEN** its remaining quantity SHALL be updated in the order book

#### Scenario: Maintain price level ordering

- **WHEN** orders are matched and removed
- **THEN** the order book SHALL maintain proper price-time ordering for remaining orders

### Requirement: Multi-Level Matching

The matching engine SHALL continue matching across multiple price levels when necessary.

#### Scenario: Match sweeps multiple price levels

- **WHEN** an aggressor order quantity exceeds all orders at best price level
- **THEN** matching SHALL continue to the next price level until order is filled or no more crosses

#### Scenario: Stop matching when no more crosses

- **WHEN** an aggressor order still has remaining quantity
- **AND** no more crossing orders exist on opposite side
- **THEN** remaining quantity SHALL be added to the order book
