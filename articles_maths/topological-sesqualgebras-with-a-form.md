# __Topological Sesqualgebras with a Form__

## Introduction

The layer of *Topological Sesqualgebras* names no form: it is the topological counterpart of the sesqualgebras of Part I, and the two scalar rules are the only constraints on the product. This article adds the second layer, in which a topological sesqualgebra carries a continuous Hermitian form tied to the product. It is the entry of the category *Topology on Sesqualgebras with a degree-2 form*, and it stands to *Topology on Algebras with a degree-2 form* as *Topological Sesqualgebras* stands to *Topological Algebras and Banach Algebras*: the same topological object, with a form of degree two, and the same two questions, of the radical and of the collapse.

The object of the layer is an associative topological $R$-algebra $A$ with a continuous $\varsigma$-semilinear involution $*$ and a continuous Hermitian form $h$, the sesqualgebra being the **derived operation** $x \star y = xy^{*}$ of *Sesqualgebras*, §*The Derived Operation of an Involutive Algebra*. The form is tied to the product by the **compatibility**

$$
h(xy, z) = h(y, x^{*}z)
$$

for all $x, y, z \in A$, an identity of the algebra product read through the form. It pairs the left multiplication by $x$ with the left multiplication by $x^{*}$, and read on the ternary product $xy^{*}z$ that the failure of associativity forces it says that the left multiplication by $xy^{*}$ has for adjoint the left multiplication by $yx^{*}$: the identity is $h(xy^{*}z, w) = h(z, yx^{*}w)$ on four variables.

Two facts organise the article. The compatibility is equivalent, through the Hermitian property, to the second identity $h(x, yz) = h(y^{*}x, z)$; with either form it makes the **radical** of the form a left ideal of the algebra, its image under $*$ a right ideal, and the form nondegenerate exactly when the radical vanishes. And at the trivial involution of the base the form is $R$-bilinear and symmetric, while at the trivial involution of the algebra the compatibility says that the left multiplications are self-adjoint for that symmetric form: the category collapses to the bilinear degree-2 form layer, whose objects are the topological algebras with such a form and whose theory is *Bilinear Forms*. The two hypotheses of the layer, that the object be of full type and that the form be nondegenerate, are independent, and the examples separate them.

The article defines the form, its Hermitian property and its radical, proves the two identities of the compatibility and the ideal property of the radical, treats the nondegenerate case and the collapse, separates the objects of full type from those with a nondegenerate form, and works the examples, with the matrix algebra as the model. The positivity and the norm of the form are *Positivity and the Positive Cone of a Hermitian Form* and *The Norm Defined by a Form*, the adjoint of an operator is *The Adjoint under a Hermitian Form*, the conjugation and the field case are *The Sesquilinear Form and the Conjugation*, the algebraic theory of the form is *Hermitian Forms on a Sesqualgebra*, the ternary product that the compatibility pairs is *Algebraic J\*-Algebras* and, topologically, *The Topological J\*-Algebra*, and the layer without a form is *Topological Sesqualgebras*. Throughout, $(R,\varsigma)$ is a commutative involutive topological ring with $1$, $A$ is an associative topological $R$-algebra with a continuous $\varsigma$-semilinear involution $*$, and $h : A \times A \to R$ is a continuous Hermitian form.

## The Form

### The Definition

**Definition.** Let $A$ be a topological $R$-module. A **sesquilinear form** on $A$ is a biadditive map $h : A \times A \to R$ with

$$
h(\lambda x, y) = \lambda\,h(x,y), \qquad h(x, \lambda y) = \varsigma(\lambda)\,h(x,y)
$$

for all $\lambda \in R$ and all $x, y \in A$. The form is **Hermitian** when $h(y,x) = \varsigma(h(x,y))$ for all $x, y$, and **skew-Hermitian** when $h(y,x) = -\varsigma(h(x,y))$. It is **continuous** when it is continuous as a map $A \times A \to R$ for the product topology, and **nondegenerate** when its **radical**

