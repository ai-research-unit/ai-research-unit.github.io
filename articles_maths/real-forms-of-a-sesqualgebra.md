# __Real Forms of a Sesqualgebra__

## Introduction

The datum of a sesqualgebra is a pair $(R,\varsigma)$ and not a ring alone, and the involution $\varsigma$ is a second piece of structure on the scalars beside the addition and the multiplication. It therefore has its own fixed ring, $R^{\varsigma}$, and beside the datum involution ${}^{*}$, which is an anti-automorphism of $A$, the object carries the order-two $\varsigma$-semilinear **automorphisms** $\alpha$ that cut its real forms. This article reads the two involutions together: the fixed ring of the base, the fixed subalgebra of an order-two automorphism, the descent of the sesquilinear structure to the fixed ring, and the real forms of a complex sesqualgebra that the descent produces.

There are two features and they point in opposite directions. The base involution has few fixed scalars and the fixed ring $R^{\varsigma}$ is generally much smaller than $R$ — for the conjugation of $\mathbb{C}$ it is $\mathbb{R}$ — so the descent of the scalars is a genuine restriction. On the fixed ring, however, the twist is gone: $\varsigma$ restricts to the identity of $R^{\varsigma}$, so a sesquilinear product read over $R^{\varsigma}$ is bilinear. This is the same collapse as in *Sesqualgebras*, seen from the other side: the sesquilinear layer contains the bilinear one as the case of the trivial involution, and the fixed ring of a nontrivial involution is exactly a place where the trivial case appears inside the nontrivial one. The four subobjects the two involutions cut, the descent, and the worked cases $\mathbb{C}$, $\mathbb{H}$ and $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ are the content.

The setting is that of *Sesqualgebras*: $R$ is a commutative ring with $1$, $\varsigma$ is an involution of $R$, $A$ is a sesqualgebra over $(R,\varsigma)$ with product $R$-linear in the first variable and $\varsigma$-semilinear in the second, carrying a $\varsigma$-semilinear involution ${}^{*}$ of order two. The fixed and anti-fixed elements of the datum are *Hermitian and Skew-Hermitian Elements*; the order-two $\varsigma$-semilinear **anti**-automorphisms, which are the involutions of $A$ in the sense of the corpus, are *The Involutions of a Sesqualgebra*, and the order-two semilinear maps of both kinds are *Anti-Automorphisms Twisted by the Base Involution*; the subalgebras stable under an involution are *Subalgebras and the Involution*; and the bilinear counterpart of the whole construction, where the descent map is a semilinear automorphism called a conjugation, is *Real Forms and the Descent of an Algebra*.

---

## The Fixed Ring of the Base Involution

### The Two Parts of the Ring

**Definition.** The **fixed ring** of the base involution is $R^{\varsigma}=\{\lambda\in R : \varsigma(\lambda)=\lambda\}$, and the **anti-fixed part** is $R^{-}=\{\lambda\in R : \varsigma(\lambda)=-\lambda\}$.

**Theorem.** The fixed ring $R^{\varsigma}$ is a subring of $R$ containing $1$; the anti-fixed part $R^{-}$ is an $R^{\varsigma}$-submodule; and when $2$ is invertible in $R$ the ring decomposes as

$$
R = R^{\varsigma}\oplus R^{-}, \qquad \lambda = \tfrac12\bigl(\lambda+\varsigma(\lambda)\bigr) + \tfrac12\bigl(\lambda-\varsigma(\lambda)\bigr).
$$

*Proof.* Sums and products of fixed elements are fixed because $\varsigma$ is a ring homomorphism, and $\varsigma(1)=1$. For $\lambda\in R^{-}$ and $\mu\in R^{\varsigma}$ one has $\varsigma(\mu\lambda)=\varsigma(\mu)\varsigma(\lambda)=\mu(-\lambda)=-\mu\lambda$, so $R^{-}$ is an $R^{\varsigma}$-submodule. The displayed decomposition is the standard one of the two projections $\tfrac12(\mathrm{id}\pm\varsigma)$, and it is direct because a scalar that is both fixed and anti-fixed satisfies $\lambda=-\lambda$, hence $2\lambda=0$ and $\lambda=0$ when $2$ is invertible. $\square$

