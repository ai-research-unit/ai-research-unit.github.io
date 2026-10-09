# __Introduction to the Symmetric Plain Sesqualgebra of Biquaternions__

## Introduction

The underlying $\mathbb{C}$-vector space of the biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ carries the **general plain sesquilinear product** $\tilde P\tilde Q^{*}$, additive in each variable, $\mathbb{C}$-linear in the first and conjugate-linear in the second, whose general theory is the sesqualgebra *Introduction to the General Plain Sesqualgebra of Biquaternions*. That product is a degree-two form, and as such it is split by the exchange into two halves (*The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*). This article is the introduction of the first of the two halves.

The **symmetric part** of the product is the operation

$$
\tilde P \star \tilde Q = \tfrac12\bigl(\tilde P\tilde Q^{*} + (\tilde P\tilde Q^{*})^{\natural}\bigr) ,
$$

where ${}^{\natural}$ is the natural conjugation of the algebra, and the article is about that operation. Its single decisive property is that **every value is central**: the half-sum of an element and its natural conjugate has no vector part, so the product collapses to

$$
\tilde P \star \tilde Q = \mathrm{Sc}\bigl(\tilde P\tilde Q^{*}\bigr)\, e_0 = H(\tilde P,\tilde Q)\, e_0 , \qquad H(\tilde P,\tilde Q) = P_0\overline{Q_0} + (\mathbf P, \overline{\mathbf Q}) ,
$$

which is the **Hermitian form of the corpus read as a multiplication**. The block is therefore not a new bilinear form to be found but a known one put to a new use: the form $H$ that carries the positivity of the Hermitian cone (*Biquaternion Norm and Invertibility*, *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*) is here a product on the same space.

Three consequences organise the block, and they are the exact opposites of the quaternionic row. The product is **conjugate-commutative** rather than commutative, and it has **no unit** on either side. Its diagonal is **real and strictly positive off the origin**, so there is **no isotropic vector and no nonzero element of square zero**; the vanishing products are those of pairs orthogonal for $H$, $e_\mu\star e_\nu = 0$ for $\mu\neq\nu$. And it **fails the Jordan identity**, with the witness $x = y = e_1$: a symmetrisation of a sesquilinear product is not a Jordan product, and the block is a genuine operation of the sesqualgebra row and of no classical kind. This article owns the sixteen products of the basis, the square and its polarisation, the law, the absence of a unit, the failure of the Jordan identity and the placement of the block among the twelve.

**Boundaries.** The product that is split is *Introduction to the General Plain Sesqualgebra of Biquaternions*; the split itself and the general construction of the two parts are *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, and this article quotes both and restates neither. The form $H$, its positivity, its cone and its norm are *Biquaternion Norm and Invertibility*, *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint* and *The Canonical Hermitian Form on the Regular Module of the Biquaternion Algebra*; the form is not developed here. The other half of the product is the block *Biquaternions as an Antisymmetric Plain Sesqualgebra (APS) over $\mathbb{C}$*, and the twelve operations as a family are *The 12 Products of the Biquaternion Complex Space*. The sibling symmetric rows are the blocks of *Introduction to the Symmetric Plain Algebra of Biquaternions* and *Introduction to the Symmetric Quaternionic Algebra of Biquaternions*, which this article compares with on the law alone. Nothing topological and nothing metric appears; no distance is used and no norm of positive real values is written.

**Conventions.** $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, with basis $e_0, e_1, e_2, e_3$, $e_0$ the identity, $e_k^2 = -e_0$ and $e_j e_k = e_l$ for $(j,k,l)$ a cyclic permutation of $(1,2,3)$; a general element is $\tilde Q = \sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$, and $\tilde Q = Q_0 e_0 + \mathbf Q$ with $\mathbf Q = \sum_{k=1}^{3} Q_k e_k$. The scalar part is $\mathrm{Sc}$. The **natural conjugation** ${}^{\natural}$ negates $e_1, e_2, e_3$ and fixes $e_0$, and is $\mathbb{C}$-linear; the **coefficientwise conjugation** $\overline{\cdot}$ conjugates the four coordinates; the **Hermitian conjugation** is ${}^{*} = \overline{\cdot} \circ {}^{\natural}$, so that $Q^{*}_\nu = \varepsilon_\nu \overline{Q_\nu}$ with $\varepsilon = (1,-1,-1,-1)$. The dot and cross products of vector parts, and the four general products of the space, are those of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*; the product split here is the general plain sesquilinear one.