$$
A^{\perp} = \{x \in A : h(x,y) = 0 \text{ for all } y \in A\}
$$

is zero. A **topological sesqualgebra with a form** is an associative topological $R$-algebra with a continuous $\varsigma$-semilinear involution $*$, together with a continuous Hermitian form $h$ that is compatible with the product in the sense of the next section; its sesqualgebra is the derived operation $x \star y = xy^{*}$.

The conventions are those of the sesqualgebra block, the pairing $\varphi(x,y) = \tau(xy^{*})$ of *The Sesquilinear Adjoint Operator*, §*The Two Parities*: $R$-linear in the first slot and $\varsigma$-semilinear in the second, with the values in $R$ rather than in an algebra, and with $\varepsilon = 1$ in the sense of *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*, §*Hermitian Forms over a Ring with Involution*, where it is the first slot that carries the twist; the bilinear forms that return at the collapse are those of *Bilinear Forms*, §*Definition*.

**Proposition (the diagonal).** Let $h$ be Hermitian. Then $h(x,x) = \varsigma(h(x,x))$ for every $x$, so the diagonal takes its values in the fixed ring $R^{\varsigma}$ of the base involution. If $h$ is skew-Hermitian then $h(x,x) = -\varsigma(h(x,x))$, so the diagonal vanishes when $2$ is invertible and $\varsigma = \mathrm{id}$.

*Proof.* $h(x,x) = \varsigma(h(x,x))$ is the Hermitian condition on the pair $(x,x)$, and the skew case is the other condition on the same pair. For the last statement, $h(x,x) = -h(x,x)$ gives $2h(x,x) = 0$. $\square$

**Proposition (the radical of a continuous form is closed).** Let $h$ be continuous. Then its radical is a closed submodule of $A$.

*Proof.* For each $y$ the map $\varphi_y : x \mapsto h(x,y)$ is continuous, being the restriction of $h$ to $A \times \{y\}$, and its kernel is closed because $\{0\}$ is closed in $R$. The radical is $\bigcap_y \ker\varphi_y$, an intersection of closed sets, hence closed; it is a subgroup and stable under the scalars because each $\varphi_y$ is additive and $R$-linear. $\square$

**Remark (the radical is two-sided).** The definition of the radical is not one-sided: because $h$ is Hermitian, the elements annihilated on the right are the same as those annihilated on the left, since $h(x,y) = 0$ for all $y$ gives $h(y,x) = \varsigma(h(x,y)) = 0$ for all $y$, which is the same condition read with the variables renamed. The radical is therefore the two-sided orthogonal of $A$, and the nondegeneracy of the definition above is symmetric in the two slots.

### The Model

**Example (the matrix algebra).** Let $A = M_n(\mathbb{C})$ with the conjugate transpose $X^{*} = \overline{X}^{T}$ and the form

$$
h(X,Y) = \operatorname{tr}(XY^{*}).
$$

The form is continuous for the entrywise topology, linear in the first slot and $\varsigma$-semilinear in the second, since $h(X, \lambda Y) = \operatorname{tr}(X \overline{\lambda} Y^{*}) = \varsigma(\lambda)h(X,Y)$ with $\varsigma$ the conjugation. It is Hermitian:

$$
h(Y,X) = \operatorname{tr}(YX^{*}) = \sum_{i,j} Y_{ij}\overline{X_{ij}} = \varsigma\Bigl(\sum_{i,j} X_{ij}\overline{Y_{ij}}\Bigr) = \varsigma\bigl(h(X,Y)\bigr),
$$

and it is nondegenerate, its Gram matrix in the unit basis being the identity: if $\operatorname{tr}(XY^{*}) = 0$ for every $Y$ then $X = 0$, taking $Y$ with a single nonzero entry. This is the form of the layer, and every statement below is read on it. It is the pairing $\varphi(x,y) = \tau(xy^{*})$ of *The Sesquilinear Adjoint Operator*, §*The Two Parities*, with $\tau = \operatorname{tr}$; for a central linear functional, $\tau(uv) = \tau(vu)$, the compatibility is automatic, since $h(xy,z) = \tau(xyz^{*})$ and $h(y,x^{*}z) = \tau\bigl(y(x^{*}z)^{*}\bigr) = \tau(yz^{*}x)$ agree.

