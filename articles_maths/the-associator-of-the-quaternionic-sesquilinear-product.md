
# __The Associator of the General Quaternionic Sesquilinear Product__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ carries four general products on its underlying $\mathbb{C}$-vector space (*The Four General Products of the Biquaternioid $\mathbb{C}$ Space*), and the fourth of them,

$$
\tilde Q_1 \star \tilde Q_2 = \tilde Q_1^{\natural}\tilde Q_2^{*} ,
$$

is the subject of this group. The rule and the scalar–vector form are *The Four General Products of the Biquaternioid $\mathbb{C}$ Space* §*The General Quaternionic Sesquilinear Product*; the sesqualgebra it defines, its multiplication table and its axioms are *Introduction to the General Quaternionic Sesqualgebra*. The symbols are those of the group: ${}^{\natural}$ is the natural conjugation $\tilde Q_1^{\natural} = Q_{1t} - \vec Q_1$, ${}^{*}$ is the star conjugation $\tilde Q_1^{*} = \overline{Q_{1t}} - \overline{\vec Q_1}$, the bar is the coefficientwise complex conjugation, and $\langle\tilde Q_1\rangle_{\natural} = \tilde Q_1\tilde Q_1^{\natural} = \sum_\mu Q_{1,\mu}^{2}$ is the norm form.

The subject of this article is the **associator** of the multiplication,

$$
[\tilde Q_1,\tilde Q_2,\tilde Q_3] = (\tilde Q_1 \star \tilde Q_2) \star \tilde Q_3 - \tilde Q_1 \star (\tilde Q_2 \star \tilde Q_3) ,
$$

the obstruction to associativity and the residue of the group's first negative statement. The associator of the fourth product is not the associator of an algebra, and it is not the associator of the derived operation either: it is the difference of two *plain* products of three factors, one for each grouping, and each grouping carries one of the conjugations in a different slot. The article establishes three things. First, the closed form

$$
[\tilde Q_1,\tilde Q_2,\tilde Q_3] = \overline{\tilde Q_2}\,\tilde Q_1\,\tilde Q_3^{*} - \tilde Q_1^{\natural}\,\tilde Q_3\,\overline{\tilde Q_2} ,
$$

the two terms being the two groupings in the notation of the plain product. Second, the **parities**: the associator is $\mathbb{C}$-linear in the first variable, $\varsigma$-semilinear in the second, and neither in the third, so the associator is not a trilinear form on $\mathbb{B}^{3}$ but a trilinear form on two different mixed modules, in the sense of *The Sesquilinear Associator and the Ternary Product*. Third, the failure of the product is total: it is not associative, not flexible and not power-associative, and the degree-three identity fails as well, so the product sits at the bottom of the property ladder of *Non-Associative Algebras and the Property Ladder* and not at some intermediate rung.

The article owns the associator, its parities and the failure of the weaker laws. It cites the general associator formula and the parity theorem to *The Sesquilinear Associator and the Ternary Product*; it cites the two propositions for the fourth product to *Introduction to the General Quaternionic Sesqualgebra* §*The Associator* and §*The Flexibility and the Degree-Three Identity*; and it does not treat the ternary product, which is *The Ternary Product and the Failure of the Jordan Triple Identity*, nor the operators, which are *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product*.

## The Associator

### Definition

**Definition.** The **associator** of the multiplication is the three-variable map

$$
[\tilde Q_1,\tilde Q_2,\tilde Q_3] = (\tilde Q_1 \star \tilde Q_2) \star \tilde Q_3 - \tilde Q_1 \star (\tilde Q_2 \star \tilde Q_3) .
$$

The product is **associative** when the associator vanishes identically; the multiplication of this group is not.

The defining difference is additivity in the three variables and nothing else, so the associator is additive in each variable; its parity in each variable is the subject of the section after next.

### The Formula

**Theorem (the closed form).** For all biquaternions $\tilde Q_1, \tilde Q_2, \tilde Q_3$,

$$
[\tilde Q_1,\tilde Q_2,\tilde Q_3] = \overline{\tilde Q_2}\,\tilde Q_1\,\tilde Q_3^{*} - \tilde Q_1^{\natural}\,\tilde Q_3\,\overline{\tilde Q_2} ,
$$

where the products on the right are the plain products of the algebra.

**Proof.** For the left grouping, expanding the rule twice and using the anti-multiplicativity of ${}^{\natural}$ and $*$, together with $(\tilde Q_4^{*})^{\natural} = \overline{\tilde Q_4}$ and $(\tilde Q_4^{\natural})^{*} = \overline{\tilde Q_4}$ read on the coordinates,