**Remark.** The two parts are the fixed and the anti-fixed elements of the base, and they are the base-level analogue of the Hermitian and skew-Hermitian elements of *Hermitian and Skew-Hermitian Elements*. The difference is that only the fixed part is a subring: it is closed under the product because $\varsigma$ is multiplicative, while a product of two anti-fixed scalars is fixed, so $R^{-}$ is a module and not a ring.

### The Scalars of the Object

**Proposition.** Every sesqualgebra over $(R,\varsigma)$ is a module over the fixed ring $R^{\varsigma}$, and for $\mu\in R^{\varsigma}$ the two scalar rules of the product read the same:

$$
(\mu x)y = \mu(xy) = x(\mu y) .
$$

*Proof.* The restriction of the $R$-action to $R^{\varsigma}$ is an action because $R^{\varsigma}$ is a subring. The first equality is the first scalar rule and the second is the second rule with $\varsigma(\mu)=\mu$. $\square$

**Corollary.** Read over $R^{\varsigma}$ alone, the product of $A$ is $R^{\varsigma}$-bilinear. The $\varsigma$-twist is invisible over the fixed ring, and $A$ is an $R^{\varsigma}$-algebra in the ordinary sense together with its involution ${}^{*}$; whether that algebra is sesquilinear or bilinear is a question about the scalars one admits, and over $R^{\varsigma}$ it is bilinear.

**Remark.** This is the first appearance of the collapse inside the theory and not at the boundary of it. A sesqualgebra is not a sesquilinear object over every ring over which it can be read: over the fixed ring of its own base involution the twist is trivial, and the object reverts to the bilinear layer. The distinction between the two layers is therefore a distinction of the datum and not of the module, and the fixed ring is where the datum forgets its involution.

## The Fixed Subalgebra of an Order-Two Automorphism

### Automorphisms and Anti-Automorphisms

Let $\alpha$ be a map of $A$ to itself. Two kinds of order-two map occur, and they give different fixed sets, so the distinction is made first.

**Definition.** A **$\varsigma$-semilinear automorphism** of $A$ is an additive bijection $\alpha$ with $\alpha(\lambda x)=\varsigma(\lambda)\alpha(x)$ and $\alpha(xy)=\alpha(x)\alpha(y)$; a **$\varsigma$-semilinear anti-automorphism** is an additive bijection with $\alpha(\lambda x)=\varsigma(\lambda)\alpha(x)$ and $\alpha(xy)=\alpha(y)\alpha(x)$. The datum involution ${}^{*}$ is of the second kind, and its fixed elements are the Hermitian ones. The word **involution** without qualification means an element of $\operatorname{Inv}(A)$, that is an anti-automorphism of order two, as in *The Involutions of a Sesqualgebra*; the descent map of this article is the other kind, an automorphism, and its fixed set $A^{\alpha}$ is a subalgebra while the fixed set of an involution is the subspace $H(A)$ of Hermitian elements.

**Remark.** For an order-two semilinear map $\alpha$ the first kind is the analogue of complex conjugation on $\mathbb{C}$ and the second is the analogue of the conjugate transpose on $M_n(\mathbb{C})$, and the difference is what happens on products. The fixed set of the second kind is not closed under the product unless the elements commute, because $\alpha(xy)=\alpha(y)\alpha(x)$ and $\alpha(x)=x$, $\alpha(y)=y$ give $\alpha(xy)=yx$; the fixed set of the first kind is closed, and it is the one that produces subalgebras. The twisted maps of both kinds are catalogued in *Anti-Automorphisms Twisted by the Base Involution*.

### The Fixed and Anti-Fixed Sets

**Definition.** For a $\varsigma$-semilinear automorphism $\alpha$ of order two, the **fixed subalgebra** and the **anti-fixed part** are

$$
A^{\alpha}=\{x\in A : \alpha(x)=x\}, \qquad A^{-\alpha}=\{x\in A : \alpha(x)=-x\}.
$$

