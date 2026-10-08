
# __The Associator of the Quaternionic Sesquilinear Product__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ carries four products on its underlying $\mathbb{C}$-vector space (*The Four Biquaternion Complex Products*), and the fourth of them,

$$
\tilde P \star \tilde Q = \tilde P^{\natural}\tilde Q^{*} ,
$$

is the subject of this group. The rule and the scalar–vector form are *The Four Biquaternion Complex Products* §*The Complex Quaternionic Sesquilinear Product*; the sesqualgebra it defines, its multiplication table and its axioms are *Biquaternions as a General Quaternionic Sesqualgebra (GQS) over $\mathbb{C}$*. The symbols are those of the group: ${}^{\natural}$ is the natural conjugation $\tilde P^{\natural} = P_0 - \mathbf P$, ${}^{*}$ is the star conjugation $\tilde P^{*} = \overline{P_0} - \overline{\mathbf Q}$, the bar is the coefficientwise complex conjugation, and $N(\tilde P) = \tilde P\tilde P^{\natural} = \sum_\mu P_\mu^{2}$ is the norm form.

The subject of this article is the **associator** of the multiplication,

$$
[\tilde P,\tilde Q,\tilde R] = (\tilde P \star \tilde Q) \star \tilde R - \tilde P \star (\tilde Q \star \tilde R) ,
$$

the obstruction to associativity and the residue of the group's first negative statement. The associator of the fourth product is not the associator of an algebra, and it is not the associator of the derived operation either: it is the difference of two *plain* products of three factors, one for each grouping, and each grouping carries one of the conjugations in a different slot. The article establishes three things. First, the closed form

$$
[\tilde P,\tilde Q,\tilde R] = \overline{\tilde Q}\,\tilde P\,\tilde R^{*} - \tilde P^{\natural}\,\tilde R\,\overline{\tilde Q} ,
$$

the two terms being the two groupings in the notation of the plain product. Second, the **parities**: the associator is $\mathbb{C}$-linear in the first variable, $\varsigma$-semilinear in the second, and neither in the third, so the associator is not a trilinear form on $\mathbb{B}^{3}$ but a trilinear form on two different mixed modules, in the sense of *The Sesquilinear Associator and the Ternary Product*. Third, the failure of the product is total: it is not associative, not flexible and not power-associative, and the degree-three identity fails as well, so the product sits at the bottom of the property ladder of *Non-Associative Algebras and the Property Ladder* and not at some intermediate rung.

The article owns the associator, its parities and the failure of the weaker laws. It cites the general associator formula and the parity theorem to *The Sesquilinear Associator and the Ternary Product*; it cites the two propositions for the fourth product to *Biquaternions as a General Quaternionic Sesqualgebra (GQS) over $\mathbb{C}$* §*The Associator* and §*The Flexibility and the Degree-Three Identity*; and it does not treat the ternary product, which is *The Ternary Product and the Failure of the Jordan Triple Identity*, nor the operators, which are *The Left and Right Multiplications of the Quaternionic Sesquilinear Product*.

## The Associator

### Definition

**Definition.** The **associator** of the multiplication is the three-variable map

$$
[\tilde P,\tilde Q,\tilde R] = (\tilde P \star \tilde Q) \star \tilde R - \tilde P \star (\tilde Q \star \tilde R) .
$$

The product is **associative** when the associator vanishes identically; the multiplication of this group is not.

The defining difference is additivity in the three variables and nothing else, so the associator is additive in each variable; its parity in each variable is the subject of the section after next.

### The Formula

**Theorem (the closed form).** For all biquaternions $\tilde P, \tilde Q, \tilde R$,

$$
[\tilde P,\tilde Q,\tilde R] = \overline{\tilde Q}\,\tilde P\,\tilde R^{*} - \tilde P^{\natural}\,\tilde R\,\overline{\tilde Q} ,
$$

where the products on the right are the plain products of the algebra.