## The Compatibility

### The Identity and Its Equivalent

**Definition.** Let $h$ be a Hermitian form on $A$. The form is **compatible with the product** when

$$
h(xy, z) = h(y, x^{*}z) \qquad \text{for all } x, y, z \in A,
$$

that is, when the left multiplication by $x$ and the left multiplication by $x^{*}$ are paired by $h$.

**Theorem (the equivalent form).** A Hermitian form $h$ is compatible if and only if

$$
h(x, yz) = h(y^{*}x, z)
$$

for all $x, y, z \in A$.

*Proof.* Let $h(xy,z) = h(y,x^{*}z)$. Then $h(x, yz) = \varsigma(h(yz, x)) = \varsigma(h(z, y^{*}x)) = h(y^{*}x, z)$, where the first and last equalities are the Hermitian property and the middle is the compatibility on the pair $(y, z, x)$. The converse is the same chain read backwards. $\square$

**Theorem (the ternary identity).** Let $h$ be compatible. Then

$$
h(xy^{*}z, w) = h(z, yx^{*}w)
$$

for all $x, y, z, w \in A$.

*Proof.* The compatibility applied to the element $c = xy^{*}$ in the place of the first variable reads $h(cz, w) = h(z, c^{*}w)$, and $c^{*} = (xy^{*})^{*} = yx^{*}$, because $*$ is an anti-automorphism of order two. $\square$

**Remark (the reading).** The identity is the compatibility at the element $xy^{*}$, and it says that the one-sided multiplications come in adjoint pairs: the left multiplication $z \mapsto xy^{*}z$ has for adjoint the left multiplication $w \mapsto yx^{*}w$. This is the form-level version of $L_a^{\dagger} = L_{\sigma(a)}$ of *Adjoints in a Commutative Involutive Algebra*, §*The Adjoint of a Multiplication*, where the identity $B(ax,y) = B(x,\sigma(a)y)$ plays the same role. The ternary product $xy^{*}z$ that carries it is the triple product of *Sesqualgebras*, §*The Triple Product*, studied algebraically in *The Sesquilinear Associator and the Ternary Product*, with the axioms of *Algebraic J\*-Algebras* and the topological development of *The Topological J\*-Algebra*.

**Example (the matrix algebra, continued).** On $M_n(\mathbb{C})$ the form $h(X,Y) = \operatorname{tr}(XY^{*})$ is compatible:

$$
h(XY, Z) = \operatorname{tr}(XYZ^{*}), \qquad h(Y, X^{*}Z) = \operatorname{tr}\bigl(Y(X^{*}Z)^{*}\bigr) = \operatorname{tr}(YZ^{*}X) = \operatorname{tr}(XYZ^{*}),
$$

the middle equality by the definition of the conjugate transpose and the last by the cyclicity of the trace. The ternary identity reads

$$
\operatorname{tr}(XY^{*}ZW^{*}) = \operatorname{tr}\bigl(Z(YX^{*}W)^{*}\bigr) = \operatorname{tr}(ZW^{*}XY^{*}),
$$

which is the same computation on the four variables.

### The Radical Is an Ideal

**Theorem.** Let $h$ be compatible. Then the radical $A^{\perp}$ is a left ideal of $A$, and its image $*(A^{\perp})$ is a right ideal.

*Proof.* Let $r \in A^{\perp}$ and $a \in A$. By the equivalent form, $h(r, yz) = h(y^{*}r, z)$ for all $y, z$, and the left side vanishes because $r$ is in the radical; hence $h(y^{*}r, z) = 0$ for all $y, z$. As $y$ runs over $A$ so does $y^{*}$, so $h(ar, z) = 0$ for all $a$ and all $z$, that is $ar \in A^{\perp}$. The radical is therefore a left ideal, and the image of a left ideal under the anti-automorphism $*$ is a right ideal. $\square$

