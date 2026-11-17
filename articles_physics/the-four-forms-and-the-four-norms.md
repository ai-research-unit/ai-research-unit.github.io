# __The Four Forms and the Four Norms__

## Introduction

**A product of two biquaternions returns a biquaternion, and its scalar part returns a complex number.** Each of the four general products of the previous entry therefore carries one function of two elements, and the four functions are the four forms. Read at their two equal arguments the four forms give four functions of one element, and those are the four algebraic norms. The two arities are the two bracket shapes, $\langle\tilde Q_1,\tilde Q_2\rangle$ for the form and $\langle\tilde Q\rangle$ for the norm.

**Every proof here is written on the coordinates.** The four forms are evaluated on the coordinates, and their inertias are those of real quadratic forms in the eight real coordinates. The multiplicativity of the quaternionic norm comes from Lagrange's identity on the cross product, and the criterion of invertibility from an explicit inverse. Neither argument leaves the algebra.

**The single idea is that two properties single out two of the four, and the two properties are different.** The quaternionic norm is the multiplicative one. The Hermitian norm is the definite one. No function is both, and the reason is the zero divisors that the complexification creates.

**The four words of the category follow the algebra and do not precede it.** The plain form is the *pairing*, the quaternionic norm the *interval*, the Hermitian norm the *weight* and the Krein norm the *volume*. Each word is earned at the end of the entry, after the object it names has been computed from the coordinates.

## The Source Table

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| the four forms, their brackets, their values on a basis, their inertias, their null sets, the two slots, the four algebraic norms, multiplicativity and definiteness, the qualified regular and degenerate pairs | [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](../articles_maths/the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html) |
| the twelve operations and their scalar parts, the symmetrisation that keeps a form and the antisymmetrisation that kills it, the distinction over $\mathbb{C}$ and the coincidence over $\mathbb{R}$ | [Symmetric and Antisymmetric Decomposition of the Four General Products](../articles_maths/symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html) |
| the four general products whose scalar parts the four forms are, the identities among the four scalar parts | [The Four General Products and Their Relations over the Biquaternion Algebra](../articles_maths/the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html) |
| the restriction of the four forms and the four norms to the six remarkable subspaces, the inertias, the definiteness on each | [Remarkable Subspaces and the Four General Products, Forms and Norms](../articles_maths/remarkable-subspaces-and-the-four-general-products-forms-and-norms.html) |
| the $\natural$-regular and $\natural$-degenerate partition, the group of invertibles, the null cone, the criterion of invertibility | [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html) |
| the Krein partition, the two sectors of the Krein norm, the indefinite geometry | [Kr-Regularity and Degeneracy in the Biquaternion Algebra](../articles_maths/kr-regularity-and-degeneracy-in-the-biquaternion-algebra.html) |
| the algebraic norm of a form and its distinction from the topological norm | [The Norm Defined by a Form](../articles_maths/the-norm-defined-by-a-form.html) |
| the one topological norm of the space and its square root | [The Euclidean Topology of the Biquaternion Algebra](../articles_maths/the-euclidean-topology-of-the-biquaternion-algebra.html) |
| the unqualified *regular* and *degenerate*, which are spectral and not norm-theoretic | [The Spectrum](../articles_maths/the-spectrum.html) |

**The rows are the order of the entry.** The four forms first, because they are the objects. Then the count of the four, which is one lemma. Then the inertias, which are what a restriction can change. Then the groups, which are what a form preserves. Then the four cuts, which are what a norm separates. The readings come last, and each names the section of mathematics it rests on.

## Notational Conventions

$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the biquaternion algebra, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, $e_t=1$, $\vec e_k^{2}=-e_t$, and central scalar imaginary $i$, $i^{2}=-1$. A general element is $\tilde Q=\sum_\mu Q_\mu e_\mu$, with $Q_\mu\in\mathbb{C}$ and $\mu\in\{t,x,y,z\}$. In the centre–vector split it is $\tilde Q=c+v$, with $c=Q_te_t$ in the centre $\mathbb{B}_C$ and $v=\sum_{k=1}^{3}Q_k\vec e_k$ in the vector subspace $\mathbb{B}_V$.

**The three conjugations.** The scalar part is $\mathrm{Sc}$, taking the coefficient of $e_t$. The coefficientwise conjugation is $\bar{\cdot}$. The quaternion conjugation is ${}^{\natural}$, with $Q^{\natural}_\nu=\varepsilon_\nu Q_\nu$ and $\varepsilon=(1,-1,-1,-1)$. The Hermitian conjugation is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, so $Q^{*}_{\nu}=\varepsilon_\nu\overline{Q_\nu}$. Both ${}^{\natural}$ and ${}^{*}$ are involutions, and ${}^{\natural}$ is an algebra automorphism.

**The vector calculus.** The vector parts carry the complex bilinear dot product $(\vec Q_1,\vec Q_2)=\sum_k Q_{1k}Q_{2k}$ and the cross product $\vec Q_1\times\vec Q_2$, both complex bilinear, so that

$$
\vec Q_1\vec Q_2=-(\vec Q_1,\vec Q_2)+\vec Q_1\times\vec Q_2 .
$$

The bracket is not the modulus and it is not Hermitian: $(\vec Q,\vec Q)$ is a complex number and may vanish off the origin.

**The four brackets and the four letters.** The four forms are $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$. Their letters are $P$ for the plain, $N$ for the quaternionic, $H$ for the Hermitian and $\mathrm{Kr}$ for the Krein. The rule is one line, read at two arities: a form is a product read on its scalar part with one conjugation per slot, $\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}\bigl(K_1(\tilde Q_1)K_2(\tilde Q_2)\bigr)$ with $K_1$ the identity or ${}^{\natural}$ and $K_2$ the identity or ${}^{*}$, and the algebraic norm is that same expression at two equal arguments, $\langle\tilde Q\rangle=\langle\tilde Q,\tilde Q\rangle$. The four choices of the pair $(K_1,K_2)$ are the four forms.

**Bilinear and sesquilinear.** A form is $\mathbb{C}$-**bilinear** when a scalar pulls out of its second slot, and **sesquilinear** when the scalar pulls out conjugated. The distinction is decided by the star in the second slot and by nothing else. The Euclidean norm is $\lVert\tilde Q\rVert=\bigl(\sum_\mu\lvert Q_\mu\rvert^{2}\bigr)^{1/2}$, the square root of the algebraic norm of $\langle\cdot,\cdot\rangle_{*}$.

## The Form of an Operation

**Definition (the form of an operation).** Let $f$ be an operation on $\mathbb{B}$. Its **scalar part** is the function that sends a pair to $\mathrm{Sc}\,f(\tilde Q_1,\tilde Q_2)$, and that function is the **form of the operation $f$**. It is bilinear when the second slot of $f$ is read without the star, and sesquilinear when it is read with the star.

**The value lies in $\mathbb{C}$ in both cases, and the second slot decides whether it is real.** A sesquilinear form is conjugate-symmetric, its value at the reversed pair being the complex conjugate, so its algebraic norm is real. A bilinear form is symmetric, the two orders agreeing, because the commutator of two elements is purely vector, $[\tilde Q_1,\tilde Q_2]=2\vec Q_1\times\vec Q_2$, and the scalar part kills it.

**A form that vanishes identically is the zero form.** It is not counted as a fifth form. The four antisymmetric operations below carry it.

## The Four Forms

The four forms are the scalar parts of the four general products, one to each reading of the two slots. Each is written on the coordinates of a pair, with its values on the basis and the inertia of its realification.

### The Plain Form

**The plain form, written $P$.**

$$
P(\tilde Q_1,\tilde Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)=Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2),
$$

the scalar part of the general plain bilinear product. It is symmetric, $\mathbb{C}$-bilinear and complex-valued. Its values on the basis are the signs $\langle\vec e_\mu,\vec e_\nu\rangle=\varepsilon_\mu\delta_{\mu\nu}$, written $\mathrm E$, and its realification is of inertia $(4,4)$. It is non-degenerate.

Its null set is the complex cone $\sum_\mu\varepsilon_\mu Q_\mu^{2}=0$, of real dimension six. That cone is neither the zero-divisor cone nor the null cone of the algebra, and it cuts across the invertibles and the non-invertibles alike. On the anti-Hermitian subspace its algebraic norm is negative definite, and on the Hermitian subspace positive definite.

### The Quaternionic Form

**The quaternionic form, written $N$.**

$$
N(\tilde Q_1,\tilde Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)=Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2),
$$

the scalar part of the general quaternionic bilinear product. It is the plain form read through the quaternion conjugation of the first slot, and it differs from it by the sign of the vector part alone. It is symmetric, $\mathbb{C}$-bilinear and complex-valued, its values on the basis are all $+1$, written $\mathrm I_4$, and its realification is of inertia $(4,4)$. It is non-degenerate.

Its null set is the zero-divisor cone $\mathcal N=\{\langle\tilde Q\rangle_{\natural}=0\}$, of real dimension six, which is the null cone of the algebra. The conjugation of the first slot is what gives the square the positive sign on the vector part, and that sign is the whole difference between the two bilinear forms.

### The Hermitian Form

**The Hermitian form, written $H$.**