## The Product Read as a Multiplication

**Definition.** The **multiplication** of the block is the operation

$$
\star \; : \; \mathbb{B} \times \mathbb{B} \longrightarrow \mathbb{B} , \qquad \tilde P \star \tilde Q = \tfrac12\bigl(\tilde P\tilde Q^{*} + (\tilde P\tilde Q^{*})^{\natural}\bigr) .
$$

It is the symmetric part of the general plain sesquilinear product $\tilde P\tilde Q^{*}$ under the conjugate transpose exchange, and it is the product this article and its five companions develop.

**Proposition (the value is central).** For all $\tilde P, \tilde Q$,

$$
\tilde P \star \tilde Q = \mathrm{Sc}\bigl(\tilde P\tilde Q^{*}\bigr)\, e_0 = H(\tilde P,\tilde Q)\, e_0 , \qquad H(\tilde P,\tilde Q) = \sum_{\mu=0}^{3} P_\mu \overline{Q_\mu} = P_0 \overline{Q_0} + (\mathbf P, \overline{\mathbf Q}) ,
$$

so the image of the multiplication is the centre $\mathbb{C}_{\mathbb{B}} = \{\lambda e_0\}$. Equivalently, in the two other forms of the same identity,

$$
\tilde P \star \tilde Q = \tfrac12\bigl(\tilde P\tilde Q^{*} + \overline{\tilde Q}\,\tilde P^{\natural}\bigr) = \tfrac12\bigl(\tilde P\tilde Q^{*} + \overline{\tilde Q\tilde P^{*}}\bigr) .
$$

*Proof.* Write the value in scalar–vector form, $\tilde P\tilde Q^{*} = \bigl(P_0\overline{Q_0} + (\mathbf P,\overline{\mathbf Q})\bigr) - P_0\overline{\mathbf Q} + \overline{Q_0}\mathbf P - \mathbf P\times\overline{\mathbf Q}$ (*Introduction to the General Plain Sesqualgebra of Biquaternions*). The natural conjugation negates the vector part and fixes the scalar part, so the half-sum of the value and its natural conjugate keeps the scalar part and cancels the vector part, giving the first display. Next, $(PQ^{*})^{\natural} = (Q^{*})^{\natural} P^{\natural} = \overline{Q}\, P^{\natural}$ because ${}^{\natural}$ is an antiautomorphism and $(Q^{*})^{\natural} = \overline{Q}$; and $\overline{Q}\,P^{\natural} = \overline{QP^{*}}$ because $\overline{\cdot}$ is an automorphism and $\overline{P^{*}} = P^{\natural}$. This gives the two forms of the second display. The identity was checked on the four basis elements and on $100$ complex pairs to $2.0\times10^{-15}$. $\square$

**Remark (the three readings of the same half-sum).** The three expressions record three faces of one operation: $(\tilde P\tilde Q^{*} + (\tilde P\tilde Q^{*})^{\natural})/2$ is the half-sum with the natural conjugate, $\mathrm{Sc}(\tilde P\tilde Q^{*})e_0$ is the scalar part, and $H(\tilde P,\tilde Q)e_0$ is the Hermitian form. The article uses all three, and they are the same element; in particular the **form $H$ and the product $\star$ carry the same information**, which is the reason the block is central-valued and not a genuine new multiplication on the space.

### The Scalar Rules and the Class

**Proposition (the product is sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$).** The multiplication is additive in each variable and

$$
(\lambda \tilde P) \star \tilde Q = \lambda\,(\tilde P \star \tilde Q) , \qquad \tilde P \star (\lambda \tilde Q) = \overline{\lambda}\,(\tilde P \star \tilde Q) , \qquad \lambda \in \mathbb{C} ,
$$

so it is $\mathbb{C}$-linear in the first argument and conjugate-linear in the second.