**Theorem.** The fixed set $A^{\alpha}$ is a subalgebra of $A$ and an $R^{\varsigma}$-submodule; the anti-fixed part $A^{-\alpha}$ is an $R^{\varsigma}$-submodule; and when $2$ is invertible in $R$ the module decomposes as $A=A^{\alpha}\oplus A^{-\alpha}$ through $\tfrac12(x\pm\alpha(x))$.

*Proof.* For $x,y\in A^{\alpha}$ the multiplicativity gives $\alpha(xy)=xy$ and the semilinearity gives $\alpha(\mu x)=\varsigma(\mu)x=\mu x$ for $\mu\in R^{\varsigma}$, so $A^{\alpha}$ is closed under the product and under the scalars of the fixed ring; the anti-fixed part is closed under the same scalars and under addition. The decomposition is $\tfrac12(\mathrm{id}\pm\alpha)$ and is direct because an element of both parts satisfies $x=-x$. $\square$

**Corollary.** The fixed subalgebra $A^{\alpha}$ is a sesqualgebra over the datum $(R^{\varsigma},\varsigma|_{R^{\varsigma}})=(R^{\varsigma},\mathrm{id})$, that is an ordinary $R^{\varsigma}$-algebra; its inclusion in $A$ is a morphism over $R^{\varsigma}$; and the datum involution ${}^{*}$ restricts to an $R^{\varsigma}$-linear involution of $A^{\alpha}$ when $\alpha$ commutes with ${}^{*}$, ${}^{*}\alpha=\alpha{}^{*}$.

*Proof.* The first two statements are the theorem with the corollary above; the restriction of ${}^{*}$ is additive and of order two, and it is $R^{\varsigma}$-linear because $\varsigma$ is the identity on $R^{\varsigma}$, so it is an involution of the ordinary algebra $A^{\alpha}$. Its restriction to $A^{\alpha}$ is well defined when $\alpha(x^{*})=x^{*}$ for $x\in A^{\alpha}$, which holds as soon as the two involutions commute, $\alpha{}^{*}={}^{*}\alpha$; whether commutation is also necessary is not established here. $\square$

## The Descent of the Sesquilinear Structure

### The Descent Theorem

**Theorem (the descent).** Let $\alpha$ be a $\varsigma$-semilinear automorphism of $A$ of order two. The multiplication of $A$ restricts to $A^{\alpha}$, the restricted product is $R^{\varsigma}$-bilinear, and the multiplication map

$$
\mu : A^{\alpha}\otimes_{R^{\varsigma}} R\longrightarrow A, \qquad \mu(x\otimes\lambda) = \lambda x,
$$

is a homomorphism of $R^{\varsigma}$-algebras which is also $R$-linear; and it is compatible with the involutions when the tensor product carries $x\otimes\lambda\mapsto x^{*}\otimes\varsigma(\lambda)$. It is an isomorphism in each of the worked cases below.

*Proof.* The restriction of the product to $A^{\alpha}$ is closed by the theorem above, and it is $R^{\varsigma}$-bilinear because both scalars rules coincide over the fixed ring. For $\mu$: the assignment $(x,\lambda)\mapsto\lambda x$ is $R^{\varsigma}$-bilinear, so it induces $\mu$; multiplicativity is $\mu\bigl((x\otimes\lambda)(y\otimes\eta)\bigr)=\mu(xy\otimes\lambda\eta)=\lambda\eta\,xy=(\lambda x)(\eta y)=\mu(x\otimes\lambda)\mu(y\otimes\eta)$, and $R$-linearity is $\mu(x\otimes r\lambda)=r\lambda x=r\mu(x\otimes\lambda)$. $\square$