$$
H(\tilde Q_1,\tilde Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2}),
$$

the scalar part of the general plain sesquilinear product. It is conjugate-symmetric, $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\overline{\langle\tilde Q_2,\tilde Q_1\rangle_{*}}$, and sesquilinear in the second slot. Its values on the basis are all $+1$, and its realification is of inertia $(8,0)$.

Its algebraic norm is real and positive definite, $\langle\tilde Q,\tilde Q\rangle_{*}>0$ for $\tilde Q\neq0$, and it is the square of the Euclidean norm, $\langle\tilde Q\rangle_{*}=\lVert\tilde Q\rVert^{2}$. It is non-degenerate, and its null set is the origin alone, so it has no cone. It is the only one of the four that is definite at the two equal arguments.

### The Krein Form

**The Krein form, written $\mathrm{Kr}$.**

$$
\mathrm{Kr}(\tilde Q_1,\tilde Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})=Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2}),
$$

the scalar part of the general quaternionic sesquilinear product. It is the Hermitian form read through the quaternion conjugation of the first slot, and it differs from it by the sign of the vector part alone. It is conjugate-symmetric and sesquilinear, its values on the basis are the signs $\mathrm E$, and its realification is of inertia $(2,6)$.

Its algebraic norm is real and indefinite, and it is the difference of the two contents of the centre–vector split,

$$
\mathrm{Kr}(\tilde Q)=\lvert Q_t\rvert^{2}-\lvert\vec Q\rvert^{2}.
$$

It is non-degenerate, and its null set is the real cone $\mathcal K=\{\lvert Q_t\rvert^{2}=\lvert\vec Q\rvert^{2}\}$, of real dimension seven.

## The Table of the Four Forms

| Full form name | Reduced name | Letter | Bracket | Expression with $\mathrm{Sc}$ | Coordinates | On the basis | Inertia over $\mathbb{R}$ | Null set | Values land in |
|---|---|---|---|---|---|---|---|---|---|
| The general plain bilinear form | **Plain Form** | $P$ | $\langle\cdot,\cdot\rangle$ | $\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | $Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)$ | $\mathrm E$ | $(4,4)$ | the complex cone | $\mathbb{C}$ |
| The general quaternionic bilinear form | **Quaternionic Form** | $N$ | $\langle\cdot,\cdot\rangle_{\natural}$ | $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)$ | $Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)$ | $\mathrm I_4$ | $(4,4)$ | $\mathcal N$, the zero-divisor cone | $\mathbb{C}$ |
| The general plain sesquilinear form | **Hermitian Form** | $H$ | $\langle\cdot,\cdot\rangle_{*}$ | $\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ | $Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})$ | $\mathrm I_4$ | $(8,0)$ | $\{0\}$ | $\mathbb{R}$ |
| The general quaternionic sesquilinear form | **Krein Form** | $\mathrm{Kr}$ | $\langle\cdot,\cdot\rangle_{\natural*}$ | $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})$ | $Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})$ | $\mathrm E$ | $(2,6)$ | $\mathcal K$, the Krein cone | $\mathbb{R}$ |

**The table separates the four by their letter, their bracket, the product under $\mathrm{Sc}$, their values on the basis, the inertia of the realification and the null set.** The last column divides them into two and two: the two bilinear forms land in $\mathbb{C}$, and the two sesquilinear forms land in $\mathbb{R}$. The star in the second slot is what makes an algebraic norm real.

## Why the Other Eight Operations Add No Form

The four forms are the scalar parts of the four general products, and the eight remaining operations of *Symmetric and Antisymmetric Decomposition of the Four General Products* add none. A symmetric part keeps the scalar part of its general product, and an antisymmetric part loses it.

**Lemma.** For a general product $f$ with parts $f^{\mathrm s}$ and $f^{\mathrm a}$, $\mathrm{Sc}\,f^{\mathrm s}=\mathrm{Sc}\,f$ and $\mathrm{Sc}\,f^{\mathrm a}=0$.

*Proof.* For the two bilinear families the scalar part is symmetric, $\mathrm{Sc}\,f(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}\,f(\tilde Q_2,\tilde Q_1)$, so the half-sum equals $\mathrm{Sc}\,f$ and the half-difference vanishes. For the two sesquilinear families the exchange is the conjugate transpose, and the value it pairs with $f(\tilde Q_1,\tilde Q_2)$ has the same scalar part, $\mathrm{Sc}\,\overline{f(\tilde Q_2,\tilde Q_1)}=\mathrm{Sc}\,f(\tilde Q_1,\tilde Q_2)$. The half-sum therefore keeps the scalar part, and the half-difference kills it.

**Proposition.** The twelve operations carry exactly four non-zero forms, each shared by a general product and by the symmetric part of its family. The four antisymmetric operations carry the zero form.

*Proof.* The lemma gives the first clause. The four are distinct as functions of a pair: at $\tilde Q_1=\vec e_x$ and $\tilde Q_2=\vec e_x+i\vec e_x$ they take the four values $-(1+i)$, $1+i$, $1-i$ and $-(1-i)$.

**Remark (the zero form is not a fifth form).** The four antisymmetric operations have zero scalar part, and their values lie in the vector subspace. The operations are counted with no form rather than with a fifth one.

## The Isometry Groups of the Four Forms

**Definition (isometry group).** A $\mathbb{C}$-linear operator $T$ **preserves** a form when the value at the transformed pair equals the value at the pair, for every pair. The preserving operators form a group, the **isometry group** of the form.

**Theorem (the four isometry groups).** The four isometry groups are the complex orthogonal group, twice, the unitary group of the definite Hermitian form, and the indefinite unitary group of inertia $(1,3)$:

$$
\mathrm{Isom}(P)=O_4(\mathbb{C}),\qquad
\mathrm{Isom}(N)=O_4(\mathbb{C}),\qquad
\mathrm{Isom}(H)=\mathrm{U}(4),\qquad
\mathrm{Isom}(\mathrm{Kr})=\mathrm{U}(1,3),
$$

of real dimensions $12$, $12$, $16$ and $16$.

*Proof.* The substitution $\vec Q\mapsto i\vec Q$ leaves the scalar coordinate alone and multiplies the vector part by $i$. It turns $Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)$ into $Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)$, so it carries the plain form to the quaternionic one. Two forms carried into each other by an invertible linear map have conjugate isometry groups, so the two bilinear groups are one group in two coordinate systems, the complex orthogonal group of either. The Hermitian pair is not of this kind: a Hermitian form has an inertia, an invertible linear change of coordinates preserves it, and $\mathrm E$ has inertia $(1,3)$ while $\mathrm I_4$ has $(4,0)$. So the fourth group is not a conjugate of the third, and it is the indefinite unitary group of the sign form. The dimensions are those of the classical groups.

**Remark (the two slots read on the groups).** The **second slot** decides whether the group is orthogonal or unitary, because it decides whether the form is bilinear or Hermitian. The **first slot** decides which orthogonal or unitary form, the sign data against the identity, and with it the compactness of the group.

**Remark (the quaternion conjugation lies in all four groups).** The involution ${}^{\natural}$ is an anti-automorphism and an involution, so $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{\natural})=\mathrm{Sc}((\tilde Q_2\tilde Q_1)^{\natural})=\mathrm{Sc}(\tilde Q_2\tilde Q_1)=\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, and the same computation with a star in the second slot gives the other two. The fundamental symmetry of the indefinite structure is therefore a symmetry of every one of the four measures, and it is not a property of the Krein form alone.

## The Two Slots

**The mechanism.** A form is obtained from a product by reading the first factor either as it stands or through the quaternion conjugation ${}^{\natural}$, and the second factor either as it stands or through the star ${}^{*}$. Nothing else varies. The four forms are indexed by a two-by-two grid, and the grid is the whole of the subject.

**What each slot decides.**

- The **second slot** decides whether the form is a **composition** or a **pairing**. Read without the star the form is bilinear and symmetric and can be iterated; read with the star it is sesquilinear and conjugate-symmetric and can only be evaluated. This is the slot that separates the two bilinear forms from the two sesquilinear ones, and it is what makes the algebraic norm of a sesquilinear form real.
- The **first slot** decides the **signs on the basis** and the **inertia**, and through them the **definiteness on each subspace**. Read as it stands the form is $P$ or $H$; read through the quaternion conjugation it is $N$ or $\mathrm{Kr}$. Since the quaternion conjugation multiplies the vector part by $-1$, the first slot flips the coefficients of the vector part and so turns the signs $\mathrm E$ into the plus signs $\mathrm I_4$.

## What the Four Forms Separate

**Proposition (no two of the four agree).** No two of the four forms are equal as functions of two elements.

*Proof.* At $\tilde Q_1=\vec e_x$ and $\tilde Q_2=\vec e_x+i\vec e_x$ the four values are $-(1+i)$, $1+i$, $1-i$ and $-(1-i)$, four different complex numbers.

**The second slot gives the symmetry, and the first slot gives the inertia.** The four fall into two pairs by symmetry, $\{P,N\}$ bilinear and $\{H,\mathrm{Kr}\}$ sesquilinear, and into two other pairs by their signs on the basis, $\{P,\mathrm{Kr}\}$ of signs $\mathrm E$ and $\{N,H\}$ of signs $\mathrm I_4$. The two divisions are independent, and their product is the four: each form is the intersection of one symmetry with one set of signs, which is the two-by-two grid of the two slots.

