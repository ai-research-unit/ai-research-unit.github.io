# __Introduction to the Symmetric Plain Sesqualgebra__

## Introduction

The underlying $\mathbb{C}$-vector space of the biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ carries the **general plain sesquilinear product** $\tilde Q_1\tilde Q_2^{*}$, additive in each variable, $\mathbb{C}$-linear in the first and conjugate-linear in the second, whose general theory is the sesqualgebra *Introduction to the General Plain Sesqualgebra*. That product is a degree-two form, and as such it is split by the exchange into two halves (*The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*). This article is the introduction of the first of the two halves.

The **symmetric part** of the product is the operation

$$
\tilde Q_1 \star \tilde Q_2 = \tfrac12\bigl(\tilde Q_1\tilde Q_2^{*} + (\tilde Q_1\tilde Q_2^{*})^{\natural}\bigr) ,
$$

where ${}^{\natural}$ is the natural conjugation of the algebra, and the article is about that operation. Its single decisive property is that **every value is central**: the half-sum of an element and its natural conjugate has no vector part, so the product collapses to

$$
\tilde Q_1 \star \tilde Q_2 = \mathrm{Sc}\bigl(\tilde Q_1\tilde Q_2^{*}\bigr)\, e_t = \langle\tilde Q_1,\tilde Q_2\rangle_{*}\, e_t , \qquad \langle\tilde Q_1,\tilde Q_2\rangle_{*} = Q_{1t}\overline{Q_{2t}} + (\vec Q_1, \overline{\vec Q_2}) ,
$$

which is the **Hermitian form of the corpus read as a multiplication**. The block is therefore not a new bilinear form to be found but a known one put to a new use: the form $\langle\cdot,\cdot\rangle_{*}$ that carries the positivity of the Hermitian cone (*The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*, *Positivity and the Hermitian Cone of the Biquaternioid Algebra with Hermitian Adjoint*) is here a product on the same space.

Three consequences organise the block, and they are the exact opposites of the quaternionic row. The product is **conjugate-commutative** rather than commutative, and it has **no unit** on either side. Its diagonal is **real and strictly positive off the origin**, so there is **no nonzero isotropic vector and no nonzero element of square zero**; the vanishing products are those of pairs orthogonal for $\langle\cdot,\cdot\rangle_{*}$, $e_\mu\star e_\nu = 0$ for $\mu\neq\nu$. And it **fails the Jordan identity**, with the witness $x = y = \vec e_x$: a symmetrisation of a sesquilinear product is not a Jordan product, and the block is a genuine operation of the sesqualgebra row and of no classical kind. This article owns the sixteen products of the basis, the square and its polarisation, the law, the absence of a unit, the failure of the Jordan identity and the placement of the block among the twelve.

**Boundaries.** The product that is split is *Introduction to the General Plain Sesqualgebra*; the split itself and the general construction of the two parts are *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, and this article quotes both and restates neither. The form $\langle\cdot,\cdot\rangle_{*}$, its positivity, its cone and its norm are *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*, *Positivity and the Hermitian Cone of the Biquaternioid Algebra with Hermitian Adjoint* and *The Canonical Hermitian Form on the Regular Module of the Biquaternioid Algebra*; the form is not developed here. The other half of the product is the block *Biquaternions as an Antisymmetric Plain Sesqualgebra (APS) over $\mathbb{C}$*, and the twelve operations as a family are *The 12 Products of the Biquaternioid Complex Space*. The sibling symmetric rows are the blocks of *Introduction to the Symmetric Plain Algebra* and *Introduction to the Symmetric Quaternionic Algebra*, which this article compares with on the law alone. Nothing topological and nothing metric appears.

**Conventions.** $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, with basis $e_t, \vec e_x, \vec e_y, \vec e_z$, $e_t$ the identity, $\vec e_\mu^2 = -e_t$ and $\vec e_\mu \vec e_\nu = \vec e_\lambda$ for $(\mu,\nu,\lambda)$ a cyclic permutation of $(1,2,3)$; a general element is $\tilde Q = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$, and $\tilde Q = Q_t e_t + \vec Q$ with $\vec Q = \sum_{k=1}^{3} Q_k \vec e_k$. The scalar part is $\mathrm{Sc}$. The **natural conjugation** ${}^{\natural}$ negates $\vec e_x, \vec e_y, \vec e_z$ and fixes $e_t$, and is $\mathbb{C}$-linear; the **coefficientwise conjugation** $\overline{\cdot}$ conjugates the four coordinates; the **Hermitian conjugation** is ${}^{*} = \overline{\cdot} \circ {}^{\natural}$, so that $Q^{*}_\nu = \varepsilon_\nu \overline{Q_\nu}$ with $\varepsilon = (1,-1,-1,-1)$. The dot and cross products of vector parts, and the four general products of the space, are those of *The Four General Products of the Biquaternioid $\mathbb{C}$ Space*; the product split here is the general plain sesquilinear one.