**Proof.** For the left grouping, expanding the rule twice and using the anti-multiplicativity of ${}^{\natural}$ and $*$, together with $(\tilde X^{*})^{\natural} = \overline{\tilde X}$ and $(\tilde X^{\natural})^{*} = \overline{\tilde X}$ read on the coordinates,

$$
(\tilde P \star \tilde Q) \star \tilde R = (\tilde P^{\natural}\tilde Q^{*})^{\natural}\tilde R^{*} = (\tilde Q^{*})^{\natural}(\tilde P^{\natural})^{\natural}\tilde R^{*} = \overline{\tilde Q}\,\tilde P\,\tilde R^{*} .
$$

For the right grouping, $(\tilde Q^{\natural}\tilde R^{*})^{*} = (\tilde R^{*})^{*}(\tilde Q^{\natural})^{*} = \tilde R\,\overline{\tilde Q}$, so

$$
\tilde P \star (\tilde Q \star \tilde R) = \tilde P^{\natural}(\tilde Q \star \tilde R)^{*} = \tilde P^{\natural}\tilde R\,\overline{\tilde Q} .
$$

Subtracting the second display from the first gives the formula. $\square$

**Remark.** The formula is the exact analogue of the associator of the derived operation, and it is not the same formula: the derived operation $x \star y = xy^{*}$ has associator $x((zy)^{*} - zy^{*})$, with the first factor untouched, while the formula above carries ${}^{\natural}$ on $\tilde P$ in the second term and the plain products $\tilde P\tilde R^{*}$ and $\tilde R\overline{\tilde Q}$ in the two terms. The two terms are the two groupings, and the difference of groupings is the whole content of non-associativity.

### The Two Groupings and Their Modules

Each term of the associator is a plain product of three factors, and each factor is one of the element, its two conjugations and its plain form; the two terms are the two **groupings**, and the two groupings are sesquilinear in different slots.

**Proposition (the modules).** Write $\mathbb{B}^{\varsigma}$ for the module $\mathbb{B}$ with the scalars twisted by the conjugation $\varsigma(z) = \bar z$; a map is $\mathbb{C}$-linear on $\mathbb{B}^{\varsigma}$ when it is conjugate-linear on $\mathbb{B}$.

(i) The left grouping $(\tilde P,\tilde Q,\tilde R) \mapsto (\tilde P \star \tilde Q) \star \tilde R = \overline{\tilde Q}\,\tilde P\,\tilde R^{*}$ is $\mathbb{C}$-linear on $\mathbb{B} \times \mathbb{B}^{\varsigma} \times \mathbb{B}^{\varsigma}$.

(ii) The right grouping $(\tilde P,\tilde Q,\tilde R) \mapsto \tilde P \star (\tilde Q \star \tilde R) = \tilde P^{\natural}\,\tilde R\,\overline{\tilde Q}$ is $\mathbb{C}$-linear on $\mathbb{B} \times \mathbb{B}^{\varsigma} \times \mathbb{B}$.

**Proof.** The products on the right are plain products, which are $\mathbb{C}$-bilinear; the parities come from the conjugations in the factors. In the left grouping the factor $\overline{\tilde Q}$ is conjugate-linear in $\tilde Q$ and the factor $\tilde R^{*}$ is conjugate-linear in $\tilde R$; in the right grouping the factor $\overline{\tilde Q}$ is conjugate-linear in $\tilde Q$ and the factor $\tilde R$ is linear in $\tilde R$. The first factor is $\tilde P$ in the left grouping and $\tilde P^{\natural}$ in the right, $\mathbb{C}$-linear in $\tilde P$ in both cases. $\square$

**Remark.** The two groupings are therefore sesquilinear in the second slot and differ in the third: the left grouping is conjugate-linear and the right grouping linear there. This is the reason the associator is not homogeneous in the third variable, and it is the general situation of *The Sesquilinear Associator and the Ternary Product* specialized to the fourth product.

## The Parities

### The First Variable

**Proposition.** The associator is $\mathbb{C}$-linear in the first variable,

$$
[\lambda\tilde P,\tilde Q,\tilde R] = \lambda[\tilde P,\tilde Q,\tilde R] .
$$