$$
(\tilde Q_1 \star \tilde Q_2) \star \tilde Q_3 = (\tilde Q_1^{\natural}\tilde Q_2^{*})^{\natural}\tilde Q_3^{*} = (\tilde Q_2^{*})^{\natural}(\tilde Q_1^{\natural})^{\natural}\tilde Q_3^{*} = \overline{\tilde Q_2}\,\tilde Q_1\,\tilde Q_3^{*} .
$$

For the right grouping, $(\tilde Q_2^{\natural}\tilde Q_3^{*})^{*} = (\tilde Q_3^{*})^{*}(\tilde Q_2^{\natural})^{*} = \tilde Q_3\,\overline{\tilde Q_2}$, so

$$
\tilde Q_1 \star (\tilde Q_2 \star \tilde Q_3) = \tilde Q_1^{\natural}(\tilde Q_2 \star \tilde Q_3)^{*} = \tilde Q_1^{\natural}\tilde Q_3\,\overline{\tilde Q_2} .
$$

Subtracting the second display from the first gives the formula.

**Remark.** The formula is the exact analogue of the associator of the derived operation, and it is not the same formula: the derived operation $x \star y = xy^{*}$ has associator $x((zy)^{*} - zy^{*})$, with the first factor untouched, while the formula above carries ${}^{\natural}$ on $\tilde Q_1$ in the second term and the plain products $\tilde Q_1\tilde Q_3^{*}$ and $\tilde Q_3\overline{\tilde Q_2}$ in the two terms. The two terms are the two groupings, and the difference of groupings is the whole content of non-associativity.

### The Two Groupings and Their Modules

Each term of the associator is a plain product of three factors, and each factor is one of the element, its two conjugations and its plain form; the two terms are the two **groupings**, and the two groupings are sesquilinear in different slots.

**Proposition (the modules).** Write $\mathbb{B}^{\varsigma}$ for the module $\mathbb{B}$ with the scalars twisted by the conjugation $\varsigma(z) = \bar z$; a map is $\mathbb{C}$-linear on $\mathbb{B}^{\varsigma}$ when it is conjugate-linear on $\mathbb{B}$.

(i) The left grouping $(\tilde Q_1,\tilde Q_2,\tilde Q_3) \mapsto (\tilde Q_1 \star \tilde Q_2) \star \tilde Q_3 = \overline{\tilde Q_2}\,\tilde Q_1\,\tilde Q_3^{*}$ is $\mathbb{C}$-linear on $\mathbb{B} \times \mathbb{B}^{\varsigma} \times \mathbb{B}^{\varsigma}$.

(ii) The right grouping $(\tilde Q_1,\tilde Q_2,\tilde Q_3) \mapsto \tilde Q_1 \star (\tilde Q_2 \star \tilde Q_3) = \tilde Q_1^{\natural}\,\tilde Q_3\,\overline{\tilde Q_2}$ is $\mathbb{C}$-linear on $\mathbb{B} \times \mathbb{B}^{\varsigma} \times \mathbb{B}$.

**Proof.** The products on the right are plain products, which are $\mathbb{C}$-bilinear; the parities come from the conjugations in the factors. In the left grouping the factor $\overline{\tilde Q_2}$ is conjugate-linear in $\tilde Q_2$ and the factor $\tilde Q_3^{*}$ is conjugate-linear in $\tilde Q_3$; in the right grouping the factor $\overline{\tilde Q_2}$ is conjugate-linear in $\tilde Q_2$ and the factor $\tilde Q_3$ is linear in $\tilde Q_3$. The first factor is $\tilde Q_1$ in the left grouping and $\tilde Q_1^{\natural}$ in the right, $\mathbb{C}$-linear in $\tilde Q_1$ in both cases.

**Remark.** The two groupings are therefore sesquilinear in the second slot and differ in the third: the left grouping is conjugate-linear and the right grouping linear there. This is the reason the associator is not homogeneous in the third variable, and it is the general situation of *The Sesquilinear Associator and the Ternary Product* specialized to the fourth product.

## The Parities

### The First Variable

**Proposition.** The associator is $\mathbb{C}$-linear in the first variable,

$$
[\lambda\tilde Q_1,\tilde Q_2,\tilde Q_3] = \lambda[\tilde Q_1,\tilde Q_2,\tilde Q_3] .
$$