## The Product Read as a Multiplication

**Definition.** The **multiplication** of the block is the operation

$$
\star \; : \; \mathbb{B} \times \mathbb{B} \longrightarrow \mathbb{B} , \qquad \tilde Q_1 \star \tilde Q_2 = \tfrac12\bigl(\tilde Q_1\tilde Q_2^{*} + (\tilde Q_1\tilde Q_2^{*})^{\natural}\bigr) .
$$

It is the symmetric part of the general plain sesquilinear product $\tilde Q_1\tilde Q_2^{*}$ under the conjugate transpose exchange, and it is the product this article and its companion articles develop.

**Proposition (the value is central).** For all $\tilde Q_1, \tilde Q_2$,

$$
\tilde Q_1 \star \tilde Q_2 = \mathrm{Sc}\bigl(\tilde Q_1\tilde Q_2^{*}\bigr)\, e_t = \langle\tilde Q_1,\tilde Q_2\rangle_{*}\, e_t , \qquad \langle\tilde Q_1,\tilde Q_2\rangle_{*} = \sum_{\mu\in\{t,x,y,z\}} Q_{1,\mu} \overline{Q_{2,\mu}} = Q_{1t} \overline{Q_{2t}} + (\vec Q_1, \overline{\vec Q_2}) ,
$$

so the image of the multiplication is the centre $\mathbb{C}_{\mathbb{B}} = \{\lambda e_t\}$. Equivalently, in the two other forms of the same identity,

$$
\tilde Q_1 \star \tilde Q_2 = \tfrac12\bigl(\tilde Q_1\tilde Q_2^{*} + \overline{\tilde Q_2}\,\tilde Q_1^{\natural}\bigr) = \tfrac12\bigl(\tilde Q_1\tilde Q_2^{*} + \overline{\tilde Q_2\tilde Q_1^{*}}\bigr) .
$$

*Proof.* Write the value in scalar–vector form, $\tilde Q_1\tilde Q_2^{*} = \bigl(Q_{1t}\overline{Q_{2t}} + (\vec Q_1,\overline{\vec Q_2})\bigr) - Q_{1t}\overline{\vec Q_2} + \overline{Q_{2t}}\vec Q_1 - \vec Q_1\times\overline{\vec Q_2}$ (*Introduction to the General Plain Sesqualgebra*). The natural conjugation negates the vector part and fixes the scalar part, so the half-sum of the value and its natural conjugate keeps the scalar part and cancels the vector part, giving the first display. Next, $(\tilde Q_1\tilde Q_2^{*})^{\natural} = (\tilde Q_2^{*})^{\natural} \tilde Q_1^{\natural} = \overline{\tilde Q_2}\, \tilde Q_1^{\natural}$ because ${}^{\natural}$ is an antiautomorphism and $(\tilde Q_2^{*})^{\natural} = \overline{\tilde Q_2}$; and $\overline{\tilde Q_2}\,\tilde Q_1^{\natural} = \overline{\tilde Q_1\tilde Q_2^{*}}$ because $\overline{\cdot}$ is an automorphism and $\overline{\tilde Q_1^{*}} = \tilde Q_1^{\natural}$. This gives the two forms of the second display.

**Remark (the three readings of the same half-sum).** The three expressions record three faces of one operation: $(\tilde Q_1\tilde Q_2^{*} + (\tilde Q_1\tilde Q_2^{*})^{\natural})/2$ is the half-sum with the natural conjugate, $\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})e_t$ is the scalar part, and $\langle\tilde Q_1,\tilde Q_2\rangle_{*}e_t$ is the Hermitian form. The article uses all three, and they are the same element; in particular the **form $\langle\cdot,\cdot\rangle_{*}$ and the product $\star$ carry the same information**, which is the reason the block is central-valued and not a genuine new multiplication on the space.