**Proof.** Both groupings are $\mathbb{C}$-linear in the first variable by the proposition above, and a difference of two linear maps is linear. $\square$

### The Second Variable

**Proposition.** The associator is conjugate-linear in the second variable,

$$
[\tilde P,\lambda\tilde Q,\tilde R] = \bar\lambda\,[\tilde P,\tilde Q,\tilde R] .
$$

**Proof.** The plain product is $\mathbb{C}$-bilinear and the conjugation $\overline{\cdot}$ is conjugate-linear, so $\overline{\lambda\tilde Q} = \bar\lambda\,\overline{\tilde Q}$ and both groupings are conjugate-linear in the second variable. $\square$

### The Third Variable: Neither

**Proposition.** The associator is neither $\mathbb{C}$-linear nor conjugate-linear in the third variable. For a non-real $\lambda$,

$$
[\tilde P,\tilde Q,\lambda\tilde R] \notin \lambda[\tilde P,\tilde Q,\tilde R] \cup \bar\lambda[\tilde P,\tilde Q,\tilde R]
$$

for a generic triple.

**Proof.** The two groupings have opposite parities in the third variable: the left grouping is conjugate-linear, $(\lambda\tilde R)^{*} = \bar\lambda\tilde R^{*}$, and the right grouping is linear, since its third factor is $\tilde R$ itself, $\tilde P^{\natural}(\lambda\tilde R)\overline{\tilde Q} = \lambda\,\tilde P^{\natural}\tilde R\overline{\tilde Q}$. The associator is the difference of a conjugate-linear function and a linear one, which is homothetic to neither, and the generic failure is read on a worked example. $\square$

**Example.** For $\tilde P = \tilde Q = e_0$ the associator is the difference of the two groupings $\tilde R^{*}$ and $\tilde R$, that is $[\tilde P,\tilde Q,\tilde R] = \tilde R^{*} - \tilde R$. At $\tilde R = e_1 + ie_2$, whose star is $-e_1 + ie_2$, the value is $-2e_1$. At $\tilde R$ replaced by $i\tilde R = ie_1 - e_2$, whose star is $ie_1 + e_2$, the value is $2e_2$. The number $2e_2$ is neither $i(-2e_1) = -2ie_1$ nor $-i(-2e_1) = 2ie_1$, so the associator at this triple is homothetic to the first value by neither $\lambda$ nor $\bar\lambda$ for $\lambda = i$, which is the generic inhomogeneity in the third variable.

### Additivity

**Proposition.** The associator is additive in each variable.

**Proof.** Both groupings are additive in each variable, being compositions of the additive multiplications and conjugations, and the difference of two additive maps is additive. $\square$

**Remark.** Linearity in the first variable, conjugate-linearity in the second, additivity in the third and inhomogeneity in the third: these are the four statements that locate the associator in the general theory. They are the parity theorem of *The Sesquilinear Associator and the Ternary Product*, read for the fourth product, and they are what the later article *The Ternary Product and the Failure of the Jordan Triple Identity* builds on.

## The Failure of the Weaker Laws

### The Product Is Not Associative

**Theorem.** The multiplication is not associative.

**Proof.** The associator is nonzero at some triple. At $(\tilde P,\tilde Q,\tilde R) = (e_0,e_0,e_1)$ the two groupings are

$$
(e_0 \star e_0) \star e_1 = e_0 \star e_1 = -e_1 , \qquad e_0 \star (e_0 \star e_1) = e_0 \star (-e_1) = e_1 ,
$$

so $[e_0,e_0,e_1] = -e_1 - e_1 = -2e_1 \neq 0$. $\square$

**Remark.** The witness uses only basis elements, and it is the smallest possible in the basis: the associator is nonzero as soon as the two groupings are told apart, and here the second argument is $e_0$, so that $\overline{\tilde Q} = e_0$ and the plain products are $e_1$ and $-e_1$.

### The Product Is Not Flexible

**Definition.** The product is **flexible** when $(\tilde P \star \tilde Q) \star \tilde P = \tilde P \star (\tilde Q \star \tilde P)$ for all $\tilde P, \tilde Q$. From the associator this is the identity $[\tilde P,\tilde Q,\tilde P] = 0$.

