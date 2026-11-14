# __The Tensor Square of the Adjoint Module__

## Introduction

The algebra $\mathbb{B}$ is a module over itself for the conjugation action, and as such it is the sum of two carriers, the trivial line and the traceless part. Its tensor square is therefore a module of dimension sixteen, and it decomposes into five irreducible summands. The multiplication of the algebra is a map between two modules, and the decomposition says exactly what it does: it is onto two of the summands and it vanishes on the third.

The result is the reason the list of carriers ends where it does. The carriers are $\mathcal{V}_1$, $\mathcal{V}_2$ and $\mathcal{V}_3$; a product of two carriers lands in a sum of carriers; and the only new summand produced by the tensor square, $\mathcal{V}_5$, is not a carrier and is killed by the multiplication. No product manufactures a type the algebra does not have.

The carriers and their types are *The Carriers of the Biquaternion Algebra*, the number attached to each type is *The Spin of a Carrier*, the weights used in the count are *The Weights of a Carrier*, and the product itself is *The Four General Products and Their Relations over the Biquaternion Algebra* and *Symmetric and Antisymmetric Decomposition of the Four General Products*.

Nothing below is a statement of physics. The types are written $\mathcal{V}_d$ with $d$ the complex dimension, so that $\mathcal{V}_1$ is the trivial module, $\mathcal{V}_3$ the adjoint module and $\mathcal{V}_5$ the module of dimension five; the spin is $(d-1)/2$ throughout.

## The Algebra as a Module

**Proposition.** For the conjugation action, $\mathbb{B}\cong\mathcal{V}_1\oplus\mathcal{V}_3$, with $\mathcal{V}_1=\mathbb{B}_{C}$ and $\mathcal{V}_3=\mathbb{B}_{V}$.

*Proof.* *The Carriers of the Biquaternion Algebra*, §*Three and Not Four*: the trace form is invariant and nondegenerate, its radical-free decomposition is $\mathbb{B}=\mathbb{B}_{C}\oplus\mathbb{B}_{C}^{\perp}$, the complement is the traceless part, and both summands are irreducible.

**Corollary (the dimensions).** $\dim_{\mathbb{C}}\mathbb{B}=4$ and $1+3=4$; the tensor square has complex dimension $16$, and the endomorphism algebra $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ has dimension $16$ as well, the two being canonically dual through the trace form.

**Remark (the multiplication is not an endomorphism).** The product $m:\mathbb{B}\otimes\mathbb{B}\to\mathbb{B}$ is a map of modules, not an element of the algebra: it is the structural map of the algebra, and its properties — associativity, the unit, the invariance — are the properties of that map. The module theory constrains it, and the constraint is the subject of this article.

## The Decomposition of the Tensor Square

**Theorem (Clebsch–Gordan for the two carriers).** The tensor products of the carrier types decompose as

$$
\mathcal{V}_3\otimes\mathcal{V}_3\cong\mathcal{V}_1\oplus\mathcal{V}_3\oplus\mathcal{V}_5,\qquad
\mathcal{V}_1\otimes\mathcal{V}_3\cong\mathcal{V}_3,\qquad
\mathcal{V}_1\otimes\mathcal{V}_1\cong\mathcal{V}_1 .
$$

*Proof.* The weights of $\mathcal{V}_3$ are $+1,0,-1$; the weights of $\mathcal{V}_3\otimes\mathcal{V}_3$ are the sums of two of them, with multiplicity, that is $+2$ once, $+1$ twice, $0$ three times, $-1$ twice and $-2$ once. The right-hand side has weights $+2,+1,0,-1,-2$ from $\mathcal{V}_5$, two copies of $+1,0,-1$ from the two $\mathcal{V}_3$, and one $0$ from $\mathcal{V}_1$, which is the same multiset. A module for the rotation algebra over $\mathbb{C}$ is determined up to isomorphism by its weight multiplicities, so the two sides are isomorphic. The other two products are the unit of the tensor category.

**Corollary (the tensor square of the algebra).**

$$
\mathbb{B}\otimes\mathbb{B}\cong 2\,\mathcal{V}_1\oplus 3\,\mathcal{V}_3\oplus\mathcal{V}_5,
$$

of dimensions $2+9+5=16$.

*Proof.* $(\mathcal{V}_1\oplus\mathcal{V}_3)\otimes(\mathcal{V}_1\oplus\mathcal{V}_3)$ expands into the four products of the theorem, and the copies are collected.

**Remark (the count is complete).** The multiplicity of $\mathcal{V}_5$ is one and the multiplicity of $\mathcal{V}_1$ is two; there is no $\mathcal{V}_7$ and no higher type, because the highest weight of a product of two strings of length three is the sum of the two highest weights, $1+1=2$, and a string of highest weight two has length five. The tensor square of a module of dimension four cannot contain a module of dimension seven.

## The Multiplication Map

**Proposition (equivariance).** The product $m(X\otimes Y)=XY$ commutes with the conjugation action:

$$
m\bigl(uXu^{*}\otimes uYu^{*}\bigr)=u(XY)u^{*}=u\,m(X\otimes Y)\,u^{*}.
$$

*Proof.* Multiply the two conjugated factors and cancel the middle pair, $u^{*}u=e_t$.

**Theorem (what the multiplication does to the summands).** The product is onto $\mathcal{V}_1\oplus\mathcal{V}_3$ and vanishes on $\mathcal{V}_5$:

$$
m\bigl(2\mathcal{V}_1\oplus 3\mathcal{V}_3\bigr)=\mathbb{B},\qquad m\bigl(\mathcal{V}_5\bigr)=0 .
$$