**The four collapse to two on real elements.** For real $\tilde Q_1,\tilde Q_2$ the coefficientwise conjugation is the identity, so $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\langle\tilde Q_1,\tilde Q_2\rangle$ and $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$. On the real part of the space the four forms are the two, and only the complex structure separates them.

**The null sets are four.** The null set of $P$ is the complex cone, that of $N$ the zero-divisor cone $\mathcal N$, that of $H$ the origin alone, and that of $\mathrm{Kr}$ the real cone $\mathcal K$. Three of the four are cones, of real dimensions six, six and seven. The two of dimension six do not agree, so the complex cone is not the null cone. The fourth null set is the origin, so the Hermitian form is definite and has no cone.

## The Algebraic Norm of an Operation

**Definition (algebraic norm).** The **algebraic norm** of a form is that form read at its two equal arguments, a function of one element. The four forms give four algebraic norms, written $P$, $N$, $H$ and $\mathrm{Kr}$.

**The value lies in the ring of the form.** It is complex for the two bilinear forms and real for the two sesquilinear ones. A form that vanishes identically gives the zero function, and that is the case of the four antisymmetric operations.

**The twelve operations carry these four and no more.** Symmetrisation keeps the scalar part of a product and antisymmetrisation kills it, so each family hands its form to two of its three operations and nothing to the third. The four are distinct as functions of one element: on $\vec e_x$ and on $ie_t$ their value pairs are $(-1,-1)$, $(1,-1)$, $(1,1)$ and $(-1,1)$, in the order $P$, $N$, $H$, $\mathrm{Kr}$.

## The Four Norms

The four norms are the four forms read at their two equal arguments. Each is written on the coordinates of one element, with its values on the basis and the inertia of its realification.

### The Plain Norm

**The plain norm, written $P$.**

$$
P(\tilde Q)=\langle\tilde Q\rangle=\langle\tilde Q,\tilde Q\rangle=\mathrm{Sc}(\tilde Q^{2})=\sum_\mu\varepsilon_\mu Q_\mu^{2}=Q_t^{2}-Q_x^{2}-Q_y^{2}-Q_z^{2},
$$

the plain form read at two equal arguments. It is complex-valued and $\mathbb{C}$-quadratic, its values on the basis are the signs $\mathrm E$, and its realification is of inertia $(4,4)$.

Its null set is the complex cone, of real dimension six. It is not multiplicative, and it decides no invertibility: the unit $e_t+\vec e_x$ has norm zero and the zero divisor $e_t+i\vec e_x$ has norm $2$. The square, its idempotents, its Peirce decomposition, its roots and its cone are properties of the product, which comes before the form.

### The Quaternionic Norm

**The quaternionic norm, written $N$.**

$$
N(\tilde Q)=\langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde Q^{\natural}\tilde Q)=\sum_\mu Q_\mu^{2}=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2},
$$

the quaternionic form read at two equal arguments. It is complex-valued, its values on the basis are all $+1$, and its realification is of inertia $(4,4)$.

Its null set is the zero-divisor cone $\mathcal N$, of real dimension six, and the norm is the reason the algebra has zero divisors at all.

**Proposition (multiplicativity).** The quaternionic norm is multiplicative:

$$
\langle\tilde Q_1\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1\rangle_{\natural}\,\langle\tilde Q_2\rangle_{\natural}.
$$

*Proof.* Write $\tilde Q_1=c_1+v_1$ and $\tilde Q_2=c_2+v_2$. The product is

$$
\tilde Q_1\tilde Q_2=\bigl(c_1c_2-(v_1,v_2)\bigr)+\bigl(c_1v_2+c_2v_1+v_1\times v_2\bigr),
$$

so its quaternionic norm is the sum of two squares,

$$
\bigl(c_1c_2-(v_1,v_2)\bigr)^{2}+\bigl(c_1v_2+c_2v_1+v_1\times v_2\bigr)^{2}.
$$

The cross terms $(v_2,v_1\times v_2)$ and $(v_1,v_1\times v_2)$ vanish, since a cross product is orthogonal to both its factors for the bilinear dot product. The remaining square of the vector part is

$$
c_1^{2}(v_2,v_2)+c_2^{2}(v_1,v_1)+2c_1c_2(v_1,v_2)+(v_1\times v_2,v_1\times v_2),
$$

and Lagrange's identity $(v_1\times v_2,v_1\times v_2)=(v_1,v_1)(v_2,v_2)-(v_1,v_2)^{2}$ cancels the mixed term. The sum is then

$$
c_1^{2}c_2^{2}+c_1^{2}(v_2,v_2)+c_2^{2}(v_1,v_1)+(v_1,v_1)(v_2,v_2),
$$

which is the product of the two norms.

**The identity $\tilde Q\tilde Q^{\natural}=\langle\tilde Q\rangle_{\natural}e_t$ is the other half of the same computation.** In the split it reads $(c+v)(c-v)=c^{2}-v^{2}=\bigl(c^{2}+(v,v)\bigr)e_t$, and it gives the inverse of every element of non-zero norm,

$$
\tilde Q^{-1}=\frac{\tilde Q^{\natural}}{\langle\tilde Q\rangle_{\natural}}.
$$

**Corollary (the criterion of invertibility).** An element is invertible exactly when its quaternionic norm is non-zero, and the group of invertibles is the level set $\langle\cdot\rangle_{\natural}=1$.

*Proof.* If the norm is non-zero, the formula above exhibits an inverse. If the norm is zero and the element is non-zero, then $\tilde Q\tilde Q^{\natural}=0$ with $\tilde Q^{\natural}\neq0$, so the element is a zero divisor and has no inverse. The origin has zero norm and is not invertible. A multiplicative function with value $1$ at $e_t$ is a homomorphism, so its level set $1$ is a group.

### The Hermitian Norm

**The Hermitian norm, written $H$.**

$$
H(\tilde Q)=\langle\tilde Q\rangle_{*}=\langle\tilde Q,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde Q\tilde Q^{*})=\sum_\mu\lvert Q_\mu\rvert^{2}=\lvert Q_t\rvert^{2}+\lvert Q_x\rvert^{2}+\lvert Q_y\rvert^{2}+\lvert Q_z\rvert^{2},
$$

the Hermitian form read at two equal arguments. It is real-valued, $\mathbb{R}$-quadratic and positive definite, $H(\tilde Q)>0$ for $\tilde Q\neq0$; its values on the basis are all $+1$, and its realification is of inertia $(8,0)$.

Its null set is the origin alone, so it has no cone. It is the one norm of the four whose square root is the topological norm, and that root gives the distance, the balls, the convergence, the bounded operators and the completion of the space. It is not multiplicative, and the section after next proves that no definite function on this algebra is.

### The Krein Norm

**The Krein norm, written $\mathrm{Kr}$.**

$$
\mathrm{Kr}(\tilde Q)=\langle\tilde Q\rangle_{\natural*}=\langle\tilde Q,\tilde Q\rangle_{\natural*}=\mathrm{Sc}(\tilde Q^{\natural}\tilde Q^{*})=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}=\lvert Q_t\rvert^{2}-\lvert Q_x\rvert^{2}-\lvert Q_y\rvert^{2}-\lvert Q_z\rvert^{2},
$$

the Krein form read at two equal arguments. It is real-valued and indefinite, its values on the basis are the signs $\mathrm E$, and its realification is of inertia $(2,6)$.

It is the difference of the two contents of the centre–vector split, so its null set is the real cone $\mathcal K$, of real dimension seven. It is not multiplicative. Its two value-one sets have different topologies: on $\{\mathrm{Kr}=1\}$ the vector part is free and the set is $S^{1}\times\mathbb{R}^{6}$, while on $\{\mathrm{Kr}=-1\}$ the scalar part is free and the set is $\mathbb{R}^{2}\times S^{5}$, so no level set of the norm is a sphere.

## The Table of the Four Norms

| Full norm name | Reduced name | Letter | Norm | Expression with $\mathrm{Sc}$ | Coordinates | On the basis | Inertia over $\mathbb{R}$ | Null set | Values land in |
|---|---|---|---|---|---|---|---|---|---|
| The general plain bilinear algebraic norm | **Plain Norm** | $P$ | $\langle\cdot\rangle$ | $\mathrm{Sc}(\tilde Q^{2})$ | $\sum_\mu\varepsilon_\mu Q_\mu^{2}$ | $\mathrm E$ | $(4,4)$ | the complex cone | $\mathbb{C}$ |
| The general quaternionic bilinear algebraic norm | **Quaternionic Norm** | $N$ | $\langle\cdot\rangle_{\natural}$ | $\mathrm{Sc}(\tilde Q^{\natural}\tilde Q)$ | $\sum_\mu Q_\mu^{2}$ | $\mathrm I_4$ | $(4,4)$ | $\mathcal N$, the zero-divisor cone | $\mathbb{C}$ |
| The general plain sesquilinear algebraic norm | **Hermitian Norm** | $H$ | $\langle\cdot\rangle_{*}$ | $\mathrm{Sc}(\tilde Q\tilde Q^{*})$ | $\sum_\mu\lvert Q_\mu\rvert^{2}$ | $\mathrm I_4$ | $(8,0)$ | $\{0\}$ | $\mathbb{R}$ |
| The general quaternionic sesquilinear algebraic norm | **Krein Norm** | $\mathrm{Kr}$ | $\langle\cdot\rangle_{\natural*}$ | $\mathrm{Sc}(\tilde Q^{\natural}\tilde Q^{*})$ | $\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$ | $\mathrm E$ | $(2,6)$ | $\mathcal K$, the Krein cone | $\mathbb{R}$ |

