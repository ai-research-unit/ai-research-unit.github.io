# __Relations and Comparison Between the Two Products__

## Introduction

The complex space carries two products, the plain bilinear $AC$ and the plain sesquilinear $A\bar C$, defined in *The Two Products of the Complex Space*, above in this category. This article reads the two on one and the same pair and sets them against each other: the conjugate of a product, the exchange of the two slots, the identities that hold for one product and fail for the other, and the property table of the two with a witness for every failing entry.

The article is the complex reading of the relations and the table of the four general products; those have collapsed to the two products of the commutative base, and with them the relations and the table. The definitions are *The Two Products of the Complex Space* above; the forms and the two algebraic norms are *The Two Forms and the Two Algebraic Norms of the Complex Space*, below this article in this category, cited and not repeated.

The elements are $A = a + ia'$ and $C = c + ic'$; the bar is complex conjugation and the star coincides with it.

## The Two Products on One and the Same Pair

On one and the same pair the two products are

$$
AC = (ac - a'c') + i(ac' + a'c), \qquad A\bar C = (ac + a'c') + i(a'c - ac') .
$$

**Proposition.** The two coincide exactly when the second slot is real, and are opposite exactly when it is purely imaginary:

$$
A\bar C = AC \iff C \in \mathbb{R}_{\mathbb{C}}, \qquad A\bar C = -AC \iff C \in i\mathbb{R}_{\mathbb{C}} .
$$

**Proof.** $A\bar C = AC$ is $A(\bar C - C) = 0$, and $\mathbb{C}$ has no zero divisor, so it is $\bar C = C$, that is $c' = 0$. The second is $A(\bar C + C) = 0$, so $\bar C = -C$, that is $c = 0$.

The half sum of the two products splits the second factor into its real and its imaginary part, the complex shadow of the factor-splitting identities:

$$
\tfrac{1}{2}\bigl(AC + A\bar C\bigr) = A\,\operatorname{Re}(C), \qquad \tfrac{1}{2}\bigl(AC - A\bar C\bigr) = i\,A\,\operatorname{Im}(C) .
$$

**Proof.** $C + \bar C = 2\operatorname{Re}(C)$ and $C - \bar C = 2i\operatorname{Im}(C)$, and the multiplication is distributive.

## The Conjugate of a Product and the Exchange of the Slots

**Proposition.** The bar is an automorphism of the bilinear product and converts the sesquilinear product into a bilinear one:

$$
\overline{AC} = \bar A\bar C, \qquad \overline{A\bar C} = \bar A C .
$$

**Proof.** The bar is an involution of the algebra, so it is multiplicative, $\overline{AC} = \bar A\bar C$; composing with the definition gives $\overline{A\bar C} = \overline{A}\,\overline{\bar C} = \bar A C$.

The **slot maps** are the two ways of conjugating one factor: $\tau_1$ conjugates the first, $\tau_2$ the second. On the same pair,

$$
A\bar C = \tau_2(AC), \qquad \bar A C = \tau_1(AC), \qquad A\bar C = \overline{\tau_1(AC)} = \overline{\bar A C} .
$$

The four products have two slot maps acting on them and produce eight conjugate readings; here the four products have collapsed to two, and the eight readings collapse with them to the relations above. The exchange of the two slots gives

$$
AC = CA, \qquad A\bar C = \overline{C\bar A},
$$

the first because the multiplication is commutative and the second because

$$
\overline{C\bar A} = \bar C A = A\bar C .
$$

The second identity is the **conjugate-commutativity** of the sesquilinear product: the two slots may be exchanged at the price of conjugating the value. The bilinear product is not conjugate-commutative, $\overline{CA} = \bar C\bar A \neq AC$ in general, so conjugate-commutativity is the symmetry that the sesquilinear product owns and the bilinear product does not.

## The Identities That Single Out Each Product

The two products are told apart by the identities each satisfies and the other breaks.