**Remark (the radical is not stable under the involution in general).** The theorem gives a left ideal and, through $*$, a right ideal, and the two agree only when $*(A^{\perp}) = A^{\perp}$, which is not automatic: on $M_n(\mathbb{C})$ with the form $h(X,Y) = \operatorname{tr}(XE_{11}Y^{*})$ of the examples below the radical is the set of matrices whose first column is zero, a left ideal that the conjugate transpose carries onto the set of matrices whose first row is zero. The asymmetry is that of the compatibility identity itself, which puts the involution on one factor and the product on the other, and it is the reason the quotient theory of the form belongs to *Hermitian Forms on a Sesqualgebra* and not to this entry.

**Proposition (nondegeneracy and the Gram matrix).** Let $A$ be a free module of finite rank with basis $e_1, \dots, e_m$ and let $H$ be the Gram matrix, $H_{ij} = h(e_i, e_j)$. Then $H$ is Hermitian, $\varsigma(H_{ij}) = H_{ji}$, and the radical is the image of the kernel of the multiplication by $H$ under the involution of the base,

$$
A^{\perp} = \varsigma\bigl(\ker H\bigr) = \ker H^{T},
$$

so $h$ is nondegenerate exactly when the multiplication by $H$ is injective. If $R$ is a field then the multiplication by $H$ is injective exactly when $H$ is invertible, so over a field the form is nondegenerate exactly when the Gram matrix is invertible.

*Proof.* The Hermitian property of $h$ gives $H_{ji} = h(e_j,e_i) = \varsigma(h(e_i,e_j)) = \varsigma(H_{ij})$, which is the assertion that $H$ is Hermitian for the involution $\varsigma$ read entrywise. In the basis

$$
h(x, y) = \sum_{i,j} x_i\,H_{ij}\,\varsigma(y_j) = x^{T}H\,\varsigma(y) = (H^{T}x)^{T}\varsigma(y),
$$

so $h(x,y) = 0$ for all $y$ exactly when $H^{T}x = 0$, because $\varsigma(y)$ ranges over the whole module as $y$ does, and that is $x \in \ker H^{T}$. The involutions of the base and of the matrix are related by $\varsigma(H) = H^{T}$, and therefore $H^{T}\varsigma(x) = \varsigma(Hx)$ and $\varsigma(H^{T}x) = H\varsigma(x)$; the first identity gives $\varsigma(\ker H) \subseteq \ker H^{T}$ and the second gives the reverse inclusion, so $\ker H^{T} = \varsigma(\ker H)$, and the radical vanishes exactly when the multiplication by $H$ is injective. Over a field an injective square matrix is invertible. $\square$

**Remark (nondegeneracy and nonsingularity).** The nondegeneracy used here is the vanishing of the radical, the notion of *Bilinear Forms*, §*Non-Degenerate Forms* in the field case and of *Unitary Geometry over a Field with Involution*, §*Definition and Matrices*; over a general ring it is weaker than the isomorphism condition that *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*, §*Hermitian Forms over a Ring with Involution* calls **nonsingularity**, and that condition for a free module of finite rank is the invertibility of the Gram matrix. The trace form of the model is nonsingular, its Gram matrix in the unit basis being the identity, and the two notions coincide over a field, which is the case in which the criterion above is stated as the invertibility of $H$.

## The Collapse at the Trivial Involution

**Theorem (the collapse of the layer).** Let $(A,h)$ be a topological sesqualgebra with a form and suppose $\varsigma = \mathrm{id}$. Then $h$ is $R$-bilinear and symmetric, $*$ is $R$-linear, and the derived operation $x \star y = xy^{*}$ is $R$-bilinear. If moreover $* = \mathrm{id}$ the compatibility reads

$$
h(xy, z) = h(y, xz),
$$