### The Scalar Rules and the Class

**Proposition (the product is sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$).** The multiplication is additive in each variable and

$$
(\lambda \tilde Q_1) \star \tilde Q_2 = \lambda\,(\tilde Q_1 \star \tilde Q_2) , \qquad \tilde Q_1 \star (\lambda \tilde Q_2) = \overline{\lambda}\,(\tilde Q_1 \star \tilde Q_2) , \qquad \lambda \in \mathbb{C} ,
$$

so it is $\mathbb{C}$-linear in the first argument and conjugate-linear in the second.

*Proof.* $\langle\lambda \tilde Q_1,\tilde Q_2\rangle_{*} = \sum_\mu \lambda Q_{1,\mu} \overline{Q_{2,\mu}} = \lambda \langle\tilde Q_1,\tilde Q_2\rangle_{*}$ and $\langle\tilde Q_1,\lambda \tilde Q_2\rangle_{*} = \sum_\mu Q_{1,\mu} \overline{\lambda Q_{2,\mu}} = \overline{\lambda} \langle\tilde Q_1,\tilde Q_2\rangle_{*}$; multiply by $e_t$.

**Remark (what the class forces on a tabulation).** Because the second slot is conjugate-linear, a table of the operation cannot be read by linearity in its second index: a scalar $Q_\nu$ in the second slot enters through its conjugate, and a scalar in the first slot enters plain. This is the first difference from the symmetric quaternionic block, whose pairing $N$ is bilinear and therefore blind to the conjugation (*Introduction to the Symmetric Quaternionic Algebra*). It is also the reason the block is a structure of the **sesqualgebra** row and not of the algebra row.

## The Multiplication Table of the Basis

**Proposition (the sixteen products).** On the four basis elements the multiplication is the diagonal rule

$$
e_\mu \star e_\nu = \langle e_\mu,e_\nu\rangle_{*}\, e_t = \delta_{\mu\nu}\, e_t ,
$$

so the table of the block is the identity table:

| $\star$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $0$ | $0$ | $0$ |
| $\vec e_x$ | $0$ | $e_t$ | $0$ | $0$ |
| $\vec e_y$ | $0$ | $0$ | $e_t$ | $0$ |
| $\vec e_z$ | $0$ | $0$ | $0$ | $e_t$ |

*Proof.* $\langle e_\mu,e_\nu\rangle_{*} = \sum_\rho (e_\mu)_\rho \overline{(e_\nu)_\rho} = \delta_{\mu\nu}$ because the basis is the standard basis of $\mathbb{C}^{4}$ for the form; multiply by $e_t$.

**Corollary (the block has the structure of a rank-one form).** Every product is a scalar multiple of the single element $e_t$, and the table is the table of the identity matrix of the form $\langle\cdot,\cdot\rangle_{*}$: the multiplication records the Gram matrix of $\langle\cdot,\cdot\rangle_{*}$ in the basis and nothing else. In particular the block is not the general plain sesquilinear product itself: the latter has the non-diagonal table $e_\mu e_\nu^{*} = \varepsilon_\nu\, e_\mu e_\nu$ of *Introduction to the General Plain Sesqualgebra*.

## The Square and Its Polarisation

**Proposition (the square is the form at the two equal arguments).** For every $\tilde Q$,

$$
\tilde Q \star \tilde Q = \langle\tilde Q,\tilde Q\rangle_{*}\, e_t = \Bigl(\lvert Q_t\rvert^{2} + \sum_{k=1}^{3} \lvert Q_k\rvert^{2}\Bigr) e_t = \Bigl(\sum_{\mu\in\{t,x,y,z\}} \lvert Q_\mu\rvert^{2}\Bigr) e_t ,
$$

a **central** element whose coefficient is real and non-negative, and strictly positive for $\tilde Q \neq 0$.

*Proof.* Put $\tilde Q_1 = \tilde Q_2$ in the central form. The coefficient is $\sum_\mu \lvert Q_{2,\mu}\rvert^{2}$, a sum of squares of moduli of complex numbers.

**Proposition (the polarisation recovers the real part alone).** For all $\tilde Q_1, \tilde Q_2$,