| identity | holds for $AC$ | holds for $A\bar C$ |
|---|---|---|
| $\overline{XC} = \bar X\bar C$, the bar multiplicative in both slots | yes | no |
| $\overline{X\bar C} = \bar X C$ | no | yes |
| $XC = CX$ | yes | no |
| $X\bar C = \overline{C\bar X}$ | no | yes |
| $X\bar C = XC$ when $C$ is real | yes | yes |
| $X\bar X$ is the definite norm on the diagonal | no, the diagonal of $AC$ is $X^2$ | yes |

**Proof.** The first row is the multiplicativity of the bar; the analogue for the sesquilinear product is $\overline{X\bar C} = \bar X C$, which equals $\bar X\bar C$ only for real $C$, so the sesquilinear product fails the row and satisfies the second instead. The third row is commutativity, owned by the bilinear product; the analogue $X\bar C = C\bar X$ asks for $\bar C = C$, so only the sesquilinear product is saved, by conjugating the value, and it satisfies the fourth. The fifth row is the proposition above. The sixth is the definition of the two diagonals, the definite norm $H(X) = X\bar X$ of the sesquilinear product against the bilinear diagonal $B(X) = X^2$; the two are the two algebraic norms of *The Two Forms and the Two Algebraic Norms of the Complex Space*, below this article in this category.

The two products have the same vanishing set: $AC = 0$ or $A\bar C = 0$ exactly when $A = 0$ or $C = 0$, since $\mathbb{C}$ is a field. The two differ in which of them carries the diagonal that is positive for every nonzero element, and that is the definite norm of the sesquilinear product.

## The Comparison

The property table of the two products is the table of the four general products with its four columns collapsed to two. The rows are the properties of an operation, except the last two, which are properties of an algebra.

| property | $AC$ | $A\bar C$ |
|---|---|---|
| $\mathbb{C}$-linear in the first argument | yes | yes |
| $\mathbb{C}$-linear in the second argument | yes | no |
| associative | yes | no |
| commutative | yes | no |
| conjugate-commutative | no | yes |
| $1$ is a left identity | yes | no |
| $1$ is a right identity | yes | yes |
| alternative | yes | no |
| flexible | yes | no |
| degree-three identity | yes | no |
| left multiplications form a monoid | yes | no |
| multiplication of an algebra over $\mathbb{C}$ | yes | no |
| multiplication of a sesqualgebra over $\mathbb{C}$ | no | yes |

The entries are established one by one, with the witness for each failure.

### Linearity in the Two Slots

Both products are $\mathbb{C}$-linear in the first argument, $(\lambda A)C = \lambda(AC)$ and $(\lambda A)\bar C = \lambda(A\bar C)$; the bilinear product is also $\mathbb{C}$-linear in the second, $A(\lambda C) = \lambda(AC)$, while the sesquilinear product is conjugate-linear there, $A\overline{(\lambda C)} = \bar\lambda(A\bar C)$.

### Associativity and the Weaker Laws

The bilinear product is associative, being the multiplication of a field. The sesquilinear product is not, with the witness $A = 1$, $C = 1$, $D = i$:

$$
(A\bar C)\bar D = -i, \qquad A\overline{(C\bar D)} = i .
$$

An associative product satisfies the weaker laws of alternation, flexibility and the degree-three identity, so the first column carries them; the second fails each, with these witnesses.

| law | identity | witness for $A\bar C$ | left side | right side |
|---|---|---|---|---|
| alternative | $X(XY) = (XX)Y$ | $X = 1$, $Y = i$ | $i$ | $-i$ |
| flexible | $(XY)X = X(YX)$ | $X = i$, $Y = 1$ | $1$ | $-1$ |
| degree-three | $(XX)X = X(XX)$ | $X = i$ | $-i$ | $i$ |

The degree-three identity is the one that makes the third power well defined; the sesquilinear product breaks it, so its iterated products depend on the parenthesisation. The three failures say the same thing: this product, which conjugates one factor, is not power-associative.

### The Unit