**Proof.** Both groupings are $\mathbb{C}$-linear in the first variable by the proposition above, and a difference of two linear maps is linear.

### The Second Variable

**Proposition.** The associator is conjugate-linear in the second variable,

$$
[\tilde Q_1,\lambda\tilde Q_2,\tilde Q_3] = \bar\lambda\,[\tilde Q_1,\tilde Q_2,\tilde Q_3] .
$$

**Proof.** The plain product is $\mathbb{C}$-bilinear and the conjugation $\overline{\cdot}$ is conjugate-linear, so $\overline{\lambda\tilde Q} = \bar\lambda\,\overline{\tilde Q}$ and both groupings are conjugate-linear in the second variable.

### The Third Variable: Neither

**Proposition.** The associator is neither $\mathbb{C}$-linear nor conjugate-linear in the third variable. For a non-real $\lambda$,

$$
[\tilde Q_1,\tilde Q_2,\lambda\tilde Q_3] \notin \lambda[\tilde Q_1,\tilde Q_2,\tilde Q_3] \cup \bar\lambda[\tilde Q_1,\tilde Q_2,\tilde Q_3]
$$

for a generic triple.

**Proof.** The two groupings have opposite parities in the third variable: the left grouping is conjugate-linear, $(\lambda\tilde Q_3)^{*} = \bar\lambda\tilde Q_3^{*}$, and the right grouping is linear, since its third factor is $\tilde Q_3$ itself, $\tilde Q_1^{\natural}(\lambda\tilde Q_3)\overline{\tilde Q_2} = \lambda\,\tilde Q_1^{\natural}\tilde Q_3\overline{\tilde Q_2}$. The associator is the difference of a conjugate-linear function and a linear one, which is homothetic to neither, and the generic failure is read on a worked example.

**Example.** For $\tilde Q_1 = \tilde Q_2 = e_t$ the associator is the difference of the two groupings $\tilde Q_3^{*}$ and $\tilde Q_3$, that is $[\tilde Q_1,\tilde Q_2,\tilde Q_3] = \tilde Q_3^{*} - \tilde Q_3$. At $\tilde Q_3 = \vec e_x + i\vec e_y$, whose star is $-\vec e_x + i\vec e_y$, the value is $-2\vec e_x$. At $\tilde Q_3$ replaced by $i\tilde Q_3 = i\vec e_x - \vec e_y$, whose star is $i\vec e_x + \vec e_y$, the value is $2\vec e_y$. The number $2\vec e_y$ is neither $i(-2\vec e_x) = -2i\vec e_x$ nor $-i(-2\vec e_x) = 2i\vec e_x$, so the associator at this triple is homothetic to the first value by neither $\lambda$ nor $\bar\lambda$ for $\lambda = i$, which is the generic inhomogeneity in the third variable.

### Additivity

**Proposition.** The associator is additive in each variable.

**Proof.** Both groupings are additive in each variable, being compositions of the additive multiplications and conjugations, and the difference of two additive maps is additive.

**Remark.** Linearity in the first variable, conjugate-linearity in the second, additivity in the third and inhomogeneity in the third: these are the four statements that locate the associator in the general theory. They are the parity theorem of *The Sesquilinear Associator and the Ternary Product*, read for the fourth product, and they are what the later article *The Ternary Product and the Failure of the Jordan Triple Identity* builds on.

## The Failure of the Weaker Laws

### The Product Is Not Associative

**Theorem.** The multiplication is not associative.

**Proof.** The associator is nonzero at some triple. At $(\tilde Q_1,\tilde Q_2,\tilde Q_3) = (e_t,e_t,\vec e_x)$ the two groupings are

$$
(e_t \star e_t) \star \vec e_x = e_t \star \vec e_x = -\vec e_x , \qquad e_t \star (e_t \star \vec e_x) = e_t \star (-\vec e_x) = \vec e_x ,
$$

so $[e_t,e_t,\vec e_x] = -\vec e_x - \vec e_x = -2\vec e_x \neq 0$.

**Remark.** The witness uses only basis elements, and it is the smallest possible in the basis: the associator is nonzero as soon as the two groupings are told apart, and here the second argument is $e_t$, so that $\overline{\tilde Q} = e_t$ and the plain products are $\vec e_x$ and $-\vec e_x$.

### The Product Is Not Flexible

**Definition.** The product is **flexible** when $(\tilde Q_1 \star \tilde Q_2) \star \tilde Q_1 = \tilde Q_1 \star (\tilde Q_2 \star \tilde Q_1)$ for all $\tilde Q_1, \tilde Q_2$. From the associator this is the identity $[\tilde Q_1,\tilde Q_2,\tilde Q_1] = 0$.