*Proof.* The image of a map of modules is a submodule, and the submodules of $\mathbb{B}$ are $\mathcal{V}_1$, $\mathcal{V}_3$ and their sum; the product is onto because $e_t$ is a unit, so the image is the whole of $\mathcal{V}_1\oplus\mathcal{V}_3$. A map of modules carries an isotypic component into the isotypic component of the same type, and $\mathbb{B}$ has no $\mathcal{V}_5$ summand, so the restriction to $\mathcal{V}_5$ is a map into zero.

**Corollary (no higher carrier).** A product of two elements of carriers lies in a carrier, and the only summand of the tensor square that is not a carrier is annihilated by the product. The algebra therefore generates no type beyond $\mathcal{V}_1$, $\mathcal{V}_2$ and $\mathcal{V}_3$: the first two by multiplication, the third by conjugation.

**Remark (the two-dimensional type is invisible here).** The decomposition above is the decomposition for the conjugation action, under which $\mathbb{B}$ is $\mathcal{V}_1\oplus\mathcal{V}_3$ and the two-dimensional type does not appear. The two-dimensional type is the carrier of the multiplication, and its products are read in the category of left modules, where the tensor product is over the algebra and not over $\mathbb{C}$. The absence of $\mathcal{V}_2$ from this table is not an omission: the adjoint action of the algebra on itself has no two-dimensional summand, and that is the content of *The Carriers of the Biquaternion Algebra*, §*Three and Not Four*.

## The Four Products

**Proposition (the four products are four maps).** Each of the four general products of *The Four General Products and Their Relations over the Biquaternion Algebra* is a map $\mathbb{B}\otimes\mathbb{B}\to\mathbb{B}$ that is equivariant for the conjugation action up to the signs of the conjugations involved; the plain bilinear product is equivariant as stated, the plain sesquilinear one is equivariant for the action composed with the involution, and the quaternionic ones likewise.

*Proof.* Each product is a composition of the multiplication with one or two applications of a conjugation to the factors, and a conjugation is either an automorphism of the module structure or an antiautomorphism, which is an isomorphism onto the module with the conjugated action. The equivariance is the associativity of the multiplication together with $u^{*}u=e_t$.

**Corollary (all four products kill $\mathcal{V}_5$).** Every one of the four products vanishes on the $\mathcal{V}_5$ summand of $\mathbb{B}\otimes\mathbb{B}$, and every one of them is onto a sum of carriers.

*Proof.* Each product is the multiplication composed with maps that permute or conjugate the factors, and conjugation preserves the isotypic components of the tensor square.

**Remark (what this says about the algebra).** The four products are four different pairings of two copies of the algebra, and the module theory says that none of them can produce an isotypic component the algebra does not already have as a module. This is the structural reason the algebra is closed under its own products at the level of types, and it is the reason the list of carriers is short.

## Summary

For the conjugation action, $\mathbb{B}\cong\mathcal{V}_1\oplus\mathcal{V}_3$, and its tensor square is $2\mathcal{V}_1\oplus3\mathcal{V}_3\oplus\mathcal{V}_5$, with dimensions $2+9+5=16$. The multiplicities are read from the weight strings: the sums of two elements of $\{+1,0,-1\}$ give $+2$ once, $+1$ twice, $0$ three times, $-1$ twice and $-2$ once, which is $\mathcal{V}_5\oplus2\mathcal{V}_3\oplus\mathcal{V}_1$.

The multiplication is a map of modules, it is onto $\mathcal{V}_1\oplus\mathcal{V}_3$, and it vanishes on $\mathcal{V}_5$ because the algebra has no five-dimensional summand. All four general products vanish there for the same reason.

Hence no product of carriers produces a new carrier, and no carrier above spin one exists: the highest weight of a tensor product is the sum of the highest weights, the square of the adjoint reaches two, the algebra stops at one, and the summand that overshoots is the one the product annihilates.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathcal{V}_d$ | the carrier type of complex dimension $d$ |
| $\mathcal{V}_1$ | the trivial module, the centre |
| $\mathcal{V}_3$ | the adjoint module, the traceless part |
| $\mathcal{V}_5$ | the module of highest weight two, a summand of the tensor square and not a carrier |
| $\mathbb{B}\cong\mathcal{V}_1\oplus\mathcal{V}_3$ | the algebra as a module for the conjugation |
| $m:\mathbb{B}\otimes\mathbb{B}\to\mathbb{B}$ | the multiplication, a map of modules |
| $2\mathcal{V}_1\oplus3\mathcal{V}_3\oplus\mathcal{V}_5$ | the decomposition of the tensor square |
| Clebsch–Gordan | the rule $\mathcal{V}_{2s+1}\otimes\mathcal{V}_{2s'+1}\cong\bigoplus_{j=|s-s'|}^{s+s'}\mathcal{V}_{2j+1}$ |

## Further Reading

- [The Carriers of the Biquaternion Algebra](the-carriers-of-the-biquaternion-algebra.html), for the three carriers, the isotypic decomposition and the proof that there are no others
- [The Spin of a Carrier](the-spin-of-a-carrier.html), for the number attached to each type
- [The Weights of a Carrier](the-weights-of-a-carrier.html), for the spectra from which the multiplicities are read
- [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the four products and their relations
- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the split of each product into its symmetric and antisymmetric halves
- [The Vector Parts of the Products over the Biquaternion Algebra](the-vector-parts-of-the-products-over-the-biquaternion-algebra.html), for the vector part of each product
- [The Category of Modules in the Biquaternion Algebra](the-category-of-modules.html), for the module category and the tensor product over the algebra
- [Representations of Lie Algebras](representations-of-lie-algebras.html), for the highest-weight classification and the Clebsch–Gordan rule in general
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for the Clebsch–Gordan decomposition of $\mathfrak{su}(2)$-modules.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the multiplicities in the tensor products of the irreducible modules.