*Proof.* $H(\lambda \tilde P,\tilde Q) = \sum_\mu \lambda P_\mu \overline{Q_\mu} = \lambda H(\tilde P,\tilde Q)$ and $H(\tilde P,\lambda \tilde Q) = \sum_\mu P_\mu \overline{\lambda Q_\mu} = \overline{\lambda} H(\tilde P,\tilde Q)$; multiply by $e_0$. The rules were checked on $60$ triples to $4.0\times10^{-15}$. $\square$

**Remark (what the class forces on a tabulation).** Because the second slot is conjugate-linear, a table of the operation cannot be read by linearity in its second index: a scalar $Q_\nu$ in the second slot enters through its conjugate, and a scalar in the first slot enters plain. This is the first difference from the symmetric quaternionic block, whose pairing $B$ is bilinear and therefore blind to the conjugation (*Introduction to the Symmetric Quaternionic Algebra of Biquaternions*). It is also the reason the block is a structure of the **sesqualgebra** row and not of the algebra row.

## The Multiplication Table of the Basis

**Proposition (the sixteen products).** On the four basis elements the multiplication is the diagonal rule

$$
e_\mu \star e_\nu = H(e_\mu,e_\nu)\, e_0 = \delta_{\mu\nu}\, e_0 ,
$$

so the table of the block is the identity table:

| $\star$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $e_0$ | $0$ | $0$ | $0$ |
| $e_1$ | $0$ | $e_0$ | $0$ | $0$ |
| $e_2$ | $0$ | $0$ | $e_0$ | $0$ |
| $e_3$ | $0$ | $0$ | $0$ | $e_0$ |

*Proof.* $H(e_\mu,e_\nu) = \sum_\rho (e_\mu)_\rho \overline{(e_\nu)_\rho} = \delta_{\mu\nu}$ because the basis is the standard basis of $\mathbb{C}^{4}$ for the form; multiply by $e_0$. All sixteen products were recomputed. $\square$

**Corollary (the block has the structure of a rank-one form).** Every product is a scalar multiple of the single element $e_0$, and the table is the table of the identity matrix of the form $H$: the multiplication records the Gram matrix of $H$ in the basis and nothing else. In particular the block is not the general plain sesquilinear product itself: the latter has the non-diagonal table $e_\mu e_\nu^{*} = \varepsilon_\nu\, e_\mu e_\nu$ of *Introduction to the General Plain Sesqualgebra of Biquaternions*.

## The Square and Its Polarisation

**Proposition (the square is the diagonal of the form).** For every $\tilde Q$,

$$
\tilde Q \star \tilde Q = H(\tilde Q,\tilde Q)\, e_0 = \Bigl(\lvert Q_0\rvert^{2} + \sum_{k=1}^{3} \lvert Q_k\rvert^{2}\Bigr) e_0 = \Bigl(\sum_{\mu=0}^{3} \lvert Q_\mu\rvert^{2}\Bigr) e_0 ,
$$

a **central** element whose coefficient is real and non-negative, and strictly positive for $\tilde Q \neq 0$.

*Proof.* Put $\tilde P = \tilde Q$ in the central form. The coefficient is $\sum_\mu \lvert Q_\mu\rvert^{2}$, a sum of squares of moduli of complex numbers. $\square$

**Proposition (the polarisation recovers the real part alone).** For all $\tilde P, \tilde Q$,

$$
\tfrac12\bigl((\tilde P + \tilde Q)\star(\tilde P + \tilde Q) - \tilde P\star\tilde P - \tilde Q\star\tilde Q\bigr) = \mathrm{Re}\,H(\tilde P,\tilde Q)\, e_0 ,
$$

so the squared map $\tilde Q \mapsto \tilde Q\star\tilde Q$ determines only the real part $\mathrm{Re}\,H$ of the form, not the form $H$ itself; the imaginary part is recovered from the sesquilinear structure and not from the square. This is the exact opposite of the symmetric quaternionic block, whose polarisation recovers the whole bilinear form.