**Theorem.** The multiplication is not flexible.

**Proof.** At $\tilde Q_1 = ie_t$ and $\tilde Q_2 = e_t$ the two sides are

$$
(ie_t \star e_t) \star ie_t = ie_t \star ie_t = (ie_t)^{\natural}(ie_t)^{*} = (ie_t)(-ie_t) = e_t ,
$$

$$
ie_t \star (e_t \star ie_t) = ie_t \star (-ie_t) = (ie_t)^{\natural}(-ie_t)^{*} = (ie_t)(ie_t)^{\natural} = (ie_t)(ie_t) = -e_t ,
$$

so $[ie_t,e_t,ie_t] = 2e_t \neq 0$.

**Remark.** The flexibility law is the weakest of the classical laws of a non-associative algebra and the one that would be needed to make the powers of an element well defined; it fails here, and it fails on a central element, which is the smallest possible failure. The witness is the one the group article records.

### The Product Is Not Power-Associative

**Definition.** The product is **power-associative** when every element generates an associative subalgebra, equivalently when $x^{p}x^{q} = x^{p+q}$ for all $p, q$; the weakest identity of the family is **third-power associativity**, $(\tilde Q_1 \star \tilde Q_1) \star \tilde Q_1 = \tilde Q_1 \star (\tilde Q_1 \star \tilde Q_1)$, which says that the third power is well defined.

**Theorem.** The multiplication is not power-associative, and the third-power identity fails.

**Proof.** At $\tilde Q_1 = i\vec e_z$ the square is $\tilde Q_1 \star \tilde Q_1 = (i\vec e_z)^{\natural}(i\vec e_z)^{*} = (-i\vec e_z)(i\vec e_z) = -e_t$, so the two groupings of the third power are

$$
(\tilde Q_1 \star \tilde Q_1) \star \tilde Q_1 = (-e_t) \star i\vec e_z = (-e_t)^{\natural}(i\vec e_z)^{*} = (-e_t)(i\vec e_z) = -i\vec e_z ,
$$

$$
\tilde Q_1 \star (\tilde Q_1 \star \tilde Q_1) = i\vec e_z \star (-e_t) = (i\vec e_z)^{\natural}(-e_t)^{*} = (-i\vec e_z)(-e_t) = i\vec e_z .
$$

The two sides are $-i\vec e_z$ and $i\vec e_z$, so the third-power identity fails; equivalently the associator at the triple $(i\vec e_z,i\vec e_z,i\vec e_z)$ is $-i\vec e_z - i\vec e_z = -2i\vec e_z \neq 0$. Since a power-associative algebra satisfies third-power associativity, the product is not power-associative.

**Remark.** The failure of third-power associativity is the strongest of the failures in the sense that it is the weakest law, so a failure there is not implied by the failures above it; the product fails at the bottom rung directly. The group article records the two failures as *The Flexibility and the Degree-Three Identity*.

### The Ladder

**Theorem (the rungs the product misses).** The property ladder of *Non-Associative Algebras and the Property Ladder* has the implications

$$
\text{associative} \implies \text{alternative} \implies \text{flexible} , \qquad \text{alternative} \implies \text{power-associative} ,
$$

and the general quaternionic sesquilinear product satisfies none of the four properties.

**Proof.** The product is not flexible by the second theorem above; since alternative implies flexible, and associative implies alternative, the product is not alternative and not associative. The product fails third-power associativity by the third theorem, and since power-associative implies third-power associativity, the product is not power-associative. The four failures all follow from the failure at the last of the three computations, together with the separate witness of non-flexibility.

**Remark.** An algebra that fails flexibility can still be non-power-associative for a different reason; here the failure of the degree-three identity at a single central element settles power-associativity, and the failure of flexibility at another settles alternativity and associativity. The two witnesses are $i\vec e_z$ and $(ie_t,e_t)$, both as small as possible, and the ladder's strictness is not used: the product lies below every rung.

## The Associator Read on the Plain Product

### The Difference of the Two Plain Products

The formula $[\tilde Q_1,\tilde Q_2,\tilde Q_3] = \overline{\tilde Q_2}\,\tilde Q_1\,\tilde Q_3^{*} - \tilde Q_1^{\natural}\,\tilde Q_3\,\overline{\tilde Q_2}$ exhibits the associator as the difference of two plain products of three factors, and it is worth reading the two terms separately.

