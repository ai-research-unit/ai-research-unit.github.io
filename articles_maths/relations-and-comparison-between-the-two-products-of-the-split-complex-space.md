# __Relations and Comparison Between the Two Products of the Split-Complex Space__

## Introduction

This article collects the **relations** between the two products $AC$ and $A\overline{C}$ and the **comparison** of their laws: each of the two products determines the other through the conjugation, the conjugation and the exchange of the two slots act differently on the two, the sum and the difference of the two values are the two coordinates of one of the factors, and a short list of identities holds for the one product and fails for the other. The comparison closes with the property table of the two products and with the collapse of the four tables of the four general products onto the two tables of these two. It is the two-dimensional companion of the property table of *Comparison Between the Four General Products*, and it is where the operational difference of the two products is stated in full.

The two products and their structures are *The Two Products of the Split-Complex Space*, the article preceding this one; the collapse of the twelve codes and the dictionary of the four general products are *The Collapse of the Twelve Structures on the Split-Complex Numbers*; the associator, the ternary product, the left and right multiplications, the sandwich and the commutator of the sesquilinear product are *The Sesquilinear Product of the Split-Complex Space*, both below this article in this category. The degree-two reading of the two products, that is the two forms and the two algebraic norms, is *The Two Forms and the Two Algebraic Norms of the Split-Complex Space*, and the products on the distinguished subspaces are *Remarkable Subspaces and the Two Products of the Split-Complex Space*. The four tables that collapse here are those of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, and the comparison of their laws is *Comparison Between the Four General Products*, with *Relations Between the Four General Products* for the identities that link the four.

**Conventions.** The algebra is $\mathbb{D}=\mathbb{R}[x]/(x^2-1)$, basis $1,j$, $j^2=+1$; a general element is $A=a+ja'$; the conjugate is $\bar A=a-ja'$; the idempotents are $\Pi_{1,2}=\tfrac12(1\pm j)$, with $A=A_+\Pi_1+A_-\Pi_2$ and $A_\pm=a\pm a'$. The natural sign is the identity and the Hermitian conjugation coincides with the bar. In this article the ring product is written $A\cdot C$ where it must be told from the sesquilinear one.

## The Products Determine Each Other

**Proposition (the two products are related by the bar).** For all $A,C\in\mathbb{D}$,

$$
A\overline{C} = \overline{\bar A C}, \qquad AC = \overline{\bar A\,\overline{C}} .
$$

Each of the two products is recovered from the other by the conjugation, so the two products carry the same information and neither can be omitted from the description of the space.

**Proof.** $\overline{\bar A C}=\overline{\bar A}\,\overline{C}$ by multiplicativity of the bar on the ring product, and $\overline{\bar A}=A$, so $\overline{\bar A C}=A\overline{C}$. Applying the bar to both sides, $AC=\overline{A\overline{C}}=\overline{\bar A\,\overline C}$, which is the second identity.

The two identities say that the bar is an isomorphism from the sesquilinear product to the bilinear one: $A\overline{C}=\overline{\bar A C}$ reads the sesquilinear product of $A$ and $C$ as the conjugate of the ring product of $\bar A$ and $C$, and $AC=\overline{\bar A\overline C}$ reads the ring product as the conjugate of the sesquilinear product of $\bar A$ and $C$. A computation may be transferred from one product to the other by conjugating one factor and the result.

## The Conjugate of a Product

**Proposition (how the bar acts on each product).**

$$
\overline{AC}=\bar A\,\bar C, \qquad \overline{A\overline{C}}=\bar A\,C .
$$

So the bar is an automorphism of the ring product and an **antilinear** operation for the sesquilinear product: it conjugates a ring product term by term and it conjugates a sesquilinear product with the conjugation of the second slot undone.

**Proof.** The first is the multiplicativity of the bar. For the second, $\overline{A\overline{C}}=\bar A\,\overline{\overline{C}}=\bar A C$.

The two rules differ in the second slot: on the ring product both slots keep their bar, on the sesquilinear product the bar of the second slot cancels. The divergence is the reason the two products behave differently under every application of the bar, and it is visible at once in the table.