and $(A,h)$ is an object of the bilinear degree-2 form layer: a topological $R$-algebra with a continuous symmetric bilinear form satisfying the pairing condition $h(ax,y) = h(x,ay)$, that is, one for which every left multiplication is self-adjoint. Conversely every such algebra with such a form is a topological sesqualgebra with a form over $(R,\mathrm{id})$.

*Proof.* With $\varsigma = \mathrm{id}$ the involution of the base is trivial, so the form satisfies $h(\lambda x, y) = \lambda h(x,y) = h(x, \lambda y)$, which is $R$-bilinearity, and the Hermitian condition reads $h(y,x) = h(x,y)$, which is symmetry. The involution $*$ is then $R$-linear by its semilinearity, and the derived operation is bilinear. The compatibility with $* = \mathrm{id}$ is the displayed identity, which says that $h(xy,z) = h(y,xz)$ for all $x, y, z$, that is that the left multiplication by $x$ is self-adjoint for the symmetric form; the converse is the same reading. $\square$

**Remark (the commutative case).** The collapsed identity $h(xy,z) = h(y,xz)$ is the pairing condition $B(ax,y) = B(x,\sigma(a)y)$ of *Adjoints in a Commutative Involutive Algebra*, §*The Pairing and the Adjoint*, with $\sigma = \mathrm{id}$ and $a = x$, for which the adjoint of a left multiplication is again a left multiplication. When in addition the algebra is commutative it is the classical invariance of a bilinear form under an associative product, $h(xy,z) = h(x,yz)$: by commutativity and symmetry,

$$
h(xy,z) = h(y,xz) = h(y,zx) = h(zx,y) = h(x,zy) = h(x,yz),
$$

the fourth equality being the compatibility on the triple $(z,x,y)$ and the rest the commutativity of the product and the symmetry of the form. The model is $h(x,y) = \tau(xy^{*})$ for a central linear functional $\tau$, the pairing of *The Sesquilinear Adjoint Operator*, for which both identities read $\tau(xyz^{*})$.

**Theorem (objects of full type).** Let $(A,h)$ be a topological sesqualgebra with a form whose derived operation $x \star y = xy^{*}$ is of **full type** in the sense of *Sesqualgebras*, §*The Collapse at the Identity*. If $\varsigma \neq \mathrm{id}$ then $\star$ is neither associative nor commutative.

*Proof.* The derived operation is a sesqualgebra over $(R,\varsigma)$ whose hypotheses are those of the collapse theorem of *Sesqualgebras*, §*The Collapse at the Identity*, which is a statement about the scalars and the product. The form is not used in it, and the topology is not used in it. $\square$

The theorem is the sense in which the form does not bilinearize the product: a compatible Hermitian form is a structure on the object, and it leaves the failure of associativity of the sesquilinear product exactly where the collapse theorem puts it. The form repairs nothing; what it supplies is the pairing in which the adjoint of an operator is defined, which is the subject of *The Adjoint under a Hermitian Form*.

### Full Type and Nondegeneracy

**Proposition (the two conditions are independent).** The condition that the derived operation be of full type and the condition that the form be nondegenerate are independent: neither implies the other.

*Proof.* The form $h(X,Y) = \operatorname{tr}(XE_{11}Y^{*})$ on $M_n(\mathbb{C})$ is compatible, since

$$
h(XY,Z) = \operatorname{tr}(XYE_{11}Z^{*}), \qquad h(Y, X^{*}Z) = \operatorname{tr}\bigl(Y(X^{*}Z)^{*}E_{11}\bigr) = \operatorname{tr}(YZ^{*}XE_{11}) = \operatorname{tr}(XYE_{11}Z^{*}),
$$

and its radical is the set of matrices whose first column is zero, which is nonzero, so the form is degenerate; while the derived operation on $M_n(\mathbb{C})$ is of full type, because the algebra is unital and faithful over $\mathbb{C}$, and for a unital algebra the generation and annihilation conditions are automatic. In the other direction let $A = \mathbb{C}$ with the zero product, with $*$ the conjugation and $h(z,w) = z\,\varsigma(w)$; the form is nondegenerate, since $z \neq 0$ gives $h(z,1) = z \neq 0$, and it is compatible because $xy = 0$ and $x^{*}z = 0$ make both sides of the identity vanish, while the derived operation is the zero product, whose products generate the zero submodule and not $A$. $\square$