$$
\tfrac12\bigl((\tilde Q_1 + \tilde Q_2)\star(\tilde Q_1 + \tilde Q_2) - \tilde Q_1\star\tilde Q_1 - \tilde Q_2\star\tilde Q_2\bigr) = \mathrm{Re}\,\langle\tilde Q_1,\tilde Q_2\rangle_{*}\, e_t ,
$$

so the squared map $\tilde Q \mapsto \tilde Q\star\tilde Q$ determines only the real part $\mathrm{Re}\,H$ of the form, not the form $\langle\cdot,\cdot\rangle_{*}$ itself; the imaginary part is recovered from the sesquilinear structure and not from the square. This is the exact opposite of the symmetric quaternionic block, whose polarisation recovers the whole bilinear form.

*Proof.* Expand $\langle\tilde Q_1+\tilde Q_2,\tilde Q_1+\tilde Q_2\rangle_{*} = \langle\tilde Q_1,\tilde Q_1\rangle_{*} + \langle\tilde Q_1,\tilde Q_2\rangle_{*} + \langle\tilde Q_2,\tilde Q_1\rangle_{*} + \langle\tilde Q_2,\tilde Q_2\rangle_{*}$ and use $\langle\tilde Q_2,\tilde Q_1\rangle_{*} = \overline{\langle\tilde Q_1,\tilde Q_2\rangle_{*}}$, so that the middle two terms are $\langle\tilde Q_1,\tilde Q_2\rangle_{*} + \overline{\langle\tilde Q_1,\tilde Q_2\rangle_{*}} = 2\,\mathrm{Re}\,\langle\tilde Q_1,\tilde Q_2\rangle_{*}$.

**Remark (a quadratic form of the sesquilinear kind).** The map $\tilde Q \mapsto \langle\tilde Q,\tilde Q\rangle_{*}e_t$ is a genuine quadratic form on the real space $\mathbb{B} \cong \mathbb{R}^{8}$, of signature $(8,0)$ and null set $\{0\}$ (*The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*). The block reads it as a square, and the square is the diagonal of the multiplication.

## Conjugate-Commutativity and the Absence of a Unit

**Theorem (the conjugate-commutative law).** For all $\tilde Q_1, \tilde Q_2$,

$$
\tilde Q_1 \star \tilde Q_2 = \overline{\tilde Q_2 \star \tilde Q_1} ,
$$

the bar acting on the central value; the law is read on the coefficient of $e_t$.

*Proof.* $\langle\tilde Q_2,\tilde Q_1\rangle_{*} = \sum_\mu Q_{2,\mu} \overline{Q_{1,\mu}} = \overline{\sum_\mu Q_{1,\mu} \overline{Q_{2,\mu}}} = \overline{\langle\tilde Q_1,\tilde Q_2\rangle_{*}}$; multiply by $e_t$ and conjugate.

**Proposition (the two involutions: one automorphism, one reversal).** The natural conjugation preserves the product and the Hermitian conjugation reverses it up to the coefficientwise conjugate:

$$
\tilde Q_1^{\natural} \star \tilde Q_2^{\natural} = \tilde Q_1 \star \tilde Q_2 , \qquad \tilde Q_1^{*} \star \tilde Q_2^{*} = \overline{\tilde Q_1 \star \tilde Q_2} = \tilde Q_2 \star \tilde Q_1 .
$$

*Proof.* On the coordinates, $(\tilde Q_1^{\natural})_\mu = \varepsilon_\mu Q_{1,\mu}$ and $(\tilde Q_1^{*})_\mu = \varepsilon_\mu\overline{Q_{1,\mu}}$ with $\varepsilon = (1,-1,-1,-1)$. Hence $\langle\tilde Q_1^{\natural},\tilde Q_2^{\natural}\rangle_{*} = \sum_\mu \varepsilon_\mu Q_{1,\mu}\,\overline{\varepsilon_\mu Q_{2,\mu}} = \sum_\mu \varepsilon_\mu^{2} Q_{1,\mu} \overline{Q_{2,\mu}} = \langle\tilde Q_1,\tilde Q_2\rangle_{*}$, since $\varepsilon_\mu^{2} = 1$; and $\langle\tilde Q_1^{*},\tilde Q_2^{*}\rangle_{*} = \sum_\mu \varepsilon_\mu \overline{Q_{1,\mu}}\,\overline{\varepsilon_\mu\overline{Q_{2,\mu}}} = \sum_\mu \varepsilon_\mu^{2} \overline{Q_{1,\mu}} Q_{2,\mu} = \overline{\langle\tilde Q_1,\tilde Q_2\rangle_{*}}$. The second equality of the display is the conjugate-commutative law.