| quantity | the ring product $AC$ | the sesquilinear product $A\overline{C}$ |
|---|---|---|
| the conjugate of the product | $\overline{AC}=\bar A\bar C$ | $\overline{A\overline{C}}=\bar A C$ |
| the value on the pair $(j,j)$ | $1$ | $-1$ |
| the conjugate of that value | $1$ | $-1$ |
| is the value real, for $A=C$? | $A^2$ real iff $aa'=0$ | $N(A)=a^2-a'^2$, always real |

## The Exchange of the Two Slots

Two exchanges are read on a product $f$ of two slots: the **plain exchange**, which interchanges the two entries, and the **conjugate exchange**, which interchanges the entries after conjugating both.

**Proposition (the two exchanges).**

$$
f(C,A): \quad AC\mapsto AC, \quad A\overline{C}\mapsto \overline{A\overline{C}}; \qquad \overline{f(\bar A,\bar C)}: \quad AC\mapsto AC, \quad A\overline{C}\mapsto A\overline{C}.
$$

So the ring product is symmetric under both exchanges, and the sesquilinear product is **conjugate**-symmetric under the plain exchange and invariant under the conjugate exchange.

**Proof.** For the ring product, $f(C,A)=CA=AC$ and $\overline{f(\bar A,\bar C)}=\overline{\bar A\bar C}=\overline{\overline{AC}}=AC$. For the sesquilinear product, $f(C,A)=C\overline A=\overline{\overline{C\bar A}}=\overline{A\bar C}$, the conjugate of the value, so the plain exchange conjugates it; and $\overline{f(\bar A,\bar C)}=\overline{\bar A\,\overline{\bar C}}=\overline{\bar A C}=A\bar C$, so the conjugate exchange returns it unchanged.

The invariance of $A\bar C$ under the conjugate exchange is the **conjugate-symmetry** of the sesquilinear product, $A\bar C=\overline{C\bar A}$, and it is what the sesqualgebra has in place of the symmetry of the ring. Its failure under the plain exchange is the statement that the sesquilinear product is not commutative.

## The Sum and the Difference

The sum and the difference of the two values on the same pair separate the two coordinates of one factor.

**Proposition (the sum and the difference).** With $c=\operatorname{Re}C$ and $c'=\operatorname{Im}C$,

$$
AC + A\overline{C} = 2c\,A, \qquad AC - A\overline{C} = 2c'\,jA .
$$