## Examples

### The Examples of the Layer

**Example (the complex numbers).** Let $A = \mathbb{C}$ over $(\mathbb{C},\varsigma)$ with the conjugation, with $* = \varsigma$ and $h(z,w) = z\,\varsigma(w) = z\overline{w}$. The form is Hermitian and nondegenerate, and it is compatible:

$$
h(xy, z) = xy\overline{z}, \qquad h(y, x^{*}z) = y\,\varsigma(x^{*}z) = y\overline{z}\,\varsigma(x^{*}) = y\overline{z}x,
$$

where $\varsigma(x^{*}) = \varsigma(\varsigma(x)) = x$; the two agree. The form is the trace form on $\mathbb{C}$ itself, $h(z,w) = z\overline{w}$, of *Unitary Geometry over a Field with Involution*, §*Definition and Matrices*. The derived operation is the sesquilinear product $x \star y = x\overline{y}$ of *Sesqualgebras*, §*Examples*, and it is of full type; since the base involution is the conjugation and not the identity, the theorem on objects of full type gives that it is neither associative nor commutative, and the collapse does not apply to it.

**Example (the matrix algebra).** On $M_n(\mathbb{C})$ the form $h(X,Y) = \operatorname{tr}(XY^{*})$ is a compatible nondegenerate Hermitian form, the model of the layer, and the derived operation is of full type, as in *Matrix Sesqualgebras*. The ternary identity reads

$$
\operatorname{tr}(XY^{*}ZW^{*}) = \operatorname{tr}\bigl(Z(YX^{*}W)^{*}\bigr) = \operatorname{tr}(ZW^{*}XY^{*}),
$$

and the algebraic theory of the ternary product that the identity pairs is *Algebraic J\*-Algebras*, whose topological development is *The Topological J\*-Algebra*.

**Example (a degenerate form on a full type object).** On $M_n(\mathbb{C})$ the form $h(X,Y) = \operatorname{tr}(XE_{11}Y^{*})$ is compatible, and its radical is the nonzero left ideal of the matrices whose first column is zero; the derived operation is nevertheless of full type. The example is the witness that full type does not force nondegeneracy.

**Example (a nondegenerate form on an object that is not of full type).** On $\mathbb{C}$ with the zero product, the conjugation and $h(z,w) = z\varsigma(w)$ the form is nondegenerate and compatible, and the derived operation is the zero product, which is not of full type. The example is the witness in the other direction, and it is the zero product of *Examples of Sesqualgebras*, §*The Zero Product*.

**Example (the collapsed model).** Let $R$ be a field with $\varsigma = \mathrm{id}$ and let $A = R$ with the algebra product and $h(x,y) = xy$. The form is bilinear, symmetric and nondegenerate, with $h(xy,z) = xyz = h(y,xz)$, so the pair is an object of the bilinear degree-2 form layer; the derived operation coincides with the algebra product, and the collapse is the one of the theorem.

## Summary

A **topological sesqualgebra with a form** is an associative topological $R$-algebra $A$ with a continuous $\varsigma$-semilinear involution $*$ and a continuous **Hermitian form** $h$, linear in the first slot and $\varsigma$-semilinear in the second, with $h(y,x) = \varsigma(h(x,y))$, that is **compatible with the product** in the identity $h(xy,z) = h(y,x^{*}z)$; the sesqualgebra of the layer is the derived operation $x \star y = xy^{*}$, and the identity pairs the left multiplication by $x$ with the left multiplication by $x^{*}$ through the form. The equivalent form is $h(x,yz) = h(y^{*}x,z)$, and the four-variable consequence $h(xy^{*}z, w) = h(z, yx^{*}w)$ says that the left multiplication by $xy^{*}$ has for adjoint the left multiplication by $yx^{*}$, so the one-sided multiplications come in adjoint pairs. The **radical** $A^{\perp} = \{x : h(x,y) = 0 \text{ for all } y\}$ is a left ideal, its image $*(A^{\perp})$ is a right ideal, and the two need not agree; the form is **nondegenerate** exactly when the radical vanishes, and the radical of a continuous form is closed. On a free module of finite rank the **Gram matrix** $H_{ij} = h(e_i,e_j)$ is Hermitian for $\varsigma$ and the radical is the image under $\varsigma$ of the kernel of the multiplication by $H$; over a field the form is nondegenerate exactly when $H$ is invertible, and nonsingularity, which is the isomorphism condition of the bilinear layer, is the invertibility of $H$ over any ring.