**Remark (why the two differ).** The natural conjugation is $\mathbb{C}$-linear and acts as an automorphism of the block; the Hermitian conjugation carries the conjugate-linear slot into the linear one, so it reverses the two arguments and conjugates the central value. In the plain bilinear product the roles are the other way round: there the natural conjugation alone is the antiautomorphism, and the product carries no conjugation of the base field.

**Theorem (no unit, on either side).** For every $\tilde Q$,

$$
\tilde Q \star e_t = Q_t\, e_t , \qquad e_t \star \tilde Q = \overline{Q_t}\, e_t .
$$

Hence $e_t$ is **neither a right unit nor a left unit** of the block: the equation $\tilde Q \star e_t = \tilde Q$ forces $\vec Q = 0$ and $Q_t$ arbitrary, and the equation $e_t \star \tilde Q = \tilde Q$ forces $\vec Q = 0$ and $Q_t$ real. No other element is a unit either, on either side: a right unit $\tilde E$ would have $\vec e_x \star \tilde E = \vec e_x$, a left unit $\tilde E$ would have $\tilde E \star \vec e_x = \vec e_x$, and every value of the product is central while $\vec e_x$ is not.

*Proof.* $\langle\tilde Q,e_t\rangle_{*} = Q_t\overline{1} = Q_t$ and $\langle e_t,\tilde Q\rangle_{*} = \overline{Q_t}$; multiply by $e_t$. For the general statement, $\vec e_x \star \tilde E = \langle \vec e_x,\tilde E\rangle_{*}e_t$ and $\tilde E \star \vec e_x = \langle\tilde E,\vec e_x\rangle_{*}e_t$ are central, while $\vec e_x\notin\mathbb{C}e_t$, so neither can equal $\vec e_x$. The two scalar rules are the failure, since the central image can carry only the scalar part of the element and not its vector part.

**Remark (the comparison with the two sibling rows).** The law is **commutative** in the symmetric plain block, $\tilde Q_1\bullet\tilde Q_2 = \tilde Q_2\bullet\tilde Q_1$, which is $\mathbb{C}$-bilinear and carries the two-sided unit $e_t$ (*Introduction to the Symmetric Plain Algebra*); it is **commutative** in the symmetric quaternionic block, whose pairing $N$ is $\mathbb{C}$-bilinear and symmetric (*Introduction to the Symmetric Quaternionic Algebra*); and it is **conjugate-commutative** here, the conjugation being exactly what the second slot of the sesquilinear pairing carries. The law therefore separates this block from the two bilinear ones, and it does not separate the two bilinear blocks from one another; those two are separated by the unit: commutative with a unit for the plain block, commutative without a unit for the quaternionic one, conjugate-commutative without a unit here. The symmetric plain block alone has a unit, and the two central blocks have none for the same reason: the values are central, and the identity of a central-valued product cannot reproduce a vector part.

## The Failure of the Jordan Identity

**Theorem (the Jordan identity fails).** The operation $\star$ does not satisfy the Jordan identity, in the associator form

$$
(x^{2} \star y) \star x = x^{2} \star (y \star x) ,
$$

and it fails already at $x = y = \vec e_x$, where the two sides are $0$ and $e_t$:

$$
(x^{2} \star x) \star x = 0 , \qquad x^{2} \star (x \star x) = e_t .
$$

*Proof.* $\vec e_x \star \vec e_x = \langle \vec e_x,\vec e_x\rangle_{*}e_t = e_t$, so $x^{2} = e_t$. Then $(x^{2} \star x) \star x = (e_t \star \vec e_x)\star \vec e_x = (\langle e_t,\vec e_x\rangle_{*}e_t)\star \vec e_x = 0$, because $\langle e_t,\vec e_x\rangle_{*} = 0$; and $x^{2} \star (x \star x) = e_t \star e_t = \langle e_t,e_t\rangle_{*}e_t = e_t$.