**Proof.** From the coordinates, $AC+A\overline{C}=(2ac)+(2a'c)j=2c(a+ja')=2cA$ and $AC-A\overline{C}=(2a'c')+(2ac')j=2c'(a'+aj)=2c'j(a+ja')=2c'jA$.

So the two products on a fixed pair $(A,C)$ differ by the term $2c'jA$, which **vanishes exactly when $C$ is real or $A$ is zero**: the two products agree on a pair exactly when the second factor has no split imaginary part. On a pair with $C=j$ they differ by $2jA$, and on the pair $(j,j)$ they take the two opposite real values $1$ and $-1$.

**Corollary (the two products separate the coordinates of the first factor).** The sum recovers the first factor whenever the second is not purely imaginary, $A=(AC+A\bar C)/(2c)$ for $c\neq0$, and the difference recovers it whenever the second has a non-zero split imaginary part, $A=(AC-A\bar C)/(2jc')$ for $c'\neq0$.

## The Identities That Separate the Two Products

A short list of identities holds for the ring product, for the reason the ring is associative and commutative, and fails for the sesquilinear product.

**Theorem.** Each identity of the table except the multiplicativity of the matrix model holds for $AC$ for all $A,C,D$ and fails for $A\overline{C}$ for some $A,C,D$; the matrix identity holds for both.

| identity | for $AC$ | for $A\overline{C}$ | witness of the failure |
|---|---|---|---|
| the bar commutes: $\overline{f(A,C)}=\bar A\bar C$ | holds | fails, $\overline{A\bar C}=\bar AC$ | $A=1,C=j$: $\overline{A\bar C}=j$ against $\bar A\bar C=-j$ |
| symmetric: $f(A,C)=f(C,A)$ | holds | fails, the plain exchange conjugates | $A=1,C=j$: $f(A,C)=-j$ against $f(C,A)=j$ |
| carried by the matrix model: $\mathsf M_2$ turns the product into a matrix product | holds | holds | $\mathsf M_2(AC)=\mathsf M_2(A)\mathsf M_2(C)$ against $\mathsf M_2(A\bar C)=\mathsf M_2(A)\mathsf M_2(\bar C)$ |
| two-sided unit | holds, $1$ | fails, $1$ is only a right unit | $A=1,C=j$: $1\bar j=-j\neq j$ |
| associative: $f(f(A,C),D)=f(A,f(C,D))$ | holds | fails | $A=C=1,D=j$: $-j$ against $j$ |
| power-associative: $f(A,f(A,A))=f(f(A,A),A)$ | holds | fails | $A=j$: $-j$ against $j$ |
| alternative: $f(A,f(A,C))=f(f(A,A),C)$ | holds | fails | $A=C=j$: $-j$ against $j$ |
| flexible: $f(f(A,C),A)=f(A,f(C,A))$ | holds | fails | $A=j,C=1$: $-1$ against $1$ |

**Proof.** The ring column is the associativity, commutativity and unit of $\mathbb{D}$ under $AC$, together with the multiplicativity of the bar on the ring product; the two products are both $\mathbb R$-bilinear maps into $\mathbb D$, and the matrix column is the multiplicativity of $\mathsf M_2$ read on each. The sesquilinear column is the list of failures: the bar of the product is $\bar AC$ and not $\bar A\bar C$; the plain exchange conjugates the value; the element $1$ satisfies $1\overline C=\bar C$; and the associator with $A=C=1$, $D=j$ does not vanish, so the associativity, power-associativity, alternativity and flexibility all fail on the displayed witnesses.

The single row that holds for both is the matrix row, and it holds for the trivial reason that both products are built from the algebra operations and $\mathsf M_2$ is multiplicative: each product is the image of the corresponding matrix product, $\mathsf M_2(AC)=\mathsf M_2(A)\mathsf M_2(C)$ and $\mathsf M_2(A\bar C)=\mathsf M_2(A)\mathsf M_2(\bar C)$. The failures of the sesquilinear column are all confined to the sesquilinear shape and are owned by *The Sesquilinear Product of the Split-Complex Space*, below this article in this category.

## The Table of the Two Products

Collecting the sections gives the **property table** of the two products.

| property | the ring product $AC$ | the sesquilinear product $A\overline{C}$ |
|---|---|---|
| scalar rule | $\mathbb{R}$-bilinear | linear in the first slot, conjugate-linear in the second |
| symmetry | symmetric, $AC=CA$ | conjugate-symmetric, $A\bar C=\overline{C\bar A}$ |
| plain exchange $f(C,A)$ | the value itself | the conjugate of the value |
| conjugate exchange $\overline{f(\bar A,\bar C)}$ | the value itself | the value itself |
| unit | two-sided | right only |
| associativity | yes | no |
| alternative, flexible, power-associative | yes | no |
| bar of the product | $\overline{AC}=\bar A\bar C$ | $\overline{A\bar C}=\bar AC$ |
| zero divisors | yes, $\Pi_1\Pi_2=0$ | yes, $\Pi_1\overline{\Pi_1}=0$ |
| commutator $f(A,C)-f(C,A)$ | zero | $2(a'c-ac')j$, non-zero in general |
| left multiplications closed under composition | yes | no |
| form and norm it defines | $B(A,C)=AC$, $B(A)=A^2$ | $H(A,C)=A\bar C$, $H(A)=N(A)=a^2-a'^2$ |

The row of the forms is the degree-two reading of the two products: the forms and the norms are *The Two Forms and the Two Algebraic Norms of the Split-Complex Space*, and the failure of closure of the sesquilinear left multiplications under composition is owned by *The Sesquilinear Product of the Split-Complex Space*.

## The Collapse of the Four Tables

The four general products of the biquaternion space each carry a property table, and their comparison is the table of *Comparison Between the Four General Products*. On the split-complex space the same collapse happens at the level of the tables: the four general products are $\mathrm{GPA}=\mathrm{GQA}=AC$ and $\mathrm{GPS}=\mathrm{GQS}=A\overline{C}$, so the four tables become two.

| family of the four general products | the table it carries on $\mathbb{D}$ |
|---|---|
| plain algebra $\mathrm{GPA},\mathrm{SPA},\mathrm{GQA},\mathrm{SQA}$ | the table of $AC$ |
| plain sesqualgebra $\mathrm{GPS},\mathrm{SPS},\mathrm{GQS},\mathrm{SQS}$ | the table of $A\overline C$ |

The collapse of the tables is the collapse of the products themselves: the quaternionic table coincides with the plain one because the natural conjugation is the identity, and the symmetrised and antisymmetrised codes add no row because the algebra is commutative, the antisymmetrised ones vanishing and the symmetrised ones coinciding with the general. The count of the properties that hold is therefore two tables and not four, and the two that remain are the two columns of the table above. This is the two-dimensional companion of the property table of *Comparison Between the Four General Products*, and the whole of the collapse of the twelve codes is *The Collapse of the Twelve Structures on the Split-Complex Numbers*, below this article in this category.

## Summary

The two products of the split-complex space determine each other through the bar: $A\overline{C}=\overline{\bar AC}$ and $AC=\overline{\bar A\overline C}$. The bar conjugates the ring product term by term, $\overline{AC}=\bar A\bar C$, and conjugates the sesquilinear product with the second slot undone, $\overline{A\bar C}=\bar AC$. The plain exchange of the two slots leaves the ring product unchanged and conjugates the sesquilinear one; the conjugate exchange leaves both unchanged, which is the conjugate-symmetry of the sesquilinear product. The sum and the difference of the two values are $AC+A\bar C=2(\operatorname{Re}C)A$ and $AC-A\bar C=2(\operatorname{Im}C)\,jA$, so the two products agree exactly when the second factor is real or the first is zero.

The comparison table lists the two columns: the ring product is bilinear, symmetric, associative, with a two-sided unit and a definite position in the forms; the sesquilinear product is conjugate-linear in the second slot, conjugate-symmetric, non-associative, with a right unit alone, and it is the second algebraic norm $N(A)=A\bar A$. The identities that hold for the one and fail for the other are read on the witnesses $A=C=1$, $D=j$ and $A=C=j$, and the only identity common to the two is the multiplicativity of the matrix model. The four tables of the four general products collapse to the two tables of these two, the two-dimensional companion of the property table of *Comparison Between the Four General Products*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A\bar C=\overline{\bar AC}$, $AC=\overline{\bar A\bar C}$ | the two products determine each other |
| $\overline{AC}=\bar A\bar C$, $\overline{A\bar C}=\bar AC$ | the bar on each product |
| $f(C,A)$ | the plain exchange of the two slots |
| $\overline{f(\bar A,\bar C)}$ | the conjugate exchange |
| $AC+A\bar C=2cA$, $AC-A\bar C=2c'jA$ | the sum and the difference, $c=\operatorname{Re}C$, $c'=\operatorname{Im}C$ |
| $AC=A\bar C \iff C\in\mathbb{R}$ or $A=0$ | the agreement condition |
| $\mathsf M_2(AC)=\mathsf M_2(A)\mathsf M_2(C)$, $\mathsf M_2(A\bar C)=\mathsf M_2(A)\mathsf M_2(\bar C)$ | $\mathsf M_2$ carries both products |
| $\mathrm{GPA}=\mathrm{GQA}=AC$, $\mathrm{GPS}=\mathrm{GQS}=A\bar C$ | the four tables collapse to two |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for algebras with involution and the distinction between an automorphism and a conjugate-linear map.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, Graduate Texts in Mathematics 131, 2nd ed. 2001), for the laws of a commutative ring and the failure of associativity in a non-associative structure.
- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for associativity, alternativity, flexibility and the power-associativity they imply.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the two products of the split-complex plane and their conjugation.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the two products of the split-complex algebra and their laws.