**The table separates the four by their letter, the product under $\mathrm{Sc}$, their coordinates, their values on the basis, the inertia of the realification and the null set.** Multiplicativity singles out the quaternionic norm and definiteness singles out the Hermitian one, so the quaternionic norm answers *when is the element invertible* and the Hermitian one answers *what is the distance*. The plain and the Krein norms are the two indefinite remainders, one complex and one real, and each is the sign-flipped twin of a working norm: the plain is the quaternionic with the sign of the vector part reversed, the Krein is the Hermitian with the same reversal. The four words of the category attach to the letters: the plain norm is the *pairing* read on the diagonal, the quaternionic the *interval*, the Hermitian the *weight* and the Krein the *volume*.

## What the Four Norms Separate

**Proposition (no function is both definite and multiplicative).** No function $g$ on $\mathbb{B}$ with $g(0)=0$ is both definite, real-valued and non-zero off the origin, and multiplicative.

*Proof.* Let $z_\pm=e_t\pm i\vec e_x$. Then $(i\vec e_x)^{2}=\vec e_x^{2}$ and $z_+z_-=e_t^{2}-(i\vec e_x)^{2}=e_t+e_t=0$, with $z_\pm\neq0$. A multiplicative function $g$ with $g(0)=0$ gives $g(z_+)g(z_-)=0$, so one of the two values is zero on a non-zero element. A definite function is non-zero there. No function is both.

**Corollary.** The Hermitian norm is definite and not multiplicative. The quaternionic norm is multiplicative and not definite, being complex-valued and vanishing on the whole zero-divisor cone. No third norm of the four repairs the split.

**Proposition (only the quaternionic norm is multiplicative).** Of the four norms, $\langle\cdot\rangle_{\natural}$ alone satisfies $\langle\tilde Q_1\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1\rangle_{\natural}\langle\tilde Q_2\rangle_{\natural}$.

*Proof.* The quaternionic norm is multiplicative by the proposition of its section. The other three are refuted by one substitution each. For $P$: $\vec e_x\vec e_y=\vec e_z$, so $P(\vec e_x\vec e_y)=-1$ while $P(\vec e_x)P(\vec e_y)=(-1)(-1)=1$. For $H$: $H(\vec e_x+i\vec e_y)=2$ while $(\vec e_x+i\vec e_y)^{2}=\vec e_x^{2}+(i\vec e_y)^{2}=-e_t+e_t=0$ and $H(0)=0$. For $\mathrm{Kr}$: $\mathrm{Kr}(e_t+\vec e_x)=0$ while $(e_t+\vec e_x)^{2}=2\vec e_x$ and $\mathrm{Kr}(2\vec e_x)=-4$.

**Remark (the two senses of norm).** Two different objects carry the name. The **algebraic norm** is a map into the ring, into $\mathbb{C}$ for the two bilinear forms and into $\mathbb{R}$ for the two sesquilinear ones; it belongs to algebra, with its quadratic forms, its polarisations and its zero divisors. The **topological norm** is the one selection of positive real values, $\lVert\tilde Q\rVert=H(\tilde Q)^{1/2}$; it belongs to topology, with its distances, its balls and its completeness. Only the Hermitian norm of the four yields it.

**Remark (the four collapse to two on real elements).** For real $\tilde Q_1,\tilde Q_2$ the coefficientwise conjugation is the identity, so $P=\mathrm{Kr}$ and $N=H$ on the real part of the space. On real coefficients the four norms are the two, and a computation restricted to them sees two and hides the other two.

## Multiplicativity, Definiteness and the Zero Divisors

**The precise claim.** The proposition above is the organising fact of the four-norm table, and it is often paraphrased as the statement that no form on $\mathbb{B}$ can be both commutative and definite. The paraphrase misplaces the word. Commutativity is a property of a product; a form is symmetric or conjugate-symmetric, and all four forms here have that property by construction. What the proposition separates is **multiplicativity**, the value of the norm of a product being the product of the two values, and **definiteness**, real values, zero at the origin and non-zero off it. The normalisation to zero at the origin belongs to the definition: without it the constant function $1$ is multiplicative and non-zero off the origin.

**Symmetry is not the failing property.** The scalar part of a product is symmetric because the commutator is purely vector, and this is why the four forms are symmetric or conjugate-symmetric. The algebra itself is not commutative: $\vec e_x\vec e_y=\vec e_z$ while $\vec e_y\vec e_x=-\vec e_z$. The symmetry of the four forms therefore survives the non-commutativity of the product, and it cannot fail in the passage from one form to another.

**The mechanism is the zero divisors.** Let $g$ be multiplicative and definite. The pair $z_\pm=e_t\pm i\vec e_x$ has $z_+z_-=0$ with $z_\pm\neq0$, so

$$
g(z_+)g(z_-)=g(0)=0,
$$

both values are non-zero by definiteness, and their product cannot be zero. No commutativity is used in the argument.

**The obstruction is not the failure of commutativity, and the examples say so.** The quaternions are not commutative, and $q\mapsto q\bar q$ is definite and multiplicative, because they have no zero divisors. The dual numbers $\mathbb{C}[\varepsilon]/(\varepsilon^{2})$ are commutative, and they admit no definite multiplicative function, since $g(\varepsilon)^{2}=g(\varepsilon^{2})=g(0)=0$ forces $g(\varepsilon)=0$ on a non-zero element. The obstruction is the zero divisor.

**The four sectors.** The quaternionic norm is multiplicative and not definite: it is complex-valued and vanishes on the whole zero-divisor cone. The Hermitian norm is definite and not multiplicative. The plain norm is neither: it is complex-valued, indefinite, and $P(\vec e_x\vec e_y)=-1$ while $P(\vec e_x)P(\vec e_y)=1$. The Krein norm is neither: it is real and indefinite, and $\mathrm{Kr}(e_t+\vec e_x)=0$ while $(e_t+\vec e_x)^{2}=2\vec e_x$ has value $-4$. The two-by-two table is therefore

| | definite | not definite |
|---|---|---|
| **multiplicative** | empty | $N$ |
| **not multiplicative** | $H$ | $P$ and $\mathrm{Kr}$ |

**The empty sector is the proposition.** The other three sectors are the two single-property survivors and the pair that keeps neither.

**The Hurwitz comparison.** In $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ and $\mathbb{O}$ the norm form is definite and multiplicative at once, because there are no zero divisors, and the two senses of *norm* coincide. In $\mathbb{B}$ the complexification creates zero divisors, and the quaternion norm complexifies to $N$, which keeps multiplicativity and loses definiteness, while the Euclidean norm of the coefficient space is the square root of $H$, which keeps definiteness and loses multiplicativity. The split is the failure of $\mathbb{B}$ to be a normed division algebra, and the zero divisors are its mechanism.

## The Qualified Regular and Degenerate Pairs

**Definition (the qualified regular and the qualified degenerate).** A biquaternion is **regular for a letter** when the value of that letter is non-zero, and **degenerate for a letter** when the value is zero. A $\natural$-regular biquaternion has $\langle\tilde Q\rangle_{\natural}\neq0$, a $P$-regular one has $P(\tilde Q)\neq0$, and the $H$ and $\mathrm{Kr}$ cases read the same way; the degenerate notion replaces non-zero by zero.

**The four conditions are polynomial equations on the eight real coordinates, homogeneous of degree two.** Written out,

$$
P(\tilde Q)=Q_t^{2}-Q_x^{2}-Q_y^{2}-Q_z^{2}=0,\qquad
\langle\tilde Q\rangle_{\natural}=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}=0,
$$

$$
H(\tilde Q)=\lvert Q_t\rvert^{2}+\lvert Q_x\rvert^{2}+\lvert Q_y\rvert^{2}+\lvert Q_z\rvert^{2}=0,\qquad
\mathrm{Kr}(\tilde Q)=\lvert Q_t\rvert^{2}-\lvert Q_x\rvert^{2}-\lvert Q_y\rvert^{2}-\lvert Q_z\rvert^{2}=0.
$$

Two of them are two real equations, for the complex-valued $P$ and $N$, and two are one real equation, for the real-valued $H$ and $\mathrm{Kr}$. Each defines a cone with apex the origin.

| letter | degenerate set | $\dim_{\mathbb R}$ | contains a unit | equals the non-invertibles |
|---|---|---|---|---|
| $P$ | the complex cone $\{P=0\}$ | $6$ | yes | no |
| $N$ | $\mathcal N$, the origin together with the zero divisors | $6$ | no | **yes** |
| $H$ | $\{0\}$ | $0$ | no | no |
| $\mathrm{Kr}$ | $\mathcal K$, the real cone $\{\mathrm{Kr}=0\}$ | $7$ | yes | no |