**Remark.** The map $\mu$ is the formal statement that the object is recovered from its fixed subalgebra by extension of scalars, and it is the shadow of the Galois-type descent of *Real Forms and the Descent of an Algebra*. One caution belongs with it in this generality: $\mu$ need not be an isomorphism for an arbitrary base, and what fails is the generation of the anti-fixed part by the fixed part, $A^{-\alpha}=A^{\alpha}R^{-}$. The smallest witness is the base $R=\mathbb{C}$ with $\varsigma=\mathrm{id}$, where $R^{\varsigma}=\mathbb{C}$, the object $A=\mathbb{C}^{2}$ with the coordinate exchange $\alpha(x,y)=(y,x)$ of order two: then $A^{\alpha}$ is the diagonal, $\mu$ is injective, and its image is the diagonal in $\mathbb{C}^{2}$, so $\mu$ is not onto. The isomorphism is therefore asserted in the worked cases and not in general. And the map is a statement about the algebra and the involution, not about the sesquilinear structure: over $R^{\varsigma}$ that structure is bilinear, so what descends is an ordinary algebra with an involution. The passage from the sesquilinear layer to the bilinear one that *Sesqualgebras* records at $\varsigma=\mathrm{id}$ is here performed by the fixed ring, on the subalgebra and not on the whole object.

### The Two Involutions Together

The datum involution ${}^{*}$ and the descent automorphism $\alpha$ are two order-two maps of $A$, and when they commute the four maps they generate are all of order two.

**Proposition.** Suppose $\alpha$ commutes with ${}^{*}$. Then the composite $\alpha{}^{*}$ is a $\varsigma$-semilinear map of order two, the four maps $\mathrm{id}$, ${}^{*}$, $\alpha$, $\alpha{}^{*}$ are commuting involutions, and their fixed subspaces are $A$, the Hermitian elements $H(A)$, the fixed subalgebra $A^{\alpha}$ and the fixed subspace of $\alpha{}^{*}$; the involution ${}^{*}$ carries $A^{\alpha}$ to itself and $\alpha$ carries $H(A)$ to itself.

*Proof.* $(\alpha{}^{*})^{2}=\alpha{}^{*}\alpha{}^{*}=\alpha^{2}{}^{*2}=\mathrm{id}$ by the commuting, and the semilinearity is the composition of two semilinear maps with $\varsigma^{2}=\mathrm{id}$. The involution ${}^{*}$ carries fixed elements of $\alpha$ to fixed elements of $\alpha$ when $\alpha{}^{*}={}^{*}\alpha$, so $\alpha$ restricts to $H(A)$. $\square$

## The Two Involutions and the Four Subobjects

### The Table

The base involution acts on $R$ and the order-two automorphism on $A$, and each cuts a fixed part and an anti-fixed part. The four subobjects are the following.

| the involution | the fixed part | the anti-fixed part | the kind of object |
|---|---|---|---|
| $\varsigma$ on $R$ | $R^{\varsigma}$, a subring containing $1$ | $R^{-}$, an $R^{\varsigma}$-submodule | the scalars |
| $\alpha$ on $A$ | $A^{\alpha}$, an $R^{\varsigma}$-subalgebra | $A^{-\alpha}$, an $R^{\varsigma}$-submodule | the algebra |

**Theorem.** The four subobjects are as tabulated; each fixed part is closed under its own product, each anti-fixed part is a module over the corresponding fixed part, and both decompositions are direct when $2$ is invertible. The fixed ring $R^{\varsigma}$ acts on all four, and it is the only one of the four that is a ring.

*Proof.* The statements about $R^{\varsigma}$, $R^{-}$ are the first theorem of the article and those about $A^{\alpha}$, $A^{-\alpha}$ are the second, and the action of $R^{\varsigma}$ on $A$ and on its two parts is the proposition on the scalars of the object. $\square$

**Remark.** The four are not independent: $A^{\alpha}$ and $A^{-\alpha}$ are modules over $R^{\varsigma}$ and not over $R$, while the scalars of $R^{-}$ lie outside $R^{\varsigma}$ and act on $A$ through the $R$-action by scalars the involution does not fix. The asymmetry is the asymmetry of the two involutions: $\varsigma$ is an involution of the scalars and $\alpha$ is an involution of the object, and only the first changes the ring over which the object is read. This is why the descent of the sesquilinear structure is a statement about $R^{\varsigma}$ and $A^{\alpha}$ jointly and cannot be made with either involution alone.