**Remark (why it fails here and holds in the symmetric plain block).** The symmetric plain block is a **special Jordan algebra**: its product $\tilde Q_1 \bullet \tilde Q_2 = \tfrac12(\tilde Q_1\tilde Q_2 + \tilde Q_2\tilde Q_1)$ is the symmetrisation of an associative product, and every such symmetrisation satisfies the Jordan identity (*Introduction to the Symmetric Plain Algebra*). The block of this article is a symmetrisation of the **sesquilinear** product $\tilde Q_1\tilde Q_2^{*}$, whose second slot carries a conjugation; the symmetrisation is balanced by the natural conjugation and not by the transposition, and the resulting operation is not the Jordan product of any associative algebra. The failure is the structural mark of the sesqualgebra row: in the twelve, the symmetric part of the plain product alone is a Jordan product, and the symmetric parts of the three other products fail (*The 12 Products of the Biquaternioid Complex Space*).

## The Reconstruction and the Placement among the Twelve

**Proposition (the reconstruction).** The general plain sesquilinear product splits as

$$
\tilde Q_1\tilde Q_2^{*} = \tilde Q_1 \star \tilde Q_2 + \tilde Q_1 \diamond \tilde Q_2 ,
$$

with $\tilde Q_1\star\tilde Q_2 = \mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})e_t$ the symmetric part of this block and $\tilde Q_1\diamond\tilde Q_2 = \mathrm{Vect}(\tilde Q_1\tilde Q_2^{*})$ the antisymmetric part, the block *Biquaternions as an Antisymmetric Plain Sesqualgebra (APS) over $\mathbb{C}$*. In terms of the twelve, $\mathrm{GPS} = \mathrm{SPS} + \mathrm{APS}$.

*Proof.* Every element is the sum of its scalar part and its vector part; the symmetric half is the scalar part by the proposition above, and the difference is the vector part. The identity is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product* applied to the plain sesquilinear product.

**Proposition (the placement).** Among the twelve operations the block is the symmetric part of the third product, and it is determined by exactly four of its properties:

- its class is **sesquilinear** over $(\mathbb{C},\bar{\cdot}\,)$, not $\mathbb{C}$-bilinear, so it is one of the six operations of the two sesqualgebra rows;
- its image is the **centre** $\mathbb{C}_{\mathbb{B}}$, one of the two central operations of the twelve, the other being the symmetric quaternionic block;
- its law is **conjugate-commutative**, not commutative, and it has **no unit**;
- it **fails** the Jordan identity, so it is not a classical nonassociative product.

On the real part of the space the block coincides with the symmetric quaternionic block, $\mathrm{SQA} = \mathrm{SPS}$, because on real elements $H = N$, the quaternion form; on the complex space the two are distinct.

*Proof.* The class is the second scalar rule of the proposition above; the image is the central form; the law and the failure are the two theorems above; the coincidence on the real part is the bridge of *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra*, $\langle\tilde Q_1,\tilde Q_2\rangle_{*} = \langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$, the quaternion form, for real $\tilde Q_1,\tilde Q_2$. The distinctness off the real subspace is exhibited by $\tilde Q_1 = \tilde Q_2 = ie_t$, where $H = 1$ and $N = -1$.

## Worked Examples

**The basis.** The products $e_\mu \star e_\nu = \delta_{\mu\nu}e_t$ are the sixteen entries of the table; in particular $\vec e_x\star \vec e_y = 0$, while the general plain sesquilinear product has $\vec e_x \vec e_y^{*} = -\vec e_z$. The block forgets the vector structure of the product entirely and keeps the pairing.

**A Hermitian element and its square.** Let $\tilde Q_2 = e_t + i\vec e_z$, of diagonal $\langle\tilde Q_2,\tilde Q_2\rangle_{*} = 2$. Then $\tilde Q_2 \star \tilde Q_2 = 2e_t$, and the polarisation with $\tilde Q_1 = e_t$ gives $\mathrm{Re}\,\langle e_t,e_t+i\vec e_z\rangle_{*}e_t = e_t$, the real part of $\langle e_t,\tilde Q_2\rangle_{*} = 1$.

**A non-real pairing.** Let $\tilde Q_1 = e_t$ and $\tilde Q_2 = ie_t$. Then $\tilde Q_1 \star \tilde Q_2 = \langle e_t,ie_t\rangle_{*}e_t = \overline{i}e_t = -ie_t$, while the conjugate-commutative law gives $\tilde Q_2 \star \tilde Q_1 = \langle ie_t,e_t\rangle_{*}e_t = ie_t$, and the two are conjugate coefficients. The example exhibits the conjugate-linearity of the second slot and the law at once.