**Proposition (only the $\natural$-degenerate set is the non-invertible set).** The $\natural$-degenerate biquaternions are the origin and the zero divisors, $\{N=0\}=\{0\}\cup\mathcal Z$, and they alone are the non-invertibles. The plain and the Krein degenerate sets contain units, and the Hermitian degenerate set contains the origin alone.

*Proof.* The criterion of invertibility identifies $\{N=0\}$ with the origin and the zero divisors. The unit $e_t+\vec e_x$ has $P=\mathrm{Kr}=0$ and $N=2$, so the plain and the Krein sets contain a unit. The Hermitian norm is a sum of four non-negative terms.

**Remark (the four sets are distinct).** Four elements witness it. The unit $e_t+\vec e_x$ is $P$-degenerate and $\mathrm{Kr}$-degenerate, and not $N$-degenerate. The zero divisor $e_t+i\vec e_x$ is $N$-degenerate and $\mathrm{Kr}$-degenerate, with $P=2$. The zero divisor $\vec e_x+i\vec e_y$ is $P$-degenerate and $N$-degenerate, with $\mathrm{Kr}=-2$. The element $\sqrt2\,e_t+\vec e_x+i\vec e_y$ is $\mathrm{Kr}$-degenerate, with $P=N=2$. The $H$-degenerate set is the origin alone.

**Remark (the origin is degenerate for all four letters).** It is neither an invertible element nor a zero divisor, so a degenerate biquaternion is not the same object as a zero divisor for any letter. The $N$ case is the closest, its set being the origin together with the zero divisors.

**Remark (the unqualified words).** **Regular** without a letter is **spectrally regular**, $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}\neq0$, and **degenerate** without a letter is **spectrally degenerate**, $B^{2}=0$. The letter is never omitted when the four norms are meant, because the spectral condition and the norm condition are independent.

**The four regular sets.** The $P$-regular set is the complement of the complex cone, open and dense, and it is not a group, since $(e_t+i\vec e_x)(e_t-i\vec e_x)=0$ with both factors $P$-regular of value $2$. The $\natural$-regular set is the group of invertibles, open and dense and a group. The $H$-regular set is $\mathbb{B}\setminus\{0\}$, open and dense, and not a group, since it contains the zero divisors. The $\mathrm{Kr}$-regular set is the complement of $\mathcal K$, open and dense with exactly two connected components, the positive and the negative region, and it is not a group, since it contains an invertible element on each side and the product of one of each crosses the cone.

## The Four Forms on the Two Sectors

**The two sectors are the two eigenspaces of the adjoint.** The adjoint ${}^{*}$ is an involution, so its eigenvalues are $+1$ and $-1$, and the two eigenspaces are the sectors. The **material sector** $\mathbb{B}_\Phi$ is the anti-Hermitian subspace, $\tilde Q^{*}=-\tilde Q$, so the scalar coordinate is imaginary and the three vector coordinates are real,

$$
\tilde R_\Phi=i q'_t e_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z,\qquad q'_t,q_x,q_y,q_z\in\mathbb{R}.
$$

The **informational sector** $\mathbb{B}_\Psi$ is the Hermitian subspace, $\tilde Q^{*}=\tilde Q$, so the scalar coordinate is real and the three vector coordinates are imaginary,