The element $1$ is fixed by the bar, so it is a two-sided unit for the bilinear product and a right unit for the sesquilinear one: $A\bar 1 = A$. It is not a left unit for the sesquilinear product, $1\bar C = \bar C \neq C$ for the witness $C = i$. On the right the two agree; on the left they do not, and the difference is exactly the bar.

### Commutativity and Conjugate-Commutativity

The bilinear product is commutative and not conjugate-commutative; the sesquilinear product is neither commutative nor free of the symmetry, but conjugate-commutative. The witnesses are $A = 1$, $C = i$ for the failure of commutativity of the sesquilinear product, $A\bar C = -i$ against $C\bar A = i$, and the conjugate-commutativity is the identity proved above.

### The Two Algebra Rows

The last two rows ask whether the operation is the multiplication of an algebra over $\mathbb{C}$ or the derived operation of a sesqualgebra over $(\mathbb{C}, \bar\cdot)$. The bilinear product is the multiplication of a commutative associative unital $\mathbb{C}$-algebra, indeed a field, so it is the first and not the second; the sesquilinear product is the derived operation $X \star Y = X\bar Y$ of the algebra with the involution bar, so it is the second and not the first, and the two rows are the algebraic summary of the table.

## Summary

The two products of the complex space are read on one and the same pair. They coincide exactly when the second slot is real and are opposite exactly when it is purely imaginary, and their half sum and half difference split the second factor into its real and imaginary parts. The bar is an automorphism of the bilinear product and converts the sesquilinear product into a bilinear one of the conjugate pair, $\overline{A\bar C} = \bar A C$; the exchange of the two slots gives $AC = CA$ for the bilinear product and $A\bar C = \overline{C\bar A}$ for the sesquilinear one, the conjugate-commutativity that the bilinear product does not have.

The property table of the two is the table of the four general products collapsed to two columns. Both products are $\mathbb{C}$-linear in the first argument; the bilinear product is also $\mathbb{C}$-linear in the second, associative, commutative, unital on both sides, alternative, flexible and degree-three, and its left multiplications form a monoid; the sesquilinear product is conjugate-linear in the second slot, non-associative, non-commutative but conjugate-commutative, right-unital and not left-unital, and fails alternation, flexibility and the degree-three identity. The first is the multiplication of a field over $\mathbb{C}$; the second is the derived operation of a sesqualgebra over $(\mathbb{C}, \bar\cdot)$. The four columns collapse to two, and the complex space is the degenerate base of the construction.

## Summary of Notation

| symbol | meaning |
|---|---|
| $AC$, $A\bar C$ | the plain bilinear and the plain sesquilinear product |
| $A = a + ia'$, $C = c + ic'$ | the elements, with real coordinates |
| $\tau_1, \tau_2$ | the slot maps, conjugating the first and the second factor |
| $\overline{AC} = \bar A\bar C$ | the bar is multiplicative on the bilinear product |
| $\overline{A\bar C} = \bar A C$ | the bar converts the sesquilinear product into a bilinear one |
| $A\bar C = \overline{C\bar A}$ | conjugate-commutativity of the sesquilinear product |
| $A\bar C = AC$, $A\bar C = -AC$ | the coincidence on a real second slot and the opposition on a purely imaginary one |
| $B(X) = X^2$, $H(X) = X\bar X$ | the bilinear diagonal and the definite norm, the two algebraic norms |
| left multiplications form a monoid; multiplication of an algebra; multiplication of a sesqualgebra | the operation-level and algebra-level rows of the table |

## Further Reading

- Serge Lang, *Algebra*, 3rd edition (Springer, 2002), for bilinear and sesquilinear products, their conjugate-linearity and the derived operation of an algebra with an involution.
- Israel Nathan Herstein, *Topics in Algebra*, 2nd edition (Wiley, 1975), for associativity, alternation, flexibility and the weaker forms of associativity of a product.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for sesqualgebras, their hermitian products and their relation to the algebras with involution.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the alternative, flexible and power-associative laws and the degree-three identity.