**The Jordan witness.** With $x = y = \vec e_x$ one has $x^{2} = e_t$, $(x^{2}\star x)\star x = 0$ and $x^{2}\star(x\star x) = e_t$: the two sides differ by the idempotent.

## The Interpretation in the Physics Band

Every value of the block is central and its coefficient is the form $\langle\cdot,\cdot\rangle_{*}$, so the block is the **probability form** written as a multiplication: its square $\tilde Q\star\tilde Q = \bigl(\sum_\mu\lvert Q_\mu\rvert^{2}\bigr)e_t$ is a positive central number vanishing only at the origin, and its vanishing products $e_\mu\star e_\nu = 0$ for $\mu\neq\nu$ are orthogonal basis states. The polarisation recovers the real part alone, so the square carries the modulus of a value and the sesquilinear structure carries its phase.

The readings are these, and each belongs to the physics article named; this article stops at the algebra. The positivity of the form, its cone and the weight of an element are read as the probability of a state and the cone of effects in *The Biquaternioid Symmetric Plain Sesqualgebra (SPS) over $\mathbb{C}$*; the central value read as the modulus of an amplitude, with the vector part the central operation discards read as its argument, is *The Biquaternioid Symmetric Plain Sesqualgebra (SPS) over $\mathbb{C}$*.

## Summary

The symmetric plain sesqualgebra is the operation $\tilde Q_1\star\tilde Q_2 = \tfrac12(\tilde Q_1\tilde Q_2^{*} + (\tilde Q_1\tilde Q_2^{*})^{\natural}) = \mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})e_t = \langle\tilde Q_1,\tilde Q_2\rangle_{*}e_t$ on the biquaternion space: the Hermitian form of the corpus read as a multiplication. Every value is central, so the block is a rank-one form and not a multiplication with a vector part; its class is sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$, $\mathbb{C}$-linear in the first argument and conjugate-linear in the second. Its sixteen basis products are $e_\mu\star e_\nu = \delta_{\mu\nu}e_t$, its square is $\tilde Q_2\star\tilde Q_2 = (\sum_\mu\lvert Q_{2,\mu}\rvert^{2})e_t$ and its polarisation recovers only $\mathrm{Re}\,H$. It is **conjugate-commutative**, $\tilde Q_1\star\tilde Q_2 = \overline{\tilde Q_2\star\tilde Q_1}$; the natural conjugation acts as an automorphism, $\tilde Q_1^{\natural}\star\tilde Q_2^{\natural} = \tilde Q_1\star\tilde Q_2$, and the Hermitian conjugation as the reversal, $\tilde Q_1^{*}\star\tilde Q_2^{*} = \overline{\tilde Q_1\star\tilde Q_2} = \tilde Q_2\star\tilde Q_1$. It has **no unit** on either side, since $\tilde Q_2\star e_t = Q_{2t}e_t$ and $e_t\star\tilde Q_2 = \overline{Q_{2t}}e_t$. It **fails the Jordan identity**, witnessed by $x = y = \vec e_x$ with the two sides $0$ and $e_t$, because it is the symmetrisation of a sesquilinear product and not that of an associative one; the symmetric plain block, alone among the twelve, is the Jordan product. The block is the scalar part of the general plain sesquilinear product, $\mathrm{GPS} = \mathrm{SPS} + \mathrm{APS}$, it is one of the two central operations of the twelve, and off the real subspace it is distinct from the symmetric quaternionic block, with which it coincides on the real part alone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra; basis $e_t,\vec e_x,\vec e_y,\vec e_z$, $e_t = 1$, $\vec e_k^{2} = -e_t$ |
| ${}^{\natural}$, $\overline{\cdot}$, ${}^{*} = \overline{\cdot}\circ{}^{\natural}$ | natural conjugation, coefficientwise conjugation, Hermitian conjugation |
| $\tilde Q_1 \star \tilde Q_2 = \tfrac12\bigl(\tilde Q_1\tilde Q_2^{*} + (\tilde Q_1\tilde Q_2^{*})^{\natural}\bigr)$ | the multiplication of the block; the symmetric part of the plain sesquilinear product |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*} = \sum_\mu Q_{1,\mu}\overline{Q_{2,\mu}} = Q_{1t}\overline{Q_{2t}} + (\vec Q_1,\overline{\vec Q_2})$ | the Hermitian form, read as the coefficient of $e_t$ |
| $\tilde Q_1\star\tilde Q_2 = \langle\tilde Q_1,\tilde Q_2\rangle_{*}e_t$ | the value is central; image $\mathbb{C}_{\mathbb{B}}$ |
| $e_\mu\star e_\nu = \delta_{\mu\nu}e_t$ | the sixteen products of the basis |
| $\tilde Q\star\tilde Q = \bigl(\sum_\mu\lvert Q_\mu\rvert^{2}\bigr)e_t$ | the square; real and positive off the origin |
| $\tilde Q_1\star\tilde Q_2 = \overline{\tilde Q_2\star\tilde Q_1}$ | the conjugate-commutative law |
| $\tilde Q_1^{\natural}\star\tilde Q_2^{\natural} = \tilde Q_1\star\tilde Q_2$, $\tilde Q_1^{*}\star\tilde Q_2^{*} = \overline{\tilde Q_1\star\tilde Q_2}$ | the two involutions: automorphism and reversal |
| $\tilde Q\star e_t = Q_te_t$, $e_t\star\tilde Q = \overline{Q_t}e_t$ | the absence of a unit on either side |
| $(x^{2}\star x)\star x = 0$, $x^{2}\star(x\star x) = e_t$ at $x = \vec e_x$ | the failure of the Jordan identity |
| $\mathrm{GPS} = \mathrm{SPS} + \mathrm{APS}$ | the reconstruction of the product from its two parts |