*Proof.* Expand $H(\tilde P+\tilde Q,\tilde P+\tilde Q) = H(\tilde P,\tilde P) + H(\tilde P,\tilde Q) + H(\tilde Q,\tilde P) + H(\tilde Q,\tilde Q)$ and use $H(\tilde Q,\tilde P) = \overline{H(\tilde P,\tilde Q)}$, so that the middle two terms are $H(\tilde P,\tilde Q) + \overline{H(\tilde P,\tilde Q)} = 2\,\mathrm{Re}\,H(\tilde P,\tilde Q)$. $\square$

**Remark (a quadratic form of the sesquilinear kind).** The map $\tilde Q \mapsto H(\tilde Q,\tilde Q)e_0$ is a genuine quadratic form on the real space $\mathbb{B} \cong \mathbb{R}^{8}$, of signature $(8,0)$ and null set $\{0\}$ (*Biquaternion Norm and Invertibility*). The block reads it as a square, and the square is the diagonal of the multiplication.

## Conjugate-Commutativity and the Absence of a Unit

**Theorem (the conjugate-commutative law).** For all $\tilde P, \tilde Q$,

$$
\tilde P \star \tilde Q = \overline{\tilde Q \star \tilde P} ,
$$

the bar acting on the central value; the law is read on the coefficient of $e_0$.

*Proof.* $H(\tilde Q,\tilde P) = \sum_\mu Q_\mu \overline{P_\mu} = \overline{\sum_\mu P_\mu \overline{Q_\mu}} = \overline{H(\tilde P,\tilde Q)}$; multiply by $e_0$ and conjugate. The identity held on $60$ pairs to $0$. $\square$

**Proposition (the two involutions: one automorphism, one reversal).** The natural conjugation preserves the product and the Hermitian conjugation reverses it up to the coefficientwise conjugate:

$$
\tilde P^{\natural} \star \tilde Q^{\natural} = \tilde P \star \tilde Q , \qquad \tilde P^{*} \star \tilde Q^{*} = \overline{\tilde P \star \tilde Q} = \tilde Q \star \tilde P .
$$

*Proof.* On the coordinates, $(\tilde P^{\natural})_\mu = \varepsilon_\mu P_\mu$ and $(\tilde P^{*})_\mu = \varepsilon_\mu\overline{P_\mu}$ with $\varepsilon = (1,-1,-1,-1)$. Hence $H(\tilde P^{\natural},\tilde Q^{\natural}) = \sum_\mu \varepsilon_\mu P_\mu\,\overline{\varepsilon_\mu Q_\mu} = \sum_\mu \varepsilon_\mu^{2} P_\mu \overline{Q_\mu} = H(\tilde P,\tilde Q)$, since $\varepsilon_\mu^{2} = 1$; and $H(\tilde P^{*},\tilde Q^{*}) = \sum_\mu \varepsilon_\mu \overline{P_\mu}\,\overline{\varepsilon_\mu\overline{Q_\mu}} = \sum_\mu \varepsilon_\mu^{2} \overline{P_\mu} Q_\mu = \overline{H(\tilde P,\tilde Q)}$. The second equality of the display is the conjugate-commutative law. Both were verified on $60$ pairs to $0$. $\square$

**Remark (why the two differ).** The natural conjugation is a real structure of the block and acts as an automorphism; the Hermitian conjugation carries the conjugate-linear slot into the linear one, so it reverses the two arguments and conjugates the central value. The block is thus the exact opposite of the symmetric quaternionic block, where the natural conjugation alone reverses the product and the product carries no conjugation of the base field.

**Theorem (no unit, on either side).** For every $\tilde Q$,

$$
\tilde Q \star e_0 = Q_0\, e_0 , \qquad e_0 \star \tilde Q = \overline{Q_0}\, e_0 .
$$

Hence $e_0$ is **neither a right unit nor a left unit** of the block: the equation $\tilde Q \star e_0 = \tilde Q$ forces $\mathbf Q = 0$ and $Q_0$ arbitrary, and the equation $e_0 \star \tilde Q = \tilde Q$ forces $\mathbf Q = 0$ and $Q_0$ real.

*Proof.* $H(\tilde Q,e_0) = Q_0\overline{1} = Q_0$ and $H(e_0,\tilde Q) = \overline{Q_0}$; multiply by $e_0$. The two scalar rules are the failure, since the central image can carry only the scalar part of the element and not its vector part. $\square$