**Definition.** The **left term** and the **right term** of the associator are

$$
L(\tilde Q_1,\tilde Q_2,\tilde Q_3) = \overline{\tilde Q_2}\,\tilde Q_1\,\tilde Q_3^{*} , \qquad R(\tilde Q_1,\tilde Q_2,\tilde Q_3) = \tilde Q_1^{\natural}\,\tilde Q_3\,\overline{\tilde Q_2} ,
$$

so that $[\tilde Q_1,\tilde Q_2,\tilde Q_3] = L - R$ by the formula.

**Proposition.** The left term is the left grouping and the right term is the right grouping; the left term carries the conjugations $\overline{\cdot}$ in the middle and ${}^{*}$ in the last factor, and the right term carries the conjugation ${}^{\natural}$ in the first factor and $\overline{\cdot}$ in the last.

**Proof.** The two groupings were computed in the theorem proving the formula. The first term is $(\tilde Q_1 \star \tilde Q_2) \star \tilde Q_3$ and the second is $\tilde Q_1 \star (\tilde Q_2 \star \tilde Q_3)$.

### Examples and the Vanishing Set

**Examples.** The associator vanishes at some triples and not at others.

- $[e_t,e_t,\vec e_x] = -2\vec e_x$, nonzero: the two groupings are $(e_t \star e_t) \star \vec e_x = -\vec e_x$ and $e_t \star (e_t \star \vec e_x) = \vec e_x$.
- $[e_t,\vec e_x,\vec e_x] = 2e_t$, nonzero: the two groupings are $(e_t \star \vec e_x) \star \vec e_x = e_t$ and $e_t \star (\vec e_x \star \vec e_x) = -e_t$.
- $[\vec e_x,\vec e_x,\vec e_x] = 0$, zero: the two groupings are $(\vec e_x \star \vec e_x) \star \vec e_x = (-e_t) \star \vec e_x = \vec e_x$ and $\vec e_x \star (\vec e_x \star \vec e_x) = \vec e_x \star (-e_t) = \vec e_x$.
- $[\vec e_x,\vec e_y,e_t] = 0$, zero: the two groupings are $(\vec e_x \star \vec e_y) \star e_t = \vec e_z \star e_t = -\vec e_z$ and $\vec e_x \star (\vec e_y \star e_t) = \vec e_x \star (-\vec e_y) = -\vec e_z$.

**Remark.** The vanishing set is the set of triples for which the two terms agree, $\overline{\tilde Q_2}\tilde Q_1\tilde Q_3^{*} = \tilde Q_1^{\natural}\tilde Q_3\overline{\tilde Q_2}$; it is a proper algebraic subset of $\mathbb{B}^{3}$ and it contains all triples with a vanishing factor and every triple of real scalar elements, but it is not the whole space. Of the $64$ triples of basis elements, $40$ make the associator vanish and $24$ do not, so the vanishing is the common case on the basis and the non-vanishing is the one that decides the laws. The group article states the same examples.

## The Comparison with the Sibling Associators

**Theorem (the sibling associators).** The associators of the four general products have the following forms:

| product | associator |
|---|---|
| $\tilde Q_1\tilde Q_2$ | $\tilde Q_1(\tilde Q_2\tilde Q_3) - (\tilde Q_1\tilde Q_2)\tilde Q_3 = 0$, the product is associative |
| $\tilde Q_1^{\natural}\tilde Q_2$ | $(\tilde Q_1^{\natural}\tilde Q_2)^{\natural}\tilde Q_3 - \tilde Q_1^{\natural}(\tilde Q_2^{\natural}\tilde Q_3)$ |
| $\tilde Q_1\tilde Q_2^{*}$ | $\tilde Q_1\bigl((\tilde Q_3\tilde Q_2)^{*} - \tilde Q_3\tilde Q_2^{*}\bigr)$ |
| $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | $\overline{\tilde Q_2}\tilde Q_1\tilde Q_3^{*} - \tilde Q_1^{\natural}\tilde Q_3\overline{\tilde Q_2}$ |

**Proof.** The plain product is associative. The sibling bilinear product has the associator obtained by inserting ${}^{\natural}$ in each first slot; it is the same kind of difference of two groupings, with the conjugations ${}^{\natural}$ and the plain form. The sibling sesquilinear associator is the general formula of *The Sesquilinear Associator and the Ternary Product* for the derived operation, $\tilde Q_1((\tilde Q_3\tilde Q_2)^{*} - \tilde Q_3\tilde Q_2^{*})$, with the first factor untouched. The fourth row is the formula of this article.