## Real Forms of a Complex Sesqualgebra

### The Definition

Let $R=\mathbb{C}$ with $\varsigma$ the conjugation, so that $R^{\varsigma}=\mathbb{R}$ and $R^{-}=i\mathbb{R}$. The object $A$ is a complex sesqualgebra.

**Definition.** A **real form** of $A$ is the fixed subalgebra $A^{\alpha}$ of a $\varsigma$-semilinear automorphism $\alpha$ of $A$ of order two for which the multiplication map $A^{\alpha}\otimes_{\mathbb{R}}\mathbb{C}\to A$ is an isomorphism; it is then a real algebra whose extension of scalars is $A$, and the isomorphism is the multiplication map of the section above. For $R=\mathbb{C}$ the isomorphism is automatic, by the theorem below, so a real form of a complex sesqualgebra is exactly the fixed subalgebra of an order-two $\varsigma$-semilinear automorphism, which is called a **conjugation** of $A$ in *Real Forms and the Descent of an Algebra*.

**Theorem.** For the conjugation of $\mathbb{C}$ the sesquilinear structure of $A$ descends to the real form: $A^{\alpha}$ is an $\mathbb{R}$-algebra, its product is $\mathbb{R}$-bilinear, the multiplication map $A^{\alpha}\otimes_{\mathbb{R}}\mathbb{C}\to A$ is an isomorphism because $A=A^{\alpha}\oplus iA^{\alpha}$, and the datum involution ${}^{*}$ restricts to an $\mathbb{R}$-linear involution of it when it commutes with $\alpha$. In particular the real form of a complex sesqualgebra is an ordinary real algebra with an involution, and the sesquilinear structure lives on the complex object and not on its real form.

*Proof.* $R^{\varsigma}=\mathbb{R}$ and $\varsigma$ is the identity there, so the corollary on the scalars of the object and the descent theorem apply with $R^{\varsigma}=\mathbb{R}$. For the isomorphism, $\alpha$ is $\mathbb{C}$-antilinear of order two, so every $x$ decomposes as $x=\tfrac12(x+\alpha x)+\tfrac12(x-\alpha x)$ with $\tfrac12(x+\alpha x)\in A^{\alpha}$ and $\tfrac12(x-\alpha x)=iy$ for $y=-\tfrac12 i(x-\alpha x)$, which lies in $A^{\alpha}$ because $\alpha(y)=-\tfrac12\varsigma(i)(\alpha x-x)=y$. The sum $A^{\alpha}+iA^{\alpha}$ is direct because an element of both parts satisfies $x=-x$. Hence $A=A^{\alpha}\oplus iA^{\alpha}$ and the multiplication map is a real-linear isomorphism, since it sends $x\otimes1\mapsto x$ and $x\otimes i\mapsto ix$. $\square$

**Remark.** The word **real form** is used here in the sense of *Real Forms and the Descent of an Algebra*: a real object whose extension of scalars is the given complex one. The two involutions are both needed for the definition — the base involution to say which ring is the real one, the order-two automorphism to say which subalgebra is the form — and neither alone gives a real form. The caution of the next section is that this pair of data is not available for every real algebra.

## Worked Cases

### The Complex Numbers

Let $A=\mathbb{C}$ over $(\mathbb{C},\varsigma)$ with $\varsigma$ the conjugation and with the datum involution ${}^{*}=\varsigma$. The conjugation $\alpha=\varsigma$ is a $\varsigma$-semilinear automorphism of order two, since $\alpha(\lambda z)=\varsigma(\lambda z)=\varsigma(\lambda)\varsigma(z)=\varsigma(\lambda)\alpha(z)$ and $\alpha(zw)=\alpha(z)\alpha(w)$, and its fixed set is

$$
\mathbb{C}^{\alpha}=\mathbb{R},
$$

the real axis. The real form of the sesqualgebra $\mathbb{C}$ is therefore $\mathbb{R}$, its product is $\mathbb{R}$-bilinear, and the datum involution restricts to the identity of $\mathbb{R}$. This is the smallest case of the descent, and it shows that the twist of the sesquilinear field is entirely carried by the imaginary scalars: the fixed ring of the base is exactly the part of $\mathbb{C}$ on which the twist does nothing.