**Theorem.** The multiplication is not flexible.

**Proof.** At $\tilde P = ie_0$ and $\tilde Q = e_0$ the two sides are

$$
(ie_0 \star e_0) \star ie_0 = ie_0 \star ie_0 = (ie_0)^{\natural}(ie_0)^{*} = (ie_0)(-ie_0) = e_0 ,
$$

$$
ie_0 \star (e_0 \star ie_0) = ie_0 \star (-ie_0) = (ie_0)^{\natural}(-ie_0)^{*} = (ie_0)(ie_0)^{\natural} = (ie_0)(ie_0) = -e_0 ,
$$

so $[ie_0,e_0,ie_0] = 2e_0 \neq 0$. $\square$

**Remark.** The flexibility law is the weakest of the classical laws of a non-associative algebra and the one that would be needed to make the powers of an element well defined; it fails here, and it fails on a central element, which is the smallest possible failure. The witness is the one the group article records.

### The Product Is Not Power-Associative

**Definition.** The product is **power-associative** when every element generates an associative subalgebra, equivalently when $x^{p}x^{q} = x^{p+q}$ for all $p, q$; the weakest identity of the family is **third-power associativity**, $(\tilde P \star \tilde P) \star \tilde P = \tilde P \star (\tilde P \star \tilde P)$, which says that the third power is well defined.

**Theorem.** The multiplication is not power-associative, and the third-power identity fails.

**Proof.** At $\tilde P = ie_3$ the square is $\tilde P \star \tilde P = (ie_3)^{\natural}(ie_3)^{*} = (-ie_3)(ie_3) = -e_0$, so the two groupings of the third power are

$$
(\tilde P \star \tilde P) \star \tilde P = (-e_0) \star ie_3 = (-e_0)^{\natural}(ie_3)^{*} = (-e_0)(ie_3) = -ie_3 ,
$$

$$
\tilde P \star (\tilde P \star \tilde P) = ie_3 \star (-e_0) = (ie_3)^{\natural}(-e_0)^{*} = (-ie_3)(-e_0) = ie_3 .
$$

The two sides are $-ie_3$ and $ie_3$, so the third-power identity fails; equivalently the associator at the triple $(ie_3,ie_3,ie_3)$ is $-ie_3 - ie_3 = -2ie_3 \neq 0$. Since a power-associative algebra satisfies third-power associativity, the product is not power-associative. $\square$

**Remark.** The failure of third-power associativity is the strongest of the failures in the sense that it is the weakest law, so a failure there is not implied by the failures above it; the product fails at the bottom rung directly. The group article records the two failures as *The Flexibility and the Degree-Three Identity*.

### The Ladder

**Theorem (the rungs the product misses).** The property ladder of *Non-Associative Algebras and the Property Ladder* has the implications

$$
\text{associative} \implies \text{alternative} \implies \text{flexible} , \qquad \text{alternative} \implies \text{power-associative} ,
$$

and the complex quaternionic sesquilinear product satisfies none of the four properties.

**Proof.** The product is not flexible by the second theorem above; since alternative implies flexible, and associative implies alternative, the product is not alternative and not associative. The product fails third-power associativity by the third theorem, and since power-associative implies third-power associativity, the product is not power-associative. The four failures all follow from the failure at the last of the three computations, together with the separate witness of non-flexibility. $\square$

**Remark.** An algebra that fails flexibility can still be non-power-associative for a different reason; here the failure of the degree-three identity at a single central element settles power-associativity, and the failure of flexibility at another settles alternativity and associativity. The two witnesses are $ie_3$ and $(ie_0,e_0)$, both as small as possible, and the ladder's strictness is not used: the product lies below every rung.

## The Associator Read on the Plain Product

### The Difference of the Two Plain Products

The formula $[\tilde P,\tilde Q,\tilde R] = \overline{\tilde Q}\,\tilde P\,\tilde R^{*} - \tilde P^{\natural}\,\tilde R\,\overline{\tilde Q}$ exhibits the associator as the difference of two plain products of three factors, and it is worth reading the two terms separately.