$$
\tilde H_\Psi=q_te_t+i\bigl(q'_x\vec e_x+q'_y\vec e_y+q'_z\vec e_z\bigr),\qquad q_t,q'_x,q'_y,q'_z\in\mathbb{R}.
$$

**On each sector the four forms coincide in pairs, with a sign.**

$$
P=-H,\qquad \mathrm{Kr}=-N\quad\text{on }\mathbb{B}_\Phi;\qquad
P=H,\qquad \mathrm{Kr}=N\quad\text{on }\mathbb{B}_\Psi.
$$

*Proof.* On $\mathbb{B}_\Phi$ the coefficients satisfy $\overline{Q_\mu}=-\varepsilon_\mu Q_\mu$, so $\lvert Q_\mu\rvert^{2}=-Q_\mu^{2}$ and each sesquilinear coordinate term is the negative of the bilinear one; on $\mathbb{B}_\Psi$ the relation is $\overline{Q_\mu}=\varepsilon_\mu Q_\mu$, and the two agree. The identities are read term by term in the formulas of the four norms above.

**The identities are statements about forms.** They do not say that the four products agree on a sector; the products are the subject of the previous entry, and they do not.

**The inertia of each restriction follows at once.**

| sector | $P$ | $N$ | $H$ | $\mathrm{Kr}$ |
|---|---|---|---|---|
| $\mathbb{B}_\Phi$, the material sector | $(0,4)$ | $(3,1)$ | $(4,0)$ | $(1,3)$ |
| $\mathbb{B}_\Psi$, the informational sector | $(4,0)$ | $(1,3)$ | $(4,0)$ | $(1,3)$ |

*Proof.* On $\mathbb{B}_\Phi$ the quaternionic norm is $N=-{q'_t}^{2}+q_x^{2}+q_y^{2}+q_z^{2}$, one negative direction and three positive ones; the plain norm is its negative, the Hermitian norm is the sum of the four squares, and the Krein norm is ${q'_t}^{2}-q_x^{2}-q_y^{2}-q_z^{2}$. On $\mathbb{B}_\Psi$ the quaternionic norm is $N={q_t}^{2}-{q'_x}^{2}-{q'_y}^{2}-{q'_z}^{2}$, and the other three follow by the identities above.

**On the six remarkable subspaces the division is sharper.** The Krein form is positive definite, $(2,0)$, on the centre and negative definite, $(0,6)$, on the vector subspace. The two bilinear forms are $(1,1)$ on the centre and $(3,3)$ on the vector subspace. The Hermitian form is definite on all six. The restriction table of *Remarkable Subspaces and the Four General Products, Forms and Norms* carries the whole list.

## The Alternating Companion of the Two Sesquilinear Forms

**The imaginary part of a sesquilinear form is an alternating form.** Write $\omega(\tilde X,\tilde Y)=\operatorname{Im}H(\tilde X,\tilde Y)$. Since $H$ is Hermitian, $\overline{H(\tilde X,\tilde Y)}=H(\tilde Y,\tilde X)$, so $\omega$ is real-valued and alternating, $\omega(\tilde X,\tilde X)=0$.

**The identity that governs it is one line.** The central $i$ is complex-linear and $(i\tilde Y)^{*}=-i\tilde Y^{*}$, so $H(\tilde X,i\tilde Y)=-iH(\tilde X,\tilde Y)$ and $H(i\tilde X,\tilde Y)=iH(\tilde X,\tilde Y)$. Taking imaginary parts,

$$
\omega(i\tilde X,\tilde Y)=\operatorname{Re}H(\tilde X,\tilde Y).
$$

The alternating companion is the symmetric form with one argument turned by a quarter turn, and it is nothing else.

**Its rank on the six subspaces is $2$, $6$ and four zeros.**

| subspace | $\dim_{\mathbb{R}}$ | $\operatorname{rank}\omega$ |
|---|---|---|
| $\mathbb{B}_C$, the centre | $2$ | $2$ |
| $\mathbb{B}_V$ | $6$ | $6$ |
| $\mathbb{B}_H$ | $4$ | $0$ |
| $\mathbb{B}_{iH}$ | $4$ | $0$ |
| $\mathbb{B}_\Psi$ | $4$ | $0$ |
| $\mathbb{B}_\Phi$ | $4$ | $0$ |

**Both halves of the table follow from the identity.** On a subspace stable under multiplication by $i$ one has $iU=U$, so if $\omega(\tilde X,\cdot)$ vanishes on $U$ then $\operatorname{Re}H(\tilde X,\cdot)$ vanishes on $U$, and $\operatorname{Re}H$ is positive definite, hence $\tilde X=0$: the companion is non-degenerate there. On a real-type subspace the Hermitian form is real-valued, since that subspace is the fixed space of an involution under which $H$ is conjugate-symmetric, so its imaginary part vanishes identically. The complex subspaces are exactly the stable ones.

**The companion of the Krein form does the same.** Replacing $H$ by $\mathrm{Kr}$ gives an alternating form of the same ranks, $2$ and $6$ on the complex subspaces and zero on the four real-type ones. The two companions differ in value and not in where they live.

## The Physical Interpretation

### I.7.a — A Form of Two Elements Is an Amplitude, and Its Diagonal Is a Number

**Read:** the four forms take two elements and return a scalar, and the four norms are those forms at two equal arguments.

**The two arities do different work in a theory.** A function of two elements is what a theory evaluates on a pair: a transition, an overlap, an expectation. A function of one element is what a theory reads off a single object: a size, a mass, a normalisation. The algebra supplies both from one letter, and the passage between them is the diagonal.

**The diagonal is not a lossless restriction.** The form knows the pair, and the norm knows one element. A form that vanishes on the diagonal can be non-zero off it: on the Krein cone $\mathrm{Kr}(\tilde Q)=0$ for every element of the cone, while $\mathrm{Kr}(\tilde Q_1,\tilde Q_2)$ is non-zero for a generic pair drawn from it. A formalism that uses one word for the two arities is using one symbol for two functions.

**The boundary.** The reading is not the claim that every pairing is an amplitude. It is the claim that the arity is a real distinction, that the algebra carries it, and that a law proved at one arity does not transfer to the other.

### I.7.b — The Pairing Is the Sign of the Sector

**Read:** the plain form is complex-valued, and on the two sectors it is minus the Hermitian norm and plus it.

$$
P(\tilde R_\Phi)=-\bigl({q'_t}^{2}+q_x^{2}+q_y^{2}+q_z^{2}\bigr)<0,\qquad
P(\tilde H_\Psi)={q_t}^{2}+{q'_x}^{2}+{q'_y}^{2}+{q'_z}^{2}>0.
$$

**A pairing may be complex, and a measure must be real.** The two forms with the star in the second slot have real values; the two without it have complex values. That division is the second slot and not a convention.

**So the plain form is a flag and not a metric.** It says which half an element belongs to, and it measures neither half: it is minus the Euclidean square on the material side and plus it on the informational side. Its sign is the sector, and its modulus is the Hermitian norm.

**The pairing also crosses the split.** For one element of each sector the scalar part is purely imaginary,

$$
\mathrm{Sc}(\tilde R_\Phi\tilde H_\Psi)=i\bigl(q'_tq_t-(\vec q,\vec q')\bigr),
$$

the Minkowski pairing of the two four-vectors multiplied by $i$, with $\vec q$ and $\vec q'$ the spatial parts of the two elements. The quaternionic form of the same two elements is $i\bigl(q'_tq_t+(\vec q,\vec q')\bigr)$, and the difference is the sign of the spatial term, which is the first slot.

**The sharpest warrant for the word *flag* is one comparison.** $P(e_t+\vec e_x)=0$ on an invertible element, and $P(e_t+i\vec e_x)=2$ on a zero divisor. A function that vanishes on an invertible element and does not vanish on a non-invertible one decides no invertibility, so it cannot be the measure of a theory of reversible operations.

**The boundary.** The complex cone is not the light cone and not the zero-divisor cone. It is a six-dimensional quadric over the complex numbers that cuts across the invertibles and the non-invertibles alike, and no physical set is its image.

### I.7.c — The Weight Is the Only Measure That Can Be Normalised

**Read:** the Hermitian norm is positive definite, $H(\tilde Q)>0$ for $\tilde Q\neq0$, of inertia $(8,0)$ on the real algebra, and its square root is the Euclidean norm.

**A probability needs a positive number that can be divided by its total.** A state needs a sphere to live on. A limit needs a topology. The three requirements are one requirement, and the Hermitian norm is the only one of the four that meets it: a norm of the coefficient space gives distance, balls, convergence, bounded operators and a completion.

**The measure is blind to the sector, and that blindness is exact.** $H$ is the same sum of four squared moduli on both sectors, while the plain form changes sign from one to the other. A material element and an informational element of the same coordinate moduli have the same weight, and the difference between them is a difference of a bilinear form and not of a measure. This is the precise content of the rule that the sesquilinear layer does not carry the sector.

**The form supplies the weight and not the state.** A pure state is a minimal Hermitian idempotent, and the weight pairs a state with an observable and returns a number. The state carries an axis and no phase, and the phase is not a value of $H$.

**The boundary.** That the definite Hermitian form is physical probability is the hypothesis of the informational sector and not a theorem of the algebra. The algebra proves that a definite pairing exists, that it is unique among the four, and that its square root is the topological norm.

### I.7.d — The Interval Is the Only Measure That Survives a Product

**Read:** the quaternionic norm is multiplicative, $N(\tilde Q_1\tilde Q_2)=N(\tilde Q_1)N(\tilde Q_2)$, and its level set $1$ is a group.

**Multiplicativity is a law of composition, and it has immediate consequences.** The value of a composite is the product of the values; the invertibles, the zero divisors and the null set are each closed under multiplication; and the level set $N=1$ is a group with the inverse $\tilde Q^{\natural}/N(\tilde Q)$. A theory that composes operations and asks for an invariant of the composite has one candidate among the four, and the candidate is the quaternionic norm.

**The other three are destroyed by composition.** The weight of a product is not the product of the weights, and the plain norm of a product is not the product of the plain norms; one substitution each settles it, as in §*What the Four Norms Separate*. The multiplicative reader is therefore the only one that can be transported along a process.

**The inverse is the geometric content of the law.** The formula $\tilde Q^{-1}=\tilde Q^{\natural}/N(\tilde Q)$ says that the quaternion conjugation supplies the direction and the norm supplies the scale. An element of norm zero has no scale to divide by, and that element is the zero divisor.

**On the material sector the same number is the interval.**

$$
N(\tilde R_\Phi)=-{q'_t}^{2}+q_x^{2}+q_y^{2}+q_z^{2},
$$

of inertia $(3,1)$, with the null cone as its zero set and the hyperboloids $N=-m^{2}c^{2}$ as its level sets. One function, two readings: a scale on the algebra, an interval on the sector.

**The boundary.** The interval is real on the four-dimensional real-type subspaces and complex on the centre and the vector subspace. The mass shell is a level set on a sector, and it is not a value of the form on the algebra.

### I.7.e — The Interval Is a Pair of Counts, Not a Letter

**Read:** the letter that carries the interval is decided by the imaginary unit, and the arithmetic is one line.

**A norm written $\sum_\mu Q_\mu^{2}$ gives a plus for a real coordinate and a minus for an imaginary one.** In $\mathbb{B}_\Phi$ the scalar coordinate is imaginary and the three vector coordinates are real, so $N=-{q'_t}^{2}+q_x^{2}+q_y^{2}+q_z^{2}$: one time direction and three space directions. In $\mathbb{B}_\Psi$ the three vector coordinates are imaginary and the scalar one is real, so $N={q_t}^{2}-{q'_x}^{2}-{q'_y}^{2}-{q'_z}^{2}$: the same split with the other sign. On the real quaternions no coordinate is imaginary, $\sum_\mu Q_\mu^{2}$ is a sum of four squares, and the minus must come from the sign data of the plain form, $P=t^{2}-q_x^{2}-q_y^{2}-q_z^{2}$.

**The interval is a pair of counts and the alphabet is a convention.** A theory that puts its spacetime in the material sector reads the interval off the quaternionic norm. A theory that works on the real grade reads the same interval off the plain norm. The two are not two metrics: one is $\sum_\mu Q_\mu^{2}$ on a slice with an imaginary time coordinate, and the other is the sign data of the plain form on a slice with none.

**Multiplication by the central $i$ exchanges the sectors and reverses the two bilinear norms.**

$$
i\mathbb{B}_\Phi=\mathbb{B}_\Psi,\qquad
P(i\tilde Q)=-P(\tilde Q),\qquad
N(i\tilde Q)=-N(\tilde Q),\qquad
H(i\tilde Q)=H(\tilde Q),\qquad
\mathrm{Kr}(i\tilde Q)=\mathrm{Kr}(\tilde Q).
$$

**So the imaginary unit flips the two complex measures and is invisible to the two real ones.** The interval of the material sector and the interval of the informational sector are one form read with opposite values, and the two real measures cannot tell the sectors apart.

**The double bookkeeping is where a sign is lost in print.** On the material sector $P=-H$ and $\mathrm{Kr}=-N$, so each measure is minus its partner there; a sign dropped in that bookkeeping turns a metric into a weight without changing a symbol.

**The boundary.** The observation is about inertias on real subspaces. On the whole algebra over $\mathbb{C}$ both bilinear forms are neutral, of inertia $(4,4)$, and the interval of a sector is a restriction and not a global object.

### I.7.f — The Mass Shell Is a Level Set

**Read:** on the material sector the quaternionic norm is $-{q'_t}^{2}+q_x^{2}+q_y^{2}+q_z^{2}$, so the level set $N=-m^{2}c^{2}$ is the hyperboloid of the four-vectors of mass $m$.

**The level set is the whole of what the norm says about the mass.** It fixes no value, since the value is the label of the level set, and it fixes no spin, no charge and no multiplicity.

**The norm and the spectrum answer different questions.** The spectrum of the previous entry is the pair of spectral values $Q_t\pm iB$, and their product is the quaternionic norm,

$$
(Q_t+iB)(Q_t-iB)=Q_t^{2}+B^{2}=N(\tilde Q).
$$

So the mass shell is a level set of a symmetric function of the two spectral values, and it is not a third object beside them. The mass is the value of that product on the sector.

**The reading also fixes what the other three cannot do.** The weight says nothing about the cone. The plain and the Krein norms vanish on invertible elements, so they say nothing about the boundary of the reversible region. Only the quaternionic norm carries both the cone and the value.

**The boundary.** The mass shell is a level set of a form on a sector. The entry derives no mass spectrum, no mass ratio and no quantisation of the level sets.

### I.7.g — The Volume Is a Signed Content

**Read:** the Krein norm is real and indefinite, of inertia $(2,6)$ on the algebra, and it is the difference of the two contents of the centre–vector split.

**The reading is a signed content.** The Hermitian norm adds the squared moduli of the coordinates; the Krein norm adds them with a minus on the three vector coordinates. The first counts the content of the element, the second counts the difference between its temporal content and its spatial content, and the surface where the two balance is the cone $\mathcal K=\{\lvert Q_t\rvert=\lvert\vec Q\rvert\}$, of real dimension seven.

**Only one of the two real measures is signed, and that is the whole of the name.** A weight is a content and has no sign problem. A signed content is a volume with an orientation, and its sign says which side of the cone the element is on.

**The indefinite form normalises nothing, and the geometry shows it.** The level sets are not spheres but hyperboloids, and they split into two components of different topology, the set $\{\mathrm{Kr}=1\}$ homeomorphic to $S^{1}\times\mathbb{R}^{6}$ and the set $\{\mathrm{Kr}=-1\}$ homeomorphic to $\mathbb{R}^{2}\times S^{5}$.

**The reading is a constraint and not a state.** A calibration distinguishes two kinds of direction and leaves the normalisation to a choice; it does not prepare a state, and its form is the form of that freedom. A definite form counts states, and an indefinite one counts a constraint.

**The fundamental symmetry makes the reading consistent.** The quaternion conjugation is an isometry of the Krein form, and its eigenspaces are the centre and the vector subspace, of complex dimensions one and three, on which the sign is opposite. So

$$
\mathrm{Kr}(\tilde Q_1,\tilde Q_2)=H\bigl(\tilde Q_1^{\natural},\tilde Q_2\bigr),
$$

and the signed measure is the weight with the quaternion conjugate inserted in the first slot. That is the exact sense in which an indefinite geometry is a definite one with a chosen conjugation. The conjugation is ${}^{\natural}$ and not multiplication by the central $i$, which has order four.

**The boundary.** The form is a form. It derives no gauge group, no coupling and no field content, and the cone $\mathcal K$ is not the zero-divisor cone.

### I.7.h — No Function Is Both a Mass and a Probability

**Read:** no function on the algebra that vanishes at the origin is both definite and multiplicative.

**The proof is one line and it is the whole reading.** The element $z_+=e_t+i\vec e_x$ and its partner $z_-=e_t-i\vec e_x$ are non-zero, and their product is zero. So a multiplicative function $g$ vanishing at the origin gives $g(z_+)g(z_-)=0$. One factor vanishes on a non-zero element, and a definite function cannot vanish there.

**A theory of one algebra therefore needs two different norms.** The interval is the measure that survives composition, and it vanishes on the null cone. The weight is the measure that never vanishes, and it is destroyed by composition. A formalism that wants both a causal structure and a probability has to carry both, and it cannot identify them.

**This is also the precise reason the biquaternions are not a normed division algebra.** In $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ and $\mathbb{O}$ the two senses coincide because there are no zero divisors. The complexification creates them, and the two senses separate.

**The obstruction is not non-commutativity.** The quaternions are non-commutative, and $q\bar q$ is definite and multiplicative. The dual numbers are commutative, and they admit no definite multiplicative function. The obstruction is the zero divisor, and the zero divisors come from the complexification.

**The boundary.** The proposition is about functions on the algebra and not about physical quantities. That the interval is the mass and the weight is the probability is the dictionary of the sector; the impossibility of one function being both is the algebra's.

### I.7.i — The Group Is the Measure

**Read:** the four isometry groups are $O_4(\mathbb{C})$, $O_4(\mathbb{C})$, $\mathrm{U}(4)$ and $\mathrm{U}(1,3)$, of real dimensions $12$, $12$, $16$ and $16$.

**A measure is known by what preserves it, and the two properties that matter physically are compactness and inertia.** The unitary group $\mathrm{U}(4)$ is compact; the indefinite unitary group $\mathrm{U}(1,3)$ is not; the complex orthogonal group is complex and imposes no reality condition.

**Compactness is the difference between a probability theory and an indefinite one.** A compact group has a finite invariant volume and a discrete set of representations. A non-compact one has neither, and it keeps a distinguished time direction instead. The passage from $\mathrm{U}(4)$ to $\mathrm{U}(1,3)$ is the passage from a state space to a constrained one, and it is decided by the sign data and by nothing else.

**The two bilinear forms share their group, and that sharing is a fact about $\mathbb{C}$.** The substitution $\vec Q\mapsto i\vec Q$ carries one form into the other, so the two bilinear measures are one measure in two coordinate systems. Over $\mathbb{R}$ that substitution is unavailable, and the two real specialisations of the four are different groups, $O(1,3)$ and $O(4)$.

**On the material sector the isometry group of the interval is the Lorentz group.** The statement is a restriction statement: it is the group of the quaternionic form on the sector, not of the quaternionic form on the algebra, and the two differ.

**The boundary.** A group of a form is not a gauge group of a theory. The entry does not claim that the gauge group of a physical model is one of the four. It claims that a measure determines its own isometries, and that those are the group a theory must respect if it uses that measure.

### I.7.j — The Fundamental Symmetry Is Invisible to All Four

**Read:** the quaternion conjugation preserves each of the four forms, so every one of the four norms takes the same value on $\tilde Q$ and on $\tilde Q^{\natural}$.

**No measure distinguishes an element from its quaternion conjugate.** The reason is that ${}^{\natural}$ is an involution and an anti-automorphism, so the scalar part of the conjugated product equals the scalar part of the original one, and the same computation with a star in the second slot gives the two sesquilinear forms.

**The physical interpretation is that the discrete operation is invisible to every measure and visible in the pairing.** A norm is unchanged by ${}^{\natural}$, because the conjugation reverses the sign of the vector part and a norm squares it away. A discrete symmetry of this kind cannot be detected by a mass or a weight, and it shows up only in a quantity that is odd in the vector part, a bracket or the orientation of a frame.

**The same involution is what makes the indefinite form usable.** It is the fundamental symmetry of the Krein form, the operator that turns it into the Hermitian one, so it is at once the symmetry of the four measures and the tool that converts the signed one into the positive one.

**The boundary.** That a measure is blind to ${}^{\natural}$ does not make ${}^{\natural}$ a physical symmetry. It states that the four measures cannot witness it, and it locates the witness elsewhere.

### I.7.k — Four Cones, and Only One Is the Wall

**Read:** the four norms have four different zero sets, of real dimensions $6$, $6$, $0$ and $7$.

**Only the quaternionic one is the set of the non-invertibles, and the others vanish on invertible elements.**

$$
\{N=0\}=\{0\}\cup\mathcal Z,\qquad
P(e_t+\vec e_x)=0,\qquad \mathrm{Kr}(e_t+\vec e_x)=0,\qquad \{H=0\}=\{0\}.
$$

**Reversibility has exactly one measure.** The wall of the reversible region is the zero set of the quaternionic norm, and no other norm draws it. A theory that wants a cone of reversibility, a horizon of invertibility or a massless boundary must use the quaternionic norm. A theory that uses the plain or the Krein norm draws a cone that contains invertible elements and therefore cuts through the reversible region.

**The light cone is a cut and not a null set.** The light cone is $\mathcal N\cap\mathbb{B}_\Phi$, and the two objects are different: the null set on the algebra is six-dimensional and contains elements of both sectors, while the light cone is its intersection with a four-dimensional slice.

**The two cones that are easy to confuse are the zero-divisor cone and the Krein cone.** They have dimensions six and seven, they are both real and both invariant, but the Krein cone contains invertible elements and the zero-divisor cone does not, so a statement about one is not a statement about the other.

**The boundary.** A zero set is a set. The entry does not claim that every element of the wall is a physical light ray, and it does not derive the signs from the cone; the direction is the other way.

### I.7.l — The Area Belongs to the Complex Subspaces

**Read:** the alternating companion is non-degenerate on the centre and on the vector subspace, of ranks $2$ and $6$, and it vanishes on the four real-type subspaces.

**The division of labour is between two questions.** The complex subspaces carry the area: the companion pairs the two times of the centre, and each material direction with its informational partner in the vector subspace. The four real-type subspaces carry the metric and the probability, which are symmetric, and no area. *How much* and *how much turns* are two questions, and they are asked on two different subspaces.

**The reason is the identity and not the naming.** The identity $\omega(i\tilde X,\tilde Y)=\operatorname{Re}H(\tilde X,\tilde Y)$ says that the area is the metric with one argument turned by a quarter turn. Where multiplication by the central $i$ stays inside the subspace the turn stays inside too, so no direction of the subspace is invisible to the companion. On a real-type subspace the Hermitian form is real-valued, and a real form has no imaginary part to give.

**The boundary.** A subspace without an area pairing is not a subspace without an antisymmetric structure: the commutator is antisymmetric and does not vanish on a sector. The vanishing stated here concerns the scalar-valued alternating part of the two sesquilinear forms, and nothing else. The area also adds no dynamics; it is a property of the restriction of a form, and it supplies neither a Hamiltonian nor a quantisation.

## The Limits

**The four words are a naming and not a theorem.** The algebra proves that four forms exist, that they are distinct, that their inertias are $(4,4)$, $(4,4)$, $(8,0)$ and $(2,6)$, that one of them is multiplicative and another definite, and that no function is both. It does not prove that these are the four quantities a physical theory evaluates.

**Three levels of inertia are kept apart throughout.** The values on a basis, a realified inertia and a restricted inertia are three statements about the same form, and the entry names the level whenever an inertia is quoted. The interval of a physical sector is a restriction.

**Two senses of norm are kept apart.** The algebraic norm is a map into the ring, complex for the two bilinear forms and real for the two sesquilinear ones; the topological norm is the one positive square root, $\lVert\tilde Q\rVert^{2}=H(\tilde Q)$. A norm is not a distance until a positivity is declared.

**The coincidences on the sectors are statements about forms.** The identities $P=\pm H$ and $\mathrm{Kr}=\pm N$ on a sector do not make the four products agree there, and they do not make the Krein form a probability or the plain form an interval.

**The entry states no dynamics, no mass value, no gauge group and no state space.** The mass shell is a level set; the interval is a metric and not an equation of motion; the volume is a signed content and not a field; the area is a restriction of a form and not a Hamiltonian.

**The four cuts are four and not one.** A degenerate biquaternion is not the same object as a zero divisor for any letter. Only the quaternionic cut coincides with the non-invertibles, and only off the origin.

## Summary

- A form is the scalar part of a product, and an algebraic norm is that form at two equal arguments; one letter serves the two arities, and the two arities obey different laws.
- The twelve operations carry four forms and no more: the symmetrisation keeps the scalar part of its family and the antisymmetrisation kills it, so the four general products and their symmetric parts carry the four forms two by two and the four antisymmetric parts carry the zero form.
- The four forms are $P=\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, $N=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)$, $H=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ and $\mathrm{Kr}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})$, with the values on a basis $\mathrm E$, $\mathrm I_4$, $\mathrm I_4$ and $\mathrm E$ and the realified inertias $(4,4)$, $(4,4)$, $(8,0)$ and $(2,6)$.
- The second slot decides whether the value is complex or real, and with it whether the form can supply a measure. The first slot decides the signs on the basis, the inertia and the definiteness on each subspace. The two divisions are independent, and their product is the four.
- Every one of the four is the plain form with a conjugation inserted in one slot or in both; the two real forms are those whose second slot is an adjoint.
- Read on the diagonal, the four forms give the four norms $\langle\tilde Q\rangle=\sum_\mu\varepsilon_\mu Q_\mu^{2}$, $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$, $\langle\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ and $\langle\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$, each attained by two operations, the general product and the symmetrisation of its family.
- The quaternionic norm is the multiplicative one. Multiplicativity is proved from Lagrange's identity on the cross product, with the inverse $\tilde Q^{\natural}/N(\tilde Q)$ and the criterion of invertibility.
- The Hermitian norm is the definite one, and its square root is the only topological norm. The plain and the Krein norms are the two indefinite remainders, one complex and one real.
- No function is both definite and multiplicative, and the zero divisors are the reason. The split is the failure of the biquaternions to be a normed division algebra, and the obstruction is the zero divisor and not the failure of commutativity.
- Each letter gives a qualified pair: a biquaternion is regular for $P$, $\natural$, $H$ or $\mathrm{Kr}$ when the value is non-zero, and degenerate when it is zero. Only the quaternionic pair is the partition into invertibles and non-invertibles; the plain and the Krein cuts vanish on invertible elements, and the Hermitian cut is the origin alone.
- On the material sector the four restrictions are $(0,4)$, $(3,1)$, $(4,0)$ and $(1,3)$, and on the informational sector they are $(4,0)$, $(1,3)$, $(4,0)$ and $(1,3)$, with $P=-H$ and $\mathrm{Kr}=-N$ on the first and $P=H$ and $\mathrm{Kr}=N$ on the second.
- The four isometry groups are $O_4(\mathbb{C})$, $O_4(\mathbb{C})$, $\mathrm{U}(4)$ and $\mathrm{U}(1,3)$, of real dimensions $12$, $12$, $16$ and $16$, and the quaternion conjugation lies in all four.
- The interval is a pair of counts and not a letter: it is the plain norm, of inertia $(1,3)$, on the real quaternions and the quaternionic norm, of inertia $(3,1)$, on the material sector, because $\sum_\mu Q_\mu^{2}$ takes a minus from an imaginary coordinate while the plain norm takes it from the sign data.
- Multiplication by the central $i$ exchanges the two sectors and reverses both bilinear norms while leaving both real measures unchanged.
- On real coefficients the four collapse to two, $P=\mathrm{Kr}$ and $N=H$, so a real computation cannot tell the plain pairing from the signed content, nor the quaternionic norm from the Hermitian one.
- The imaginary part of a sesquilinear form is an alternating form: it is non-degenerate on the two complex subspaces, of ranks $2$ and $6$, and it vanishes on the four real-type ones.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde Q_1,\tilde Q_2\rangle$, $P$ | the plain form, $\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, symmetric, values on a basis $\mathrm E$, inertia $(4,4)$ |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$, $N$ | the quaternionic form, the interval, $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)$, inertia $(4,4)$ |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*}$, $H$ | the Hermitian form, the weight, $\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$, inertia $(8,0)$ |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$, $\mathrm{Kr}$ | the Krein form, the volume, $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})$, inertia $(2,6)$ |
| $\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}\bigl(K_1(\tilde Q_1)K_2(\tilde Q_2)\bigr)$, $\langle\tilde Q\rangle=\langle\tilde Q,\tilde Q\rangle$ | one expression, two arities: two arguments give the form, one gives the algebraic norm; $K_1$ is the identity or ${}^{\natural}$, $K_2$ the identity or ${}^{*}$ |
| $\varepsilon=(1,-1,-1,-1)$ | the sign vector of the quaternion conjugation, which the first slot applies |
| $\mathrm E$, $\mathrm I_4$ | the two sets of values on a basis; $\mathrm E$ carries the signs, $\mathrm I_4$ the plus signs |
| $P(\tilde Q)$, $N(\tilde Q)$, $H(\tilde Q)$, $\mathrm{Kr}(\tilde Q)$ | the four norms, with values in $\mathbb{C}$, $\mathbb{C}$, $\mathbb{R}$, $\mathbb{R}$ |
| $(4,4)$, $(4,4)$, $(8,0)$, $(2,6)$ | the realified inertias of the four norms |
| $\mathcal N$, $\mathcal K$, the complex cone | the null sets of $N$, of $\mathrm{Kr}$ and of $P$; that of $H$ is $\{0\}$ |
| regular for a letter, degenerate for a letter | the value under $P$, $N$, $H$ or $\mathrm{Kr}$ is non-zero, respectively zero; only the $N$ pair is the partition into invertibles and non-invertibles |
| $O_4(\mathbb{C})$, $\mathrm{U}(4)$, $\mathrm{U}(1,3)$ | the isometry groups, of real dimensions $12$, $16$ and $16$ |
| $\omega(\tilde X,\tilde Y)$ | the alternating companion, $\operatorname{Im}H$, of ranks $2$ and $6$ on the complex subspaces and $0$ on the four real-type ones |
| $z_\pm=e_t\pm i\vec e_x$ | the pair of zero divisors, $z_+z_-=0$ |
| $\tilde R_\Phi$, $\tilde H_\Psi$ | a material element, $i q'_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$, and an informational element, $q_te_t+i(q'_x\vec e_x+q'_y\vec e_y+q'_z\vec e_z)$ |
| $\lVert\tilde Q\rVert$ | the topological norm, $H(\tilde Q)^{1/2}$ |
| $\mathcal Z$ | the zero divisors; $\{N=0\}=\{0\}\cup\mathcal Z$ |