**Remark.** The three non-associative associators are all differences of two groupings with opposite third-slot parities, and the parity structure is the same for all three: $\mathbb{C}$-linear in the first variable, conjugate-linear in the second, neither in the third. What distinguishes the fourth row from the sibling sesquilinear row is the factor $\overline{\tilde Q_2}$ in front and the ${}^{\natural}$ on $\tilde Q_1$ in the second term; the sibling's associator has the first factor $\tilde Q_1$ untouched, and the fourth product's associator carries the extra $\natural$ that makes it the isotope of the derived operation. This is the associator-level form of the isotope reading of *Introduction to the General Quaternionic Sesqualgebra* §*The Isotope Interpretation*.

## Summary

The associator of the general quaternionic sesquilinear multiplication is

$$
[\tilde Q_1,\tilde Q_2,\tilde Q_3] = \overline{\tilde Q_2}\,\tilde Q_1\,\tilde Q_3^{*} - \tilde Q_1^{\natural}\,\tilde Q_3\,\overline{\tilde Q_2} ,
$$

the difference of the two groupings of the product, each grouping being a plain product of three factors. The associator is $\mathbb{C}$-linear in the first variable, conjugate-linear in the second, and neither linear nor conjugate-linear in the third, so it is a trilinear form on two different mixed modules rather than on $\mathbb{B}^{3}$; it is additive in all three variables. The product is not associative, with witness $[e_t,e_t,\vec e_x] = -2\vec e_x$; it is not flexible, with witness $[ie_t,e_t,ie_t] = 2e_t$; and it is not power-associative, third-power associativity failing at $\tilde Q_1 = i\vec e_z$ with the two sides $-i\vec e_z$ and $i\vec e_z$. The product therefore satisfies none of the four rungs of the property ladder, and each failure is read on a single basis element. The associator vanishes at some triples, the vanishing set being the proper algebraic subset $\overline{\tilde Q_2}\tilde Q_1\tilde Q_3^{*} = \tilde Q_1^{\natural}\tilde Q_3\overline{\tilde Q_2}$ of $\mathbb{B}^{3}$. The sibling sesquilinear associator is $\tilde Q_1((\tilde Q_3\tilde Q_2)^{*} - \tilde Q_3\tilde Q_2^{*})$, and the associator of the fourth product is its isotope by ${}^{\natural}$, carrying the extra factor $\overline{\tilde Q_2}$ and the extra conjugation on the first factor.

## Summary of Notation

| symbol | meaning |
|---|---|
| $[\tilde Q_1,\tilde Q_2,\tilde Q_3]$ | the associator $(\tilde Q_1\star\tilde Q_2)\star\tilde Q_3 - \tilde Q_1\star(\tilde Q_2\star\tilde Q_3)$ |
| $\overline{\tilde Q_2}\tilde Q_1\tilde Q_3^{*} - \tilde Q_1^{\natural}\tilde Q_3\overline{\tilde Q_2}$ | the closed form of the associator |
| $L(\tilde Q_1,\tilde Q_2,\tilde Q_3) = \overline{\tilde Q_2}\tilde Q_1\tilde Q_3^{*}$ | the left term, the left grouping |
| $R(\tilde Q_1,\tilde Q_2,\tilde Q_3) = \tilde Q_1^{\natural}\tilde Q_3\overline{\tilde Q_2}$ | the right term, the right grouping |
| $\mathbb{B} \times \mathbb{B}^{\varsigma} \times \mathbb{B}^{\varsigma}$ | the module of the left grouping |
| $\mathbb{B} \times \mathbb{B}^{\varsigma} \times \mathbb{B}$ | the module of the right grouping |
| $[e_t,e_t,\vec e_x] = -2\vec e_x$ | a witness of non-associativity |
| $[ie_t,e_t,ie_t] = 2e_t$ | a witness of non-flexibility |
| $[i\vec e_z,i\vec e_z,i\vec e_z] = -2i\vec e_z$ | a witness of the failure of third-power associativity |
| $\{ \overline{\tilde Q_2}\tilde Q_1\tilde Q_3^{*} = \tilde Q_1^{\natural}\tilde Q_3\overline{\tilde Q_2} \}$ | the vanishing set of the associator |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the associator, the flexible law and power-associativity.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the degree-three identity and the algebra of the associator.
- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the associator of a multiplication on a module and its linearity properties.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the associator of a product with an involution inserted in a slot.