### The Complex Matrices

Let $A=M_n(\mathbb{C})$ with the conjugate transpose and the datum $(\mathbb{C},\varsigma)$ of the conjugation. The entrywise conjugation

$$
\alpha(X)=\bar{X}, \qquad \alpha(X)_{ij}=\varsigma(X_{ij}),
$$

is a $\varsigma$-semilinear automorphism of order two, and its fixed set is

$$
M_n(\mathbb{C})^{\alpha}=M_n(\mathbb{R}),
$$

the real matrices. The real form of $M_n(\mathbb{C})$ with the conjugate transpose is $M_n(\mathbb{R})$ with the transpose, because the conjugate transpose of a real matrix is its transpose; the datum involution restricts, and it is $\mathbb{R}$-linear on the form.

### The Biquaternion Algebra

Let $A=\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ as the complex algebra of *Biquaternions as a General Plain Algebra (GPA) over $\mathbb{C}$*, with the coordinate basis $e_0, e_1, e_2, e_3$ and the two conjugations of that article: the coefficient conjugation $\bar{\cdot}$ and the involution $\natural$ that negates the vector units, with the Hermitian conjugation ${}^{*}=\bar{\cdot}\circ\natural$. The coefficient conjugation

$$
\alpha=\bar{\cdot}, \qquad \alpha(z\,e_\nu)=\varsigma(z)\,e_\nu,
$$

is a $\varsigma$-semilinear automorphism of order two: it conjugates the coefficients and fixes the units, so it multiplies on products. Its fixed set is the quaternion part,

$$
\mathbb{B}^{\bar{\cdot}} = \mathbb{R}e_0\oplus\mathbb{R}e_1\oplus\mathbb{R}e_2\oplus\mathbb{R}e_3 \cong \mathbb{H},
$$

the biquaternions with real coefficients. So the quaternion algebra is a real form of the biquaternion algebra, $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{B}$, which is the statement of *Biquaternions as an Algebra over $\mathbb{R}$*; the datum involution ${}^{*}$ restricts to $\natural$ on the form, and $\natural$ is the quaternion conjugation. The base involution of this case is trivial, because $R=\mathbb{R}$; the twist is not in the base but in the coefficient conjugation of the complex object, and the real form is cut by that conjugation and not by $\varsigma$.

### The Quaternions

The quaternion algebra $\mathbb{H}$ is where the construction stops, and the reason is worth stating. A complex sesqualgebra needs a $\mathbb{C}$-module structure respecting the product, that is an algebra homomorphism $\mathbb{C}\to Z(\mathbb{H})$; but the centre of $\mathbb{H}$ is $\mathbb{R}$,

$$
Z(\mathbb{H}) = \mathbb{R},
$$

so there is no such homomorphism and $\mathbb{H}$ carries no $\mathbb{C}$-sesquilinear structure at all. The quaternion conjugation is $\mathbb{R}$-linear, and read on the complexification $\mathbb{B}$ it extends to the $\mathbb{C}$-linear $\natural$, which is an anti-automorphism and not the anti-linear involution a complex sesquilinear structure requires; the involution that does the work is the composite ${}^{*}=\bar{\cdot}\circ\natural$, and its antilinearity comes from the coefficient conjugation. The caution is therefore that the real form of a complex object is not itself a complex object: $\mathbb{H}$ is a sesqualgebra over $(\mathbb{R},\mathrm{id})$ only, it is the real form of $\mathbb{B}$, and it is not a complex sesqualgebra in any structure.

## Summary