## Further Reading

**In the mathematics corpus.** The nine articles of the source table, and inside the first of them the sections *The Four Forms*, which owns the brackets and the isometry groups; *The Four Algebraic Norms*, which owns the coordinates of the four; *What the Four Algebraic Norms Separate*, which owns the proposition that no function is both and the refutation of each of the other three; and *Commutativity, Multiplicativity and Definiteness*, which owns the correction of the common paraphrase.

**In this category.** [The Four Products: Composition, Probability, Causality and Gauge](the-four-products-composition-probability-causality-and-gauge.html) supplies the products whose scalar parts the four forms are. [The Spectrum and the Two Modes](the-spectrum-and-the-two-modes.html) supplies the two spectral values whose product is the quaternionic norm. [The Two Sectors: Split and the Four Bridges](the-two-sectors-split-and-the-four-bridges.html) supplies the restriction table and the cross-sector pairing.

**The sources of this entry.** [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](../articles_maths/the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html) is the mathematical treatment of the same four letters. [The K Norm and the Indefinite Structure](the-k-norm-and-the-indefinite-structure.html) is the indefinite geometry at large. [States, Observables and the Born Weight](states-observables-and-the-born-weight.html) is the weight read as a probability. [The Partition: Two Invariants and Four Regimes](the-partition-two-invariants-and-four-regimes.html) is the invertibility cut. [The Group of Invertibles, the Cone and the Orders](the-group-of-invertibles-the-cone-and-the-orders.html) is the cone as a physical boundary.