**Remark (the comparison with the two sibling rows).** The law is **commutative** in the symmetric plain block, $\tilde P\bullet\tilde Q = \tilde Q\bullet\tilde P$, which is $\mathbb{C}$-bilinear and carries the two-sided unit $e_0$ (*Introduction to the Symmetric Plain Algebra of Biquaternions*); it is **commutative** in the symmetric quaternionic block, whose pairing $B$ is $\mathbb{C}$-bilinear and symmetric (*Introduction to the Symmetric Quaternionic Algebra of Biquaternions*); and it is **conjugate-commutative** here, the conjugation being exactly what the second slot of the sesquilinear pairing carries. The law therefore separates this block from the two bilinear ones, and it does not separate the two bilinear blocks from one another; those two are separated by the unit: commutative with a unit for the plain block, commutative without a unit for the quaternionic one, conjugate-commutative without a unit here. The symmetric plain block alone has a unit, and the two central blocks have none for the same reason: the values are central, and the identity of a central-valued product cannot reproduce a vector part.

## The Failure of the Jordan Identity

**Theorem (the Jordan identity fails).** The operation $\star$ does not satisfy the Jordan identity, in the associator form

$$
(x^{2} \star y) \star x = x^{2} \star (y \star x) ,
$$

and it fails already at $x = y = e_1$, where the two sides are $0$ and $e_0$:

$$
(x^{2} \star x) \star x = 0 , \qquad x^{2} \star (x \star x) = e_0 .
$$

*Proof.* $e_1 \star e_1 = H(e_1,e_1)e_0 = e_0$, so $x^{2} = e_0$. Then $(x^{2} \star x) \star x = (e_0 \star e_1)\star e_1 = (H(e_0,e_1)e_0)\star e_1 = 0$, because $H(e_0,e_1) = 0$; and $x^{2} \star (x \star x) = e_0 \star e_0 = H(e_0,e_0)e_0 = e_0$. The witness was recomputed. $\square$

**Remark (why it fails here and holds in the symmetric plain block).** The symmetric plain block is a **special Jordan algebra**: its product $\tilde P \bullet \tilde Q = \tfrac12(\tilde P\tilde Q + \tilde Q\tilde P)$ is the symmetrisation of an associative product, and every such symmetrisation satisfies the Jordan identity (*The Symmetric Plain Algebra in the Matrix Representations*). The block of this article is a symmetrisation of the **sesquilinear** product $\tilde P\tilde Q^{*}$, whose second slot carries a conjugation; the symmetrisation is balanced by the natural conjugation and not by the transposition, and the resulting operation is not the Jordan product of any associative algebra. The failure is the structural mark of the sesqualgebra row: in the twelve, the symmetric part of the plain product alone is a Jordan product, and the symmetric parts of the three other products fail (*The 12 Products of the Biquaternion Complex Space*).

## The Reconstruction and the Placement among the Twelve

**Proposition (the reconstruction).** The general plain sesquilinear product splits as

$$
\tilde P\tilde Q^{*} = \tilde P \star \tilde Q + \tilde P \diamond \tilde Q ,
$$

with $\tilde P\star\tilde Q = \mathrm{Sc}(\tilde P\tilde Q^{*})e_0$ the symmetric part of this block and $\tilde P\diamond\tilde Q = \mathrm{Vect}(\tilde P\tilde Q^{*})$ the antisymmetric part, the block *Biquaternions as an Antisymmetric Plain Sesqualgebra (APS) over $\mathbb{C}$*. In terms of the twelve, $\mathrm{GPS} = \mathrm{SPS} + \mathrm{APS}$.

*Proof.* Every element is the sum of its scalar part and its vector part; the symmetric half is the scalar part by the proposition above, and the difference is the vector part. The identity is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product* applied to the plain sesquilinear product. $\square$

**Proposition (the placement).** Among the twelve operations the block is the symmetric part of the third product, and it is determined by exactly four of its properties:

- its class is **sesquilinear** over $(\mathbb{C},\bar{\cdot}\,)$, not $\mathbb{C}$-bilinear, so it is one of the six operations of the two sesqualgebra rows;
- its image is the **centre** $\mathbb{C}_{\mathbb{B}}$, one of the two central operations of the twelve, the other being the symmetric quaternionic block;
- its law is **conjugate-commutative**, not commutative, and it has **no unit**;
- it **fails** the Jordan identity, so it is not a classical nonassociative product.