**Definition.** The **left term** and the **right term** of the associator are

$$
L(\tilde P,\tilde Q,\tilde R) = \overline{\tilde Q}\,\tilde P\,\tilde R^{*} , \qquad R(\tilde P,\tilde Q,\tilde R) = \tilde P^{\natural}\,\tilde R\,\overline{\tilde Q} ,
$$

so that $[\tilde P,\tilde Q,\tilde R] = L - R$ by the formula.

**Proposition.** The left term is the left grouping and the right term is the right grouping; the left term carries the conjugations $\overline{\cdot}$ in the middle and ${}^{*}$ in the last factor, and the right term carries the conjugation ${}^{\natural}$ in the first factor and $\overline{\cdot}$ in the last.

**Proof.** The two groupings were computed in the theorem proving the formula. The first term is $(\tilde P \star \tilde Q) \star \tilde R$ and the second is $\tilde P \star (\tilde Q \star \tilde R)$. $\square$

### Examples and the Vanishing Set

**Examples.** The associator vanishes at some triples and not at others.

- $[e_0,e_0,e_1] = -2e_1$, nonzero: the two groupings are $(e_0 \star e_0) \star e_1 = -e_1$ and $e_0 \star (e_0 \star e_1) = e_1$.
- $[e_0,e_1,e_1] = 2e_0$, nonzero: the two groupings are $(e_0 \star e_1) \star e_1 = e_0$ and $e_0 \star (e_1 \star e_1) = -e_0$.
- $[e_1,e_1,e_1] = 0$, zero: the two groupings are $(e_1 \star e_1) \star e_1 = (-e_0) \star e_1 = e_1$ and $e_1 \star (e_1 \star e_1) = e_1 \star (-e_0) = e_1$.
- $[e_1,e_2,e_0] = 0$, zero: the two groupings are $(e_1 \star e_2) \star e_0 = e_3 \star e_0 = -e_3$ and $e_1 \star (e_2 \star e_0) = e_1 \star (-e_2) = -e_3$.

**Remark.** The vanishing set is the set of triples for which the two terms agree, $\overline{\tilde Q}\tilde P\tilde R^{*} = \tilde P^{\natural}\tilde R\overline{\tilde Q}$; it is a proper algebraic subset of $\mathbb{B}^{3}$ and it contains all triples with a vanishing factor and every triple of real scalar elements, but it is not the whole space. Of the $64$ triples of basis elements, $40$ make the associator vanish and $24$ do not, so the vanishing is the common case on the basis and the non-vanishing is the one that decides the laws. The group article states the same examples.

## The Comparison with the Sibling Associators

**Theorem (the sibling associators).** The associators of the four products have the following forms:

| product | associator |
|---|---|
| $\tilde P\tilde Q$ | $\tilde P(\tilde Q\tilde R) - (\tilde P\tilde Q)\tilde R = 0$, the product is associative |
| $\tilde P^{\natural}\tilde Q$ | $(\tilde P^{\natural}\tilde Q)^{\natural}\tilde R - \tilde P^{\natural}(\tilde Q^{\natural}\tilde R)$ |
| $\tilde P\tilde Q^{*}$ | $\tilde P\bigl((\tilde R\tilde Q)^{*} - \tilde R\tilde Q^{*}\bigr)$ |
| $\tilde P^{\natural}\tilde Q^{*}$ | $\overline{\tilde Q}\tilde P\tilde R^{*} - \tilde P^{\natural}\tilde R\overline{\tilde Q}$ |

**Proof.** The plain product is associative. The sibling bilinear product has the associator obtained by inserting ${}^{\natural}$ in each first slot; it is the same kind of difference of two groupings, with the conjugations ${}^{\natural}$ and the plain form. The sibling sesquilinear associator is the general formula of *The Sesquilinear Associator and the Ternary Product* for the derived operation, $\tilde P((\tilde R\tilde Q)^{*} - \tilde R\tilde Q^{*})$, with the first factor untouched. The fourth row is the formula of this article. $\square$