At $\varsigma = \mathrm{id}$ the form is $R$-bilinear and symmetric and the layer **collapses** to the topological algebras with a continuous symmetric form whose left multiplications are self-adjoint, the compatibility being $h(xy,z) = h(y,xz)$ when the algebra involution is also trivial, which is the classical invariance $h(xy,z) = h(x,yz)$ when in addition the algebra is commutative; the theory of those bilinear forms is *Bilinear Forms* and *Algebras with a degree-2 form*. The collapse is not available with a nontrivial involution: the derived operation **of full type** is neither associative nor commutative, so a compatible Hermitian form does not bilinearize the product, and the two hypotheses of the layer, full type and nondegeneracy, are independent, the matrix algebra with the form $\operatorname{tr}(XE_{11}Y^{*})$ separating them one way and the complex numbers with the zero product the other. The examples are the complex field with $z\varsigma(w)$, the matrix algebra with the trace form, the degenerate form on the matrix algebra, the zero product with a nondegenerate form, and the collapsed field.

## Summary of Notation

| symbol | meaning |
|---|---|
| $h(x,y)$ | a sesquilinear form, $R$-linear in $x$ and $\varsigma$-semilinear in $y$ |
| $h(y,x) = \varsigma(h(x,y))$ | the Hermitian condition; the skew-Hermitian one has $-\varsigma$ in its place |
| $A^{\perp}$ | the radical $\{x : h(x,y) = 0 \text{ for all } y\}$; the form is nondegenerate when it is zero |
| $h(xy,z) = h(y,x^{*}z)$ | the compatibility of the form with the product |
| $h(x,yz) = h(y^{*}x,z)$ | the equivalent form of the compatibility |
| $h(xy^{*}z, w) = h(z, yx^{*}w)$ | the ternary identity: the left multiplication by $xy^{*}$ has adjoint the left multiplication by $yx^{*}$ |
| $\operatorname{tr}(XY^{*})$ | the model form on $M_n(\mathbb{C})$ |
| $H_{ij} = h(e_i,e_j)$ | the Gram matrix, Hermitian for $\varsigma$; the radical is $\varsigma(\ker H)$, so over a field the form is nondegenerate exactly when $H$ is invertible |
| $x \star y = xy^{*}$ | the derived operation, the sesqualgebra of the layer |
| $\varsigma = \mathrm{id}$ | the collapse: the form is bilinear and symmetric, and with $* = \mathrm{id}$ the object is a topological algebra whose left multiplications are self-adjoint |

## Further Reading

- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for Hermitian forms over a ring with involution, their radicals and their Gram matrices.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the algebras with involution on which the forms of the layer are built.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Frobenius algebras with an associative bilinear form, the commutative case of the collapse.
- Seth Warner, *Topological Rings* (North-Holland, 1993), for the continuity of the form and of the involution of the base.
- Harald Upmeier, *Jordan Algebras in Analysis, Operator Theory, and Quantum Mechanics* (American Mathematical Society, 1987), for the $\mathrm{J}^*$-triples and the ternary identity of the product $xy^{*}z$ that the compatibility pairs.
- Cho-Ho Chu, *Jordan Structures in Geometry and Analysis* (Cambridge University Press, 2012), for the Hermitian structures of an algebra read algebraically.