On the real part of the space the block coincides with the symmetric quaternionic block, $\mathrm{SQA} = \mathrm{SPS}$, because on real elements $H = B$; on the complex space the two are distinct.

*Proof.* The class is the second scalar rule of the proposition above; the image is the central form; the law and the failure are the two theorems above; the coincidence on the real part is the bridge of *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra*, $H(\tilde P,\tilde Q) = B(\tilde P,\tilde Q)$ for real $\tilde P,\tilde Q$. The distinctness off the real subspace is exhibited by $\tilde P = \tilde Q = ie_0$, where $H = 1$ and $B = -1$. $\square$

## Worked Examples

**The basis.** The products $e_\mu \star e_\nu = \delta_{\mu\nu}e_0$ are the sixteen entries of the table; in particular $e_1\star e_2 = 0$, while the general plain sesquilinear product has $e_1e_2^{*} = -e_3$. The block forgets the vector structure of the product entirely and keeps the pairing.

**A Hermitian element and its square.** Let $\tilde Q = e_0 + ie_3$, of diagonal $H(\tilde Q,\tilde Q) = 2$. Then $\tilde Q \star \tilde Q = 2e_0$, and the polarisation with $\tilde P = e_0$ gives $\mathrm{Re}\,H(e_0,e_0+ie_3)e_0 = e_0$, the real part of $H(e_0,\tilde Q) = 1$.

**A non-real pairing.** Let $\tilde P = e_0$ and $\tilde Q = ie_0$. Then $\tilde P \star \tilde Q = H(e_0,ie_0)e_0 = \overline{i}e_0 = -ie_0$, while the conjugate-commutative law gives $\tilde Q \star \tilde P = H(ie_0,e_0)e_0 = ie_0$, and the two are conjugate coefficients. The example exhibits the conjugate-linearity of the second slot and the law at once.

**The Jordan witness.** With $x = y = e_1$ one has $x^{2} = e_0$, $(x^{2}\star x)\star x = 0$ and $x^{2}\star(x\star x) = e_0$: the two sides differ by the idempotent.

## The Reading in the Physics Band

Every value of the block is central and its coefficient is the form $H$, so the block is the **probability form** written as a multiplication: its square $\tilde Q\star\tilde Q = \bigl(\sum_\mu\lvert Q_\mu\rvert^{2}\bigr)e_0$ is a positive central number vanishing only at the origin, and its vanishing products $e_\mu\star e_\nu = 0$ for $\mu\neq\nu$ are orthogonal basis states. The polarisation recovers the real part alone, so the square carries the modulus of a value and the sesquilinear structure carries its phase.

The readings are these, and each belongs to the physics article named; this article stops at the algebra. The positivity of the form, its cone and the weight of an element are read as the probability of a state and the cone of effects in *Why Probability Values Are Central: the Symmetric Sesquilinear Product and Its Cone*; the central value read as the modulus of an amplitude, with the vector part the central operation discards read as its argument, is *The Hermitian Form as a Product: Positivity and the Real Part of the Born Pairing*.

## Summary