**Remark.** The three non-associative associators are all differences of two groupings with opposite third-slot parities, and the parity structure is the same for all three: $\mathbb{C}$-linear in the first variable, conjugate-linear in the second, neither in the third. What distinguishes the fourth row from the sibling sesquilinear row is the factor $\overline{\tilde Q}$ in front and the ${}^{\natural}$ on $\tilde P$ in the second term; the sibling's associator has the first factor $\tilde P$ untouched, and the fourth product's associator carries the extra $\natural$ that makes it the isotope of the derived operation. This is the associator-level form of the isotope reading of *Biquaternions as a General Quaternionic Sesqualgebra (GQS) over $\mathbb{C}$* §*The Isotope Reading*.

## Summary

The associator of the complex quaternionic sesquilinear multiplication is

$$
[\tilde P,\tilde Q,\tilde R] = \overline{\tilde Q}\,\tilde P\,\tilde R^{*} - \tilde P^{\natural}\,\tilde R\,\overline{\tilde Q} ,
$$

the difference of the two groupings of the product, each grouping being a plain product of three factors. The associator is $\mathbb{C}$-linear in the first variable, conjugate-linear in the second, and neither linear nor conjugate-linear in the third, so it is a trilinear form on two different mixed modules rather than on $\mathbb{B}^{3}$; it is additive in all three variables. The product is not associative, with witness $[e_0,e_0,e_1] = -2e_1$; it is not flexible, with witness $[ie_0,e_0,ie_0] = 2e_0$; and it is not power-associative, third-power associativity failing at $\tilde P = ie_3$ with the two sides $-ie_3$ and $ie_3$. The product therefore satisfies none of the four rungs of the property ladder, and each failure is read on a single basis element. The associator vanishes at some triples, the vanishing set being the proper algebraic subset $\overline{\tilde Q}\tilde P\tilde R^{*} = \tilde P^{\natural}\tilde R\overline{\tilde Q}$ of $\mathbb{B}^{3}$. The sibling sesquilinear associator is $\tilde P((\tilde R\tilde Q)^{*} - \tilde R\tilde Q^{*})$, and the associator of the fourth product is its isotope by ${}^{\natural}$, carrying the extra factor $\overline{\tilde Q}$ and the extra conjugation on the first factor.

## Summary of Notation

| symbol | meaning |
|---|---|
| $[\tilde P,\tilde Q,\tilde R]$ | the associator $(\tilde P\star\tilde Q)\star\tilde R - \tilde P\star(\tilde Q\star\tilde R)$ |
| $\overline{\tilde Q}\tilde P\tilde R^{*} - \tilde P^{\natural}\tilde R\overline{\tilde Q}$ | the closed form of the associator |
| $L(\tilde P,\tilde Q,\tilde R) = \overline{\tilde Q}\tilde P\tilde R^{*}$ | the left term, the left grouping |
| $R(\tilde P,\tilde Q,\tilde R) = \tilde P^{\natural}\tilde R\overline{\tilde Q}$ | the right term, the right grouping |
| $\mathbb{B} \times \mathbb{B}^{\varsigma} \times \mathbb{B}^{\varsigma}$ | the module of the left grouping |
| $\mathbb{B} \times \mathbb{B}^{\varsigma} \times \mathbb{B}$ | the module of the right grouping |
| $[e_0,e_0,e_1] = -2e_1$ | a witness of non-associativity |
| $[ie_0,e_0,ie_0] = 2e_0$ | a witness of non-flexibility |
| $[ie_3,ie_3,ie_3] = -2ie_3$ | a witness of the failure of third-power associativity |
| $\{ \overline{\tilde Q}\tilde P\tilde R^{*} = \tilde P^{\natural}\tilde R\overline{\tilde Q} \}$ | the vanishing set of the associator |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the associator, the flexible law and power-associativity.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the degree-three identity and the algebra of the associator.
- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the associator of a multiplication on a module and its linearity properties.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the associator of a product with an involution inserted in a slot.