The datum $(R,\varsigma)$ of a sesqualgebra has a **fixed ring** $R^{\varsigma}$ and an anti-fixed part $R^{-}$, they decompose $R=R^{\varsigma}\oplus R^{-}$ when $2$ is invertible, and over the fixed ring the twist disappears: every sesqualgebra is an ordinary $R^{\varsigma}$-algebra with an involution, its product being $R^{\varsigma}$-bilinear. An order-two automorphism $\alpha$ cuts a **fixed subalgebra** $A^{\alpha}$, closed under the product and $R^{\varsigma}$-linear, and an anti-fixed part $A^{-\alpha}$, a module; the fixed subalgebra is the sesqualgebra that descends, the multiplication map $A^{\alpha}\otimes_{R^{\varsigma}}R\to A$ recovering the object by extension of scalars.

The two involutions, $\varsigma$ on the scalars and $\alpha$ on the object, cut the **four subobjects** $R^{\varsigma}$, $R^{-}$, $A^{\alpha}$ and $A^{-\alpha}$, of which the two fixed parts are subalgebras, the two anti-fixed parts are modules, and only $R^{\varsigma}$ is a ring; the fixed ring acts on all four, and this is why the descent needs both involutions and not one. For $R=\mathbb{C}$ with the conjugation the construction gives the **real forms**: the fixed subalgebra of a conjugate-linear automorphism of order two, an ordinary real algebra with an involution whose extension of scalars is the complex object. The worked cases are $\mathbb{C}$ with its real axis, $M_n(\mathbb{C})$ with the conjugate transpose whose real form is $M_n(\mathbb{R})$ with the transpose, and $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with the coefficient conjugation whose real form is $\mathbb{H}$. The caution is $\mathbb{H}$ itself: its centre is $\mathbb{R}$, so it carries no $\mathbb{C}$-sesquilinear structure, and it is the real form of the complex object and not a complex object.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\varsigma$ | the base involution, part of the datum $(R,\varsigma)$ of a sesqualgebra |
| $R^{\varsigma}=\{\lambda:\varsigma(\lambda)=\lambda\}$ | the fixed ring of the base |
| $R^{-}=\{\lambda:\varsigma(\lambda)=-\lambda\}$ | the anti-fixed part of the base |
| $R=R^{\varsigma}\oplus R^{-}$ | the decomposition, when $2$ is invertible |
| $\alpha$ | a $\varsigma$-semilinear order-two automorphism of $A$ |
| $A^{\alpha}=\{x:\alpha(x)=x\}$ | the fixed subalgebra, an $R^{\varsigma}$-algebra |
| $A^{-\alpha}=\{x:\alpha(x)=-x\}$ | the anti-fixed part, an $R^{\varsigma}$-submodule |
| $\mu(x\otimes\lambda)=\lambda x$ | the multiplication map of the descent |
| $A^{\alpha}\otimes_{R^{\varsigma}}R\cong A$ for $R=\mathbb{C}$ | the recovery of the object by extension of scalars |
| $H(A)$ | the Hermitian elements, fixed by the datum involution ${}^{*}$ |
| $\mathbb{C}^{\alpha}=\mathbb{R}$, $M_n(\mathbb{C})^{\alpha}=M_n(\mathbb{R})$ | the real forms of the field and of the matrices |
| $\mathbb{B}^{\bar{\cdot}}\cong\mathbb{H}$ | the quaternion algebra as the real form of the biquaternions |
| $Z(\mathbb{H})=\mathbb{R}$ | the reason $\mathbb{H}$ carries no $\mathbb{C}$-sesquilinear structure |

## Further Reading

- Nicolas Bourbaki, *Algebra II* (Springer, 2003), for the fixed ring of an involution and the descent of the scalars.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the involutions of an algebra, their fixed subalgebras and the descent.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the fixed rings and the symmetric elements of an involutive ring.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the fixed subalgebras and the descent in the Jordan setting.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, second edition, 2001), for the quaternion algebra, its centre and the biquaternion algebra.
- The companion articles of this series: *Sesqualgebras*, *Hermitian and Skew-Hermitian Elements*, *The Involutions of a Sesqualgebra*, *Anti-Automorphisms Twisted by the Base Involution*, *Subalgebras and the Involution*, *Real Forms and the Descent of an Algebra*, *Tensor Products of Sesqualgebras* and *Biquaternions as an Algebra over $\mathbb{R}$*.