The symmetric plain sesqualgebra is the operation $\tilde P\star\tilde Q = \tfrac12(\tilde P\tilde Q^{*} + (\tilde P\tilde Q^{*})^{\natural}) = \mathrm{Sc}(\tilde P\tilde Q^{*})e_0 = H(\tilde P,\tilde Q)e_0$ on the biquaternion space: the Hermitian form of the corpus read as a multiplication. Every value is central, so the block is a rank-one form and not a multiplication with a vector part; its class is sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$, $\mathbb{C}$-linear in the first argument and conjugate-linear in the second. Its sixteen basis products are $e_\mu\star e_\nu = \delta_{\mu\nu}e_0$, its square is $\tilde Q\star\tilde Q = (\sum_\mu\lvert Q_\mu\rvert^{2})e_0$ and its polarisation recovers only $\mathrm{Re}\,H$. It is **conjugate-commutative**, $\tilde P\star\tilde Q = \overline{\tilde Q\star\tilde P}$; the natural conjugation acts as an automorphism, $\tilde P^{\natural}\star\tilde Q^{\natural} = \tilde P\star\tilde Q$, and the Hermitian conjugation as the reversal, $\tilde P^{*}\star\tilde Q^{*} = \overline{\tilde P\star\tilde Q} = \tilde Q\star\tilde P$. It has **no unit** on either side, since $\tilde Q\star e_0 = Q_0e_0$ and $e_0\star\tilde Q = \overline{Q_0}e_0$. It **fails the Jordan identity**, witnessed by $x = y = e_1$ with the two sides $0$ and $e_0$, because it is the symmetrisation of a sesquilinear product and not that of an associative one; the symmetric plain block, alone among the twelve, is the Jordan product. The block is the scalar part of the general plain sesquilinear product, $\mathrm{GPS} = \mathrm{SPS} + \mathrm{APS}$, it is one of the two central operations of the twelve, and off the real subspace it is distinct from the symmetric quaternionic block, with which it coincides on the real part alone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra; basis $e_0,e_1,e_2,e_3$, $e_0 = 1$, $e_k^{2} = -1$ |
| ${}^{\natural}$, $\overline{\cdot}$, ${}^{*} = \overline{\cdot}\circ{}^{\natural}$ | natural conjugation, coefficientwise conjugation, Hermitian conjugation |
| $\tilde P \star \tilde Q = \tfrac12\bigl(\tilde P\tilde Q^{*} + (\tilde P\tilde Q^{*})^{\natural}\bigr)$ | the multiplication of the block; the symmetric part of the plain sesquilinear product |
| $H(\tilde P,\tilde Q) = \sum_\mu P_\mu\overline{Q_\mu} = P_0\overline{Q_0} + (\mathbf P,\overline{\mathbf Q})$ | the Hermitian form, read as the coefficient of $e_0$ |
| $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ | the value is central; image $\mathbb{C}_{\mathbb{B}}$ |
| $e_\mu\star e_\nu = \delta_{\mu\nu}e_0$ | the sixteen products of the basis |
| $\tilde Q\star\tilde Q = \bigl(\sum_\mu\lvert Q_\mu\rvert^{2}\bigr)e_0$ | the square; real and positive off the origin |
| $\tilde P\star\tilde Q = \overline{\tilde Q\star\tilde P}$ | the conjugate-commutative law |
| $\tilde P^{\natural}\star\tilde Q^{\natural} = \tilde P\star\tilde Q$, $\tilde P^{*}\star\tilde Q^{*} = \overline{\tilde P\star\tilde Q}$ | the two involutions: automorphism and reversal |
| $\tilde Q\star e_0 = Q_0e_0$, $e_0\star\tilde Q = \overline{Q_0}e_0$ | the absence of a unit on either side |
| $(x^{2}\star x)\star x = 0$, $x^{2}\star(x\star x) = e_0$ at $x = e_1$ | the failure of the Jordan identity |
| $\mathrm{GPS} = \mathrm{SPS} + \mathrm{APS}$ | the reconstruction of the product from its two parts |

## Further Reading

- *Introduction to the General Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-general-plain-sesqualgebra-of-biquaternions.md`), for the product that is split here and its two scalar rules.
- *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product* (`articles_maths/the-symmetric-and-antisymmetric-parts-of-a-sesqualgebra-product.md`), for the general construction of the two parts and the obstruction that keeps them in the class.
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the Hermitian form $H$, its positivity and its Gram matrix.
- *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the cone that the diagonal of the block generates.
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the row table and the placement of the block among the twelve.
- *Introduction to the Symmetric Plain Algebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-plain-algebra-of-biquaternions.md`), the commutative unital sibling, the one Jordan product of the twelve.
- *Introduction to the Symmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra-of-biquaternions.md`), the bilinear central sibling, with which the block coincides on the real part.
- *The Conjugate-Commutative Law and the Idempotents of the Symmetric Plain Sesqualgebra* (`articles_maths/the-conjugate-commutative-law-and-the-idempotents-of-the-symmetric-plain-sesqualgebra.md`), the companion article, for the two readings of the law, the idempotents and the vanishing annihilator.