## Further Reading

- *Introduction to the General Plain Sesqualgebra* (`articles_maths/introduction-to-the-general-plain-sesqualgebra.md`), for the product that is split here and its two scalar rules.
- *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product* (`articles_maths/the-symmetric-and-antisymmetric-parts-of-a-sesqualgebra-product.md`), for the general construction of the two parts and the obstruction that keeps them in the class.
- *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternioid-c-space.md`), for the Hermitian form $\langle\cdot,\cdot\rangle_{*}$, its positivity and its Gram matrix.
- *Positivity and the Hermitian Cone of the Biquaternioid Algebra with Hermitian Adjoint* (`articles_maths/positivity-and-the-hermitian-cone-of-the-biquaternioid-algebra-with-hermitian-adjoint.md`), for the cone that the diagonal of the block generates.
- *The 12 Products of the Biquaternioid Complex Space* (`articles_maths/the-12-products-of-the-biquaternioid-complex-space.md`), for the row table and the placement of the block among the twelve.
- *Introduction to the Symmetric Plain Algebra* (`articles_maths/introduction-to-the-symmetric-plain-algebra.md`), the commutative unital sibling, the one Jordan product of the twelve.
- *Introduction to the Symmetric Quaternionic Algebra* (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra.md`), the bilinear central sibling, with which the block coincides on the real part.
- *The Conjugate-Commutative Law and the Idempotents of the Symmetric Plain Sesqualgebra* (`articles_maths/the-conjugate-commutative-law-and-the-idempotents-of-the-symmetric-plain-sesqualgebra.md`), the companion article, for the two readings of the law and its comparison with the sibling blocks.
- *Norm and Invertibility in the Symmetric Plain Sesqualgebra* (`articles_maths/norm-and-invertibility-in-the-symmetric-plain-sesqualgebra.md`), for the norm of the block, the absence of a unit and the square map.
- *Zero Divisors in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/zero-divisors-in-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the punctured-space zero-divisor set and the annihilators.
- *Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/square-roots-of-one-and-the-idempotents-in-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the root set of $+1$, the two central idempotents and the halving map from the roots of one.
- *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/square-roots-of-zero-and-the-nilpotents-in-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the emptiness of the root set of $0$ and the index-three nilpotents of the vector subspace.
- *Square Roots of a General Element in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/square-roots-of-a-general-element-in-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the root sets and the square-root classification.
- *The Specificities of the Symmetric Plain Sesqualgebra* (`articles_maths/the-specificities-of-the-symmetric-plain-sesqualgebra.md`), for the Hermitian criterion that isolates the block among the twelve.
