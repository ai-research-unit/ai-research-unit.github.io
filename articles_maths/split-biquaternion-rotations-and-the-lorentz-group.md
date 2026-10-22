
# __Split-Biquaternion Rotations and the Lorentz Group__

## Introduction

This article is the rotation slot of the split biquaternion system. It determines which Lorentzian geometry the algebra $\mathbb{H}_{\mathbb{D}}$ carries, identifies the isometry groups of the quadratic forms that the algebra presents, and describes how much of those isometry groups the algebra itself realises. The **Lorentz group** is used here in its mathematical sense throughout: it is the isometry group of a non-degenerate symmetric bilinear form of signature $(3,1)$ on a real vector space of dimension four. Nothing physical is attached to the word; it names a position in the classification of forms, and the companion statements about forms of signature $(2,2)$ are made in the same spirit. The two-dimensional model, where the corresponding group is the hyperbolic rotation group of the split complex numbers, is the article *The Three Two-Dimensional Algebras and the Three Kinds of Rotation*, and the general theory of forms of indefinite signature, of their isometry groups and of the geometry they define is the article *Pseudo-Riemannian and Lorentzian Geometry* in Part II, written in parallel; both are cited rather than reproduced.

The article assumes the split biquaternion algebra from *Split-Biquaternion Algebra*: $\mathbb{H}_{\mathbb{D}} = \mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}$, of real dimension eight, with the four conjugations ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$ and ${}^{\flat} = -{}^{*}$, with the idempotents $\tilde\Pi_{1,2} = \tfrac{1}{2}(1\pm j)$ and the isomorphism $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$. It assumes the split-biquaternion norm $\langle\tilde Q\rangle_{\natural} = \tilde Q\tilde{Q}^{\natural}$ and the theory of its invertibility from *Split-Biquaternion Norm and Invertibility*, the description of the zero divisors from *Split-Biquaternion Zero Divisors*, the classification of the roots of $-e_t$ from *Split-Biquaternion Roots of Minus One*. It uses the hyperbolic rotations of the split complex plane from *Hyperbolic Rotations*, and the quaternion rotation theory — the double cover $Sp(1)\to SO(3)$ and the two-sided action giving $SO(4)$ — from *Quaternion Rotations and Reflections*. It does not restate any of them; the rotation theory of the quaternions is used only as the compact model against which the split biquaternion case is compared. The Lie algebra $\mathrm{SO}(3,1)$ and its complexification are treated in *The Orthogonal Lie Algebra* in Part I, where the isomorphism $\mathrm{SO}(1,3)\cong\mathrm{SL}_2(\mathbb{C})$ is established.

The article follows the shared conventions. The quaternion basis is $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ with $\vec e_k^2 = -e_t$ and $\vec e_x\vec e_y = \vec e_z$; the split complex unit is $j$ with $j^2 = +e_t$, commuting with every $\vec e_k$; a split biquaternion is $\tilde Q = \sum_{\mu\in\{t,x,y,z\}}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{D}$, written $\tilde Q = a + jb$ with $a, b\in\mathbb{H}$ and, equivalently, $\tilde Q = \tilde Q_+\tilde\Pi_1 + \tilde Q_-\tilde\Pi_2$ with $\tilde Q_{\pm}\in\mathbb{H}$. The Hermitian conjugation is $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$, and the four invariant subspaces are as in *Split-Biquaternion Algebra*.

## The Lorentz Group as an Isometry Group

### The Definition

**Definition.** Let $V$ be a real vector space and let $g$ be a non-degenerate symmetric bilinear form on $V$. Write $(n,m)$ for its **signature**, where $n$ is the number of positive and $m$ the number of negative entries in a diagonalisation; the dimension of $V$ is $N = n+m$. The **orthogonal group** $O(n,m)$ is the group of linear isomorphisms $T$ of $V$ with

$$
g(T\mathbf{Q}, T\mathbf{P}) = g(\mathbf{Q},\mathbf{P}) \qquad\text{for all } \mathbf{Q}, \mathbf{P}\in V .
$$

When $(n,m) = (3,1)$ the group $O(3,1)$ is called the **Lorentz group**, and the form a **Lorentzian form**; when $(n,m) = (2,2)$ the group is written $O(2,2)$ and the form is called **neutral** or **of Kleinian signature**.

**Proposition.** For every non-degenerate symmetric form the group $O(n,m)$ is a closed subgroup of $GL_n(\mathbb{R})$, hence a Lie group; it contains the finite central subgroup $\{\pm 1\}$; its Lie algebra is

$$
\mathrm{SO}(n,m) = \{X\in\mathrm{GL}_n(\mathbb{R}) : g(X\mathbf{Q},\mathbf{P}) + g(\mathbf{Q},X\mathbf{P}) = 0\ \text{for all } \mathbf{Q},\mathbf{P}\},
$$

of dimension $\tfrac{1}{2}\langle N-1\rangle_{\natural}$; and its identity component has index at most four in it.

*Proof.* Closure is continuity of the defining equations. The differential condition is obtained by differentiating $g(\exp(tX)\mathbf{Q}, \exp(tX)\mathbf{P}) = g(\mathbf{Q},\mathbf{P})$ at $t = 0$. The dimension is the dimension of the space of $g$-skew endomorphisms, which is $\tfrac{1}{2}\langle N-1\rangle_{\natural}$ because $g$ identifies $V$ with $V^{*}$ and skewness is a condition of that dimension. The four components are separated by the sign of the determinant and by the sign of the restriction of the form to the invariant subspace on which it is definite; for a Lorentzian form the invariant is $\det T$ together with the sign of $g(Tu,u)$ for one timelike $u$.

### The Groups $O(3,1)$, $SO(3,1)$ and $SO^{+}(3,1)$

For a Lorentzian form of signature $(3,1)$ the determinant takes the two values $\pm1$ and $\det T = +1$ singles out $SO(3,1)$, of index two. The identity component $SO^{+}(3,1)$ is the subgroup of $SO(3,1)$ carrying a chosen timelike vector to a vector in the same half of the timelike cone; it has index two in $SO(3,1)$ and index four in $O(3,1)$. Both $SO(3,1)$ and $SO^{+}(3,1)$ have dimension six, and their Lie algebras agree:

$$
\dim\mathrm{SO}(3,1) = 6, \qquad \mathrm{SO}(3,1)\cong\mathrm{SO}(1,3)\cong\mathrm{SL}_2(\mathbb{C}) \ \text{ as complex Lie algebras},
$$

the last isomorphism being the one established in *The Orthogonal Lie Algebra*. The maximal compact subgroup of $SO^{+}(3,1)$ is the group $SO(3)$ of rotations of the spacelike $3$-plane, the stabiliser of a timelike vector; it is the compact part whose existence is guaranteed by the general structure theory of real Lie groups, and the quotient is a symmetric space, namely hyperbolic three-space. This last identification is developed, and is not used below.

### The Groups $O(2,2)$ and $SO(2,2)$

For a neutral form of signature $(2,2)$ the determinant again takes the values $\pm1$, $\dim\mathrm{SO}(2,2) = 6$, and

$$
\mathrm{SO}(2,2)\cong\mathrm{SL}_2(\mathbb{R})\oplus\mathrm{SL}_2(\mathbb{R}), \qquad
SO^{+}(2,2)\cong( SL_2(\mathbb{R})\times SL_2(\mathbb{R}))/\{\pm1\},
$$

the latter a standard isomorphism, obtained as follows: $SL_2(\mathbb{R})$ acts on the space of symmetric $2\times2$ matrices by $M\mapsto AMA^{t}$, preserving the determinant, which is a form of signature $(2,1)$, and the product acts on all $2\times2$ matrices by $(A,B)\cdot M = AMB^{-1}$, preserving the determinant, which is a form of signature $(2,2)$. The maximal compact subgroup of $SO^{+}(2,2)$ is the two-dimensional torus $SO(2)\times SO(2)$, larger than in the Lorentzian case relative to the dimension; the difference between the two signatures is exactly the difference between the ranks of the associated symmetric spaces.

The two signatures are not unrelated. Over $\mathbb{C}$ a non-degenerate symmetric form has no signature, and the complexifications $O(3,1)_{\mathbb{C}}$ and $O(2,2)_{\mathbb{C}}$ coincide with $O(4,\mathbb{C})$; the two real forms classified by $(3,1)$ and $(2,2)$ are the two real structures of the same complex group, one with real points the Lorentz group and one with real points the neutral group. The complex quadric $\{g = 0\}\subset\mathbb{P}^3$, which describes both, is doubly ruled: through each of its points pass two lines, and the two families are interchanged by the Galois action. This is the sense in which the definite case has one kind of rotation and the indefinite case has three, and it explains why the classification of one-parameter subgroups below has three entries rather than one.

## The Hermitian Form on the Split Biquaternions

### The Hermitian Scalar Form and Its Signature

The algebra carries a natural real bilinear form, built from the Hermitian conjugation alone.

**Definition.** The **Hermitian scalar form** on $\mathbb{H}_{\mathbb{D}}$, the corpus's $\langle\cdot,\cdot\rangle_{*}$ written $g$, is

$$
g(\tilde Q_1, \tilde Q_2) = \mathrm{Sc}\!\left(\tilde Q_1\tilde Q_2^{*}\right),
$$

where $\mathrm{Sc}$ is the scalar part, the coefficient of $e_t$ in the developed form.

**Proposition.** The Hermitian scalar form is symmetric, real-valued and $\mathbb{R}$-bilinear, and its signature is $(4,4)$. In the real basis $(e_t, \vec e_x, \vec e_y, \vec e_z, je_t, j\vec e_x, j\vec e_y, j\vec e_z)$ it is diagonal with entries $(+1,+1,+1,+1,-1,-1,-1,-1)$.

*Proof.* Symmetry: $\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*}) = \mathrm{Sc}((\tilde Q_2\tilde Q_1^{*})^{\natural}) = \mathrm{Sc}(\tilde Q_2\tilde Q_1^{*})$, because the scalar part is fixed by ${}^{\natural}$ and by $\bar{\cdot}$ separately, hence by ${}^{*}$. Bilinearity is clear. For the signature, write $\tilde Q_2 = c + jd$ with $c, d\in\mathbb{H}$; then $\tilde Q_2^{*} = c^{\natural} - jd^{\natural}$ and

$$
\tilde Q_1\tilde Q_2^{*} = \left(ac^{\natural} - bd^{\natural}\right) + j\left(bc^{\natural} - ad^{\natural}\right)
$$

for $\tilde Q_1 = a + jb$, so that $g(\tilde Q_1,\tilde Q_2) = \mathrm{Sc}(ac^{\natural} - bd^{\natural})$ with $\mathrm{Sc}$ now the quaternion scalar part. On the basis elements this gives $g(e_\mu,e_\nu) = \delta_{\mu\nu}$, $g(je_\mu,je_\nu) = -\delta_{\mu\nu}$ and $g(e_\mu,je_\nu) = 0$, since $\mathrm{Sc}(ac^{\natural})$ and $-\mathrm{Sc}(bd^{\natural})$ are the two contributions and the cross terms vanish.

The form is non-degenerate, of signature $(4,4)$, so it is neutral on the algebra as a whole, with four positive and four negative directions. This is the ambient form of the split biquaternion rotations: every rotation considered below is required to preserve it.

### The Hermitian and the Anti-Hermitian Subspaces

**Definition.** The **Hermitian subspace** $\mathbb{M}_+$ and the **anti-Hermitian subspace** $\mathbb{M}_-$ are the fixed-point sets of ${}^{*}$ and of ${}^{\flat} = -{}^{*}$:

$$
\mathbb{M}_+ = \{\tilde Q : \tilde{Q}^{*} = \tilde Q\}, \qquad \mathbb{M}_- = \{\tilde Q : \tilde Q^{\flat} = \tilde Q\} = \{\tilde Q : \tilde{Q}^{*} = -\tilde Q\}.
$$

**Proposition.** Both subspaces are four-dimensional and real, they are orthogonal to one another, and $\mathbb{H}_{\mathbb{D}} = \mathbb{M}_+\oplus\mathbb{M}_-$ is an orthogonal direct sum. Concretely,

$$
\mathbb{M}_+ = \{a + jb : a\in\mathbb{R}\,e_t,\ b\in\operatorname{Im}\mathbb{H}\}, \qquad
\mathbb{M}_- = \{a + jb : a\in\operatorname{Im}\mathbb{H},\ b\in\mathbb{R}\,e_t\},
$$

so that $\mathbb{M}_+$ has the orthonormal basis $(e_t, j\vec e_x, j\vec e_y, j\vec e_z)$ and $\mathbb{M}_-$ the orthogonal basis $(je_t, \vec e_x, \vec e_y, \vec e_z)$.

*Proof.* The subspaces are the $\pm1$-eigenspaces of the involution ${}^{*}$, hence complementary. If $\tilde Q_1^{*} = \tilde Q_1$ and $\tilde Q_2^{*} = -\tilde Q_2$, then $g(\tilde Q_1,\tilde Q_2) = \mathrm{Sc}(\tilde Q_1\tilde Q_2^{*}) = -\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, and $g(\tilde Q_2,\tilde Q_1) = \mathrm{Sc}(\tilde Q_2\tilde Q_1^{*}) = \mathrm{Sc}(\tilde Q_2\tilde Q_1) = \mathrm{Sc}(\tilde Q_1\tilde Q_2)$; by symmetry the two are equal, so both vanish. For the explicit descriptions, write $\tilde Q = a + jb$; then $\tilde{Q}^{*} = a^{\natural} - jb^{\natural}$, and $\tilde{Q}^{*} = \tilde Q$ gives $a^{\natural} = a$ and $b^{\natural} = -b$, while $\tilde{Q}^{*} = -\tilde Q$ gives $a^{\natural} = -a$ and $b^{\natural} = b$.

**Theorem.** The restrictions of the Hermitian scalar form have signatures

$$
g\big|_{\mathbb{M}_+} \sim (1,3), \qquad g\big|_{\mathbb{M}_-} \sim (3,1).
$$

Consequently $\mathbb{M}_-$ is a Lorentzian four-space with the form $g$, and $O(3,1)$ is the isometry group of $(\mathbb{M}_-,g)$; $\mathbb{M}_+$ carries the opposite Lorentzian form, and $O(1,3)\cong O(3,1)$ is its isometry group.

*Proof.* On $\mathbb{M}_+$ the basis $(e_t, j\vec e_x, j\vec e_y, j\vec e_z)$ gives diagonal entries $g(e_t,e_t) = +1$ and $g(j\vec e_k,j\vec e_k) = -1$, hence signature $(1,3)$. On $\mathbb{M}_-$ the basis $(je_t, \vec e_x, \vec e_y, \vec e_z)$ gives $g(je_t,je_t) = -1$ and $g(\vec e_k,\vec e_k) = +1$, hence signature $(3,1)$. The identification of the isometry group is the definition of $O(3,1)$.

The element $je_t$ is therefore a **timelike** vector of the algebra, of $g$-norm $-1$; the elements $\vec e_x, \vec e_y, \vec e_z$ are **spacelike**, of $g$-norm $+1$; and $\mathbb{M}_-$ is the Lorentzian four-space attached to the split biquaternion algebra. In the identity $u = u_+ + u_-$ with $u_{\pm}$ the projections onto $\mathbb{M}_{\pm}$, the form is $g(u,u) = |u_+|^2_{+} + |u_-|^2_{-}$ where the two summands carry opposite signs.

### Neutral Planes and the $(2,2)$ Form

**Definition.** A real subspace $W\subset\mathbb{H}_{\mathbb{D}}$ is **neutral** if $\dim W = 4$ and $g\big|_W$ has signature $(2,2)$. Such a subspace is **totally isotropic** if $g\big|_W = 0$ and $\dim W = 4$; the maximal $g$-totally-isotropic subspaces of $\mathbb{H}_{\mathbb{D}}$ are four-dimensional.

**Proposition.** Let $\mu\neq\nu$ be two distinct elements of $\{t,x,y,z\}$. The $\mathbb{D}$-span

$$
\mathbb{D}e_\mu\oplus\mathbb{D}e_\nu = \mathbb{R}e_\mu\oplus\mathbb{R}je_\mu\oplus\mathbb{R}e_\nu\oplus\mathbb{R}je_\nu
$$

is a neutral four-plane, with the orthonormal basis $(e_\mu, je_\mu, e_\nu, je_\nu)$ and the diagonal form $(+1,-1,+1,-1)$; the isometry group of this plane is $O(2,2)$. Every neutral four-plane of $\mathbb{H}_{\mathbb{D}}$ is carried to one of these by the symmetries of the algebra.

*Proof.* The basis is orthogonal because distinct basis elements of the quaternion basis are $g$-orthogonal and because $g(e_\mu,je_\mu) = 0$ by the cross-term computation above; the diagonal values are $g(e_\mu,e_\mu) = +1$ and $g(je_\mu,je_\mu) = -1$, and likewise for $\nu$. The form is therefore of signature $(2,2)$, and its isometry group is $O(2,2)$ by definition. The last assertion is the standard fact that a non-degenerate subspace of a given signature is unique up to the isometry group of the ambient form, applied with the ambient form $g$; the transitivity needed is that of the group preserving the quaternion structure of the index set, which acts transitively on unordered pairs of distinct indices.

So the split biquaternion algebra carries Lorentzian four-planes of both relevant signatures: the two eigenspaces of the Hermitian conjugation with $(3,1)$ and $(1,3)$, and the neutral four-planes spanned by two quaternion coordinates with $(2,2)$. The Lorentz group and the neutral group are both isometry groups of forms that the algebra presents, and this is the precise sense in which the split biquaternions are the algebra of the Lorentz groups $SO(3,1)$ and $SO(2,2)$.

## The Unit Sphere of the Algebra

### The Norm-One Group

**Definition.** The **unit sphere** of the split biquaternion algebra is

$$
S(\mathbb{H}_{\mathbb{D}}) = \{\tilde S\in\mathbb{H}_{\mathbb{D}} : \langle\tilde S\rangle_{\natural} = e_t\}.
$$

**Theorem.** An element $\tilde S$ has norm $e_t$ if and only if its two idempotent components are unit quaternions, so that

$$
S(\mathbb{H}_{\mathbb{D}}) = \left\{\tilde S_+\tilde\Pi_1 + \tilde S_-\tilde\Pi_2 : \lvert\tilde S_+\rvert = \lvert\tilde S_-\rvert = 1\right\}\cong S^3\times S^3,
$$

a compact group of dimension six. Under the identification $\tilde S = a + jb$ it is

$$
S(\mathbb{H}_{\mathbb{D}}) = \left\{a + jb : \lvert a + b\rvert = \lvert a - b\rvert = 1\right\}.
$$

*Proof.* By the idempotent decomposition of *Split-Biquaternion Algebra*, the split-biquaternion norm is $\langle\tilde S\rangle_{\natural} = \langle\tilde S_+\rangle_{\natural}\tilde\Pi_1 + \langle\tilde S_-\rangle_{\natural}\tilde\Pi_2$, since $\tilde\Pi_1\tilde\Pi_2 = 0$ and $\tilde\Pi_{1,2}$ are orthogonal idempotents; this equals $e_t = \tilde\Pi_1 + \tilde\Pi_2$ exactly when the two quaternion norms are both $1$. The relation $\tilde S_{\pm} = a\pm b$ gives the second description.

The unit sphere is thus a product of two copies of the quaternion unit sphere, and in particular it is **compact**. This is the first substantive difference from the classical description of a rotation group attached to an indefinite form: the set of units of the split biquaternion algebra is not a hyperboloid, and it is not diffeomorphic to a non-compact symmetric space. The hyperboloids appear only when the Hermitian form $g$ is used, and they are subsets of $\mathbb{M}_-$, as described below. The split complex unit group, by contrast, is the hyperbola $\{u\in\mathbb{D} : \langle u\rangle_{\natural} = 1\}$, a two-branched curve each branch of which is an isomorphic copy of $\mathbb{R}$, as in *Hyperbolic Rotations*; the difference is that in $\mathbb{H}_{\mathbb{D}}$ the split-biquaternion norm is definite on each quaternion component.

### The Two-Sided Action and the Comparison with the Quaternion Sphere

**Proposition.** The unit sphere acts on $\mathbb{H}_{\mathbb{D}}$ by the two-sided action

$$
\Phi_{(\tilde S,\tilde Q_3)}(\tilde{Q}) = \tilde S\tilde{Q}\tilde Q_3^{-1},
$$

which preserves the split-biquaternion norm; the resulting homomorphism $S^3\times S^3\times S^3\times S^3\to GL_8(\mathbb{R})$ has image of dimension eight, and the restriction to the quaternion subspace $\mathbb{H}\subset\mathbb{H}_{\mathbb{D}}$, on which the action is $\tilde{Q}\mapsto \tilde S_+\tilde{Q}\tilde S_-^{-1}$, realises $SO(4)$ on each idempotent component, as in *Quaternion Rotations and Reflections*.

*Proof.* Multiplicativity of the split-biquaternion norm shows that $\tilde S\tilde{Q}\tilde Q_3^{-1}$ has norm $\langle\tilde S\rangle_{\natural}\langle\tilde{Q}\rangle_{\natural}\langle\tilde Q_3\rangle_{\natural}^{-1} = \langle\tilde{Q}\rangle_{\natural}$ when $\tilde S,\tilde Q_3$ have norm $e_t$. The image is the product of the two commuting $SO(4)$s corresponding to the two idempotent components, of dimension $3+3$ for the components plus the two-dimensional diagonal scaling, that is eight. The restriction statement is the two-sided action of the quaternion unit sphere, established in *Quaternion Rotations and Reflections*.

The comparison with the quaternion sphere is then as follows. In the quaternion algebra the unit sphere $S^3$ is the whole group of units; in the split biquaternion algebra the unit sphere is $S^3\times S^3$, and the group of all units is four times as large in dimension, $\mathbb{H}^\times\times\mathbb{H}^\times$. The compactness of $S^3$ is not lost but doubled. What is lost is the divisibility: the split biquaternion algebra has zero divisors, so the set of elements of norm one is a proper subset of the units, and the polar decomposition of a unit is governed by the idempotent decomposition rather than by a single unit quaternion.

## Realising the Rotations in the Algebra

### The Unitary Group and the Elliptic Rotations

**Definition.** The **unitary group** of the Hermitian form is

$$
\mathrm{U}(\mathbb{H}_{\mathbb{D}}) = \{\tilde S\in\mathbb{H}_{\mathbb{D}} : \tilde S\tilde{S}^{*} = e_t\}.
$$

**Theorem.** The unitary group is four-dimensional and isomorphic to the direct product $Sp(1)\times\mathbb{R}$. Concretely,

$$
\mathrm{U}(\mathbb{H}_{\mathbb{D}}) = \left\{u\,\exp(\psi j) : u\in Sp(1),\ \psi\in\mathbb{R}\right\}, \qquad \exp(\psi j) = \cosh\psi + j\sinh\psi,
$$

and its action on $\mathbb{M}_-$ given by $\tilde{Q}\mapsto \tilde S\tilde{Q}\tilde{S}^{*}$ is by isometries of $g$; it fixes the timelike vector $je_t$ and acts on the spacelike three-plane $\operatorname{Im}\mathbb{H} = \mathbb{R}\vec e_x\oplus\mathbb{R}\vec e_y\oplus\mathbb{R}\vec e_z$ by

$$
v\longmapsto u\,v\,u^{\natural} ,
$$

so that the image is the group $SO(3)$ of rotations of the spacelike three-plane. The factor $\exp(\psi j)$ lies in the kernel of the action.

*Proof.* Write $\tilde S = a + jb$. Then $\tilde S\tilde{S}^{*} = (aa^{\natural} - bb^{\natural}) + j(ba^{\natural} - ab^{\natural}) = e_t$ gives the two conditions $aa^{\natural} - bb^{\natural} = 1$ and $ab^{\natural} = ba^{\natural}$; the second says $ab^{\natural}$ is real. Writing $b = tu$ with $t = \lvert b\rvert$ and $u\in Sp(1)$, the first condition forces $a = \pm\sqrt{1 + t^2}\,u$, so $\tilde S = \pm u(\cosh\psi + j\sinh\psi)$ with $\sinh\psi = t$, and since $j$ is central the factor $\cosh\psi + j\sinh\psi = \exp(\psi j)$ commutes with $u$; the sign is absorbed into $u$, giving the stated decomposition, of dimension $3+1$. For the action, let $\tilde{Q} = a' + jb'$ with $a'\in\operatorname{Im}\mathbb{H}$ and $b'\in\mathbb{R}$, so that $\tilde{Q}\in\mathbb{M}_-$. Then $\tilde{Q}^{*} = -a' - jb' = -\tilde{Q}$, and

$$
\tilde S\tilde{Q}\tilde{S}^{*} = u(a' + jb')\exp(\psi j)\big(u^{\natural} - ju^{\natural}\,\sinh\psi\big)
= u a'u^{\natural} + j\,b' ,
$$

because $j$ is central, $\exp(\psi j)$ is central with $\exp(\psi j)\exp(\psi j){}^{*} = \exp(-\psi j)\exp(\psi j) = e_t$, and $b'$ is real and therefore commutes with $u$. Hence the first component is the adjoint action $a'\mapsto ua'u^{\natural}$ on the imaginary quaternions and the second is unchanged. The adjoint action of $Sp(1)$ on $\operatorname{Im}\mathbb{H}$ is the standard surjection $Sp(1)\to SO(3)$ with kernel $\{\pm1\}$, by *Quaternion Rotations and Reflections*, so the image is $SO(3)$. Preservation of $g$ follows because the displayed formula has $g$-norms $\lvert a'\rvert^2 - (b')^2$ unchanged. Finally the action of $\exp(\psi j)$ alone is trivial, so this factor lies in the kernel.

The unitary group therefore realises the **elliptic** part of the Lorentz group: the compact subgroup $SO(3)\subset SO^{+}(3,1)$ of spacelike rotations, which fixes the timelike direction $je_t$ and acts on the spacelike three-plane. The rotations obtained are exactly the conjugates of the quaternion rotations into the split biquaternion algebra.

### The Split-Complex Units and the Hyperbolic Rotations

The hyperbolic part is realised not on $\mathbb{M}_-$ but on the neutral planes and on the split complex lines. Let

$$
C = \mathbb{R}\,e_t\oplus\mathbb{R}\,j \subset\mathbb{H}_{\mathbb{D}}
$$

be the copy of the split complex algebra generated by $j$; it is central in $\mathbb{H}_{\mathbb{D}}$, and the split complex conjugation $\bar{\cdot}$ of the algebra restricts to the conjugation $c + js\mapsto c - js$ of $C$.

**Proposition.** The group of units $H = \{u\in C : uu^{*} = e_t\}$ is

$$
H = \left\{\exp(\theta j) = \cosh\theta + j\sinh\theta : \theta\in\mathbb{R}\right\}\cup\left\{-\exp(\theta j) : \theta\in\mathbb{R}\right\}\cong\mathbb{R}\times\mathbb{Z}/2\mathbb{Z},
$$

its identity component is the one-parameter group of the split complex hyperbolic rotations, and its action on $\mathbb{D}e_\mu$ by left multiplication, for each $\mu$, is the same hyperbolic rotation of the real plane $\mathbb{R}e_\mu\oplus\mathbb{R}je_\mu$:

$$
\exp(\theta j)\left(c\,e_\mu + s\,je_\mu\right) = \left(c\cosh\theta + s\sinh\theta\right)e_\mu + \left(c\sinh\theta + s\cosh\theta\right)je_\mu .
$$

*Proof.* In $C$ one has $uu^{*} = c^2 - s^2$ for $u = c + js$, so $uu^{*} = 1$ is the hyperbola $c^2 - s^2 = 1$, whose two branches are parametrised by $c = \cosh\theta$, $s = \sinh\theta$ and by their negatives. Since $j$ is central and $je_\mu = e_\mu j$, the product $\exp(\theta j)e_\mu = (\cosh\theta)e_\mu + (\sinh\theta)je_\mu$ and $\exp(\theta j)je_\mu = (\sinh\theta)e_\mu + (\cosh\theta)je_\mu$, giving the displayed formula, which is the matrix of a hyperbolic rotation.

**Proposition.** Left multiplication by $\exp(\theta j)$ preserves the Hermitian scalar form $g$ on every neutral four-plane $\mathbb{D}e_\mu\oplus\mathbb{D}e_\nu$ with $\mu\neq\nu$, and it does not preserve $\mathbb{M}_-$. On the neutral plane it acts as a simultaneous hyperbolic rotation in the two coordinate planes $\mathbb{R}e_\mu\oplus\mathbb{R}je_\mu$ and $\mathbb{R}e_\nu\oplus\mathbb{R}je_\nu$, so that the image is the diagonal one-parameter subgroup

$$
\Delta\,SO(1,1)\subset SO(1,1)\times SO(1,1)\subset SO^{+}(2,2).
$$

*Proof.* The basis $(e_\mu, je_\mu, e_\nu, je_\nu)$ of the neutral plane is $g$-orthonormal of signature $(+1,-1,+1,-1)$. In each coordinate plane the map is the hyperbolic rotation with matrix $\begin{pmatrix}\cosh\theta & \sinh\theta\\ \sinh\theta & \cosh\theta\end{pmatrix}$ in the basis $(e_\rho, je_\rho)$, and this matrix preserves the form $\operatorname{diag}(+1,-1)$ because $\cosh^2\theta - \sinh^2\theta = 1$ and the cross term $\cosh\theta\sinh\theta - \sinh\theta\cosh\theta$ vanishes; two blocks therefore preserve the form of signature $(2,2)$. It does not preserve $\mathbb{M}_-$: the image of $je_t$ is $\sinh\theta\,e_t + \cosh\theta\,je_t$, whose $e_t$-component is real and non-zero for $\theta\neq0$, whereas an element of $\mathbb{M}_-$ has a purely imaginary $e_t$-component.

Two geometrically distinct families of isometries are thus realised inside the algebra: the elliptic group $SO(3)$ of the unitary action, on the Lorentzian four-plane $\mathbb{M}_-$, and the hyperbolic group, the diagonal $SO(1,1)$ inside $SO(1,1)\times SO(1,1)$, of the split complex units, on the neutral four-planes. The two families commute: the unitary action is conjugation by quaternion units and fixes the central split complex scalars, while left multiplication by $\exp(\theta j)$ is central and commutes with conjugation by any element.

### The Parabolic Case and the Absence of Nilpotents

The classification of the one-parameter subgroups of $SO^{+}(3,1)$ has three entries, matching the three kinds of rotation of the two-dimensional algebras. A non-zero generator $N\in\mathrm{SO}(3,1)$ has a non-trivial kernel on the complexification of $\mathbb{R}^{3,1}$, and the kernel always contains a real vector; the one-parameter subgroup $t\mapsto\exp(tN)$ is called **elliptic** if that kernel contains a timelike vector, **hyperbolic** if it contains a spacelike vector and no timelike one, and **parabolic** if it contains a null vector and no non-null one. Every elliptic one-parameter subgroup is conjugate to a rotation of a spacelike two-plane; every hyperbolic one is conjugate to a boost, with a fixed spacelike two-plane and two real null eigenvectors; every parabolic one is conjugate to a transvection

$$
T_t = 1 + tN, \qquad N^2 = 0,
$$

fixing a null vector and no other, with $\langle\cdot\rangle_{\natural}$ nilpotent.

The elliptic type is realised in the algebra by the exponentials of the quaternion vector fields in the unitary group of the preceding subsection; the hyperbolic type is realised by the split complex units $\exp(\psi j)$ and by their conjugates; both are exponents of elements with square $-e_t$ and $+e_t$ respectively in the algebra, in the sense of the exponentials of *Split-Biquaternion Roots of Minus One*. The parabolic type is not realised in the algebra at all, and the reason is structural:

**Proposition.** The split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$ contains no non-zero nilpotent element, and consequently no element of $\mathbb{H}_{\mathbb{D}}$ exponentiates to a parabolic one-parameter subgroup; the parabolic one-parameter subgroups exist only in the isometry group of the Lorentzian form, not in the algebra acting on itself.

*Proof.* By *Split-Biquaternion Algebra*, $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$ as a ring, a direct sum of two division rings, hence a semisimple ring; a semisimple ring has no non-zero nilpotent elements, since a nilpotent element would generate a nilpotent ideal, contradicting semisimplicity. The exponential of a nilpotent element is unipotent of the form $1 + tN$ with $N^2 = 0$, so the absence of nilpotents removes parabolic generators from the algebra. In the isometry group of a $(3,1)$ form the transvections exist regardless, because $\mathrm{SO}(3,1)$ contains nilpotent elements although the algebra of coefficients does not.

This is the precise content of the split in the classification: the elliptic and the hyperbolic one-parameter subgroups are separated because the form is indefinite, and only these two are contributed by the coefficient algebra. The dual number construction, which realises the parabolic rotation of the plane by the exponential of a square-zero element, has no counterpart in $\mathbb{H}_{\mathbb{D}}$, as recorded in *The Three Two-Dimensional Algebras and the Three Kinds of Rotation*.

## The Dagger Sandwich of a General Unit

The unitary action $\tilde Q\mapsto\tilde S\tilde Q\tilde{S}^{*}$ of the preceding section is defined for every unit, unitary or not; taken in that generality it is the **dagger sandwich**, a linear representation of the unit group that is an automorphism only on the unitary subgroup.

**Definition.** The **dagger sandwich** of a unit $\tilde U$ is the real-linear map

$$
\operatorname{H}_{\tilde U} : \mathbb{H}_{\mathbb{D}}\longrightarrow\mathbb{H}_{\mathbb{D}}, \qquad \operatorname{H}_{\tilde U}(\tilde Q) = \tilde U\,\tilde Q\,\tilde U^{*}.
$$

It is well defined for every unit and depends only on $\tilde U$; the two-sided placement of the Hermitian conjugate is what distinguishes it from left and right multiplication. It is invertible, with inverse $\operatorname{H}_{\tilde U^{-1}}$, since $(\tilde U^{*})^{-1} = (\tilde U^{-1})^{\dagger}$.

**Theorem (multiplicative exactly on the unitary subgroup).** Let $\tilde U$ be a unit. Then $\operatorname{H}_{\tilde U}(\tilde Q_1\tilde Q_2) = \operatorname{H}_{\tilde U}(\tilde Q_1)\operatorname{H}_{\tilde U}(\tilde Q_2)$ for all $\tilde Q_1,\tilde Q_2$ if and only if $\tilde U^{*}\tilde U = e_t$, that is, if and only if $\tilde U$ is unitary.

**Proof.** The two sides are $\tilde U\tilde Q_1\tilde Q_2\tilde U^{*}$ and $\tilde U\tilde Q_1\tilde U^{*}\tilde U\tilde Q_2\tilde U^{*}$; they agree for all $\tilde Q_1,\tilde Q_2$ exactly when the factor $\tilde U^{*}\tilde U$ inserted between $\tilde Q_1$ and $\tilde Q_2$ is $e_t$, that is when $\tilde U^{*} = \tilde U^{-1}$ and $\tilde U$ is unitary. In that case the sandwich is the inner automorphism $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{-1}$.

**Theorem.** For every unit $\tilde U$ the sandwich maps $\mathbb{M}_+$ to $\mathbb{M}_+$ and $\mathbb{M}_-$ to $\mathbb{M}_-$.

**Proof.** If $\tilde Q^{\dagger} = \tilde Q$ then $(\tilde U\tilde Q\tilde U^{*})^{\dagger} = \tilde U^{\dagger{}^{*}}\tilde Q^{\dagger}\tilde U^{*} = \tilde U\tilde Q\tilde U^{*}$, so the image is Hermitian; if $\tilde Q^{\dagger} = -\tilde Q$ the image is anti-Hermitian.

**Theorem (the defect under the indefinite form).** With $N_{\pm}(\tilde U) = \lvert\tilde U_{\pm}\rvert^{2}$ the two real components of the split-biquaternion norm,

$$
N\!\left(\operatorname{H}_{\tilde U}(\tilde Q)\right) = N_+(\tilde U)\,N_-(\tilde U)\,\langle\tilde Q\rangle_{\natural}, \qquad g\!\left(\operatorname{H}_{\tilde U}(\tilde Q)\right) = g(\tilde Q) \ \text{ for unitary } \tilde U .
$$

**Proof.** The split-biquaternion norm is multiplicative, so $\langle\operatorname{H}_{\tilde U}(\tilde Q)\rangle_{\natural} = \langle\tilde U\rangle_{\natural}\langle\tilde Q\rangle_{\natural}\langle\tilde U^{*}\rangle_{\natural}$, and the Hermitian conjugation interchanges the two idempotent components, so $\langle\tilde U^{*}\rangle_{\natural} = \lvert\tilde U_-\rvert^{2}\tilde\Pi_1 + \lvert\tilde U_+\rvert^{2}\tilde\Pi_2$ while $\langle\tilde U\rangle_{\natural} = \lvert\tilde U_+\rvert^{2}\tilde\Pi_1 + \lvert\tilde U_-\rvert^{2}\tilde\Pi_2$; their product is the central real number $\lvert\tilde U_+\rvert^{2}\lvert\tilde U_-\rvert^{2}e_t = N_+(\tilde U)N_-(\tilde U)e_t$. For the Hermitian form, a unitary $\tilde U$ satisfies $\tilde U^{*} = \tilde U^{-1}$, and $\operatorname{H}_{\tilde U}$ is then the inner automorphism; since conjugation preserves the scalar part and $\operatorname{H}_{\tilde U}(\tilde Q)^{\dagger} = \operatorname{H}_{\tilde U}(\tilde Q^{\dagger})$, one has $g(\operatorname{H}_{\tilde U}(\tilde Q)) = \mathrm{Sc}\bigl(\operatorname{H}_{\tilde U}(\tilde Q)\operatorname{H}_{\tilde U}(\tilde Q)^{\dagger}\bigr) = \mathrm{Sc}\bigl(\tilde U\,\tilde Q\tilde Q^{\dagger}\tilde U^{-1}\bigr) = \mathrm{Sc}(\tilde Q\tilde Q^{\dagger}) = g(\tilde Q)$.

The factor $N_+(\tilde U)N_-(\tilde U)$ is therefore the **defect** of the sandwich under the indefinite form. It vanishes exactly when one of the two components is zero, that is exactly on the zero divisors; on the unit group it is a nonzero real number of either sign, and the Hermitian form $g$ is preserved by every unitary element. The biquaternion sandwich has the analogous factor $\lvert \langle\tilde U\rangle_{\natural}\rvert^{2}$; the difference is that there the factor is a sum of squares and here a difference.

**Theorem (kernel).** $\operatorname{H}_{\tilde U} = \mathrm{id}$ if and only if $\tilde U$ is central and unitary, that is $\tilde U = Q_te_t$ with $Q_t = q_t + jq'_t$ and $q_t^{2} - q'^{2}_{0} = 1$. On the unit-norm slice $\langle\tilde U\rangle_{\natural} = e_t$ the kernel reduces to $\{\pm e_t\}$.

**Proof.** If $\operatorname{H}_{\tilde U}(\tilde Q) = \tilde Q$ for all $\tilde Q$, then $\tilde Q = e_t$ gives $\tilde U\tilde U^{*} = e_t$, so $\tilde U$ is unitary, and then $\tilde U\tilde Q = \tilde Q\tilde U$ for all $\tilde Q$, so $\tilde U$ is central. A central element is $Q_te_t$ with $Q_t\in\mathbb{D}$, and it is unitary exactly when $Q_t\bar{Q_t} = q_t^{2} - q'^{2}_{0} = 1$, the two branches of a hyperbola in the centre. Restricting to $\langle\tilde U\rangle_{\natural} = Q_t^{2} = e_t$ gives $Q_t = \pm1$.

The kernel of the full sandwich is thus the group of central unitary elements, the split complex units of modulus one, an $\mathbb{R}\times\mathbb{Z}/2$ inside the centre — the analogue of the circle $\mathrm{U}(1)$ of the biquaternion case. On the unit-norm slice it is the two central signs, and that kernel of order two is the double cover.

### The Comparison with Left Multiplication, and the Table of Subspaces

| | left multiplication $\tilde U\tilde Q$ | the sandwich $\operatorname{H}_{\tilde U}(\tilde Q)$ |
|---|---|---|
| type of map | algebra endomorphism | neither multiplicative nor unital; a representation of the units |
| image of $e_t$ | $\tilde U$ | $\tilde U\tilde U^{*}$, Hermitian but not central in general |
| kernel on the unit sphere | $\{e_t\}$ | $\{\pm e_t\}$ |
| effect on the norm | $\langle\tilde U\tilde Q\rangle_{\natural} = \langle\tilde U\rangle_{\natural}\langle\tilde Q\rangle_{\natural}$ | $\langle\operatorname{H}_{\tilde U}\tilde Q\rangle_{\natural} = N_+(\tilde U)N_-(\tilde U)\langle\tilde Q\rangle_{\natural}$ |

The sandwich acts on the four distinguished subspaces as follows.

| subspace | preserved by $\operatorname{H}_{\tilde U}$? | image |
|---|---|---|
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$, the centre | no | $\tilde UQ_0\tilde U^{*}$, not central in general |
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, the quaternion subspace | no | not closed in general |
| $\mathbb{M}_+$ | yes | $\mathbb{M}_+$ |
| $\mathbb{M}_-$ | yes | $\mathbb{M}_-$ |

The centre is not preserved: on $e_t$ the sandwich gives $\tilde U\tilde U^{*}$, which is Hermitian but not central for a general unit, although on the unitary subgroup, where the sandwich is an automorphism, it preserves the centre because an automorphism carries the centre to itself. The two sectors are the only subspaces of the four that survive, and they survive as a pair: the sandwich preserves each separately and cannot move one into the other, because Hermitian character is exactly what the map preserves. This is the operator-theoretic reason that the Hermitian decomposition $\mathbb{H}_{\mathbb{D}} = \mathbb{M}_+\oplus\mathbb{M}_-$ is the natural one for the action.

### The Polar Dictionary

**Proposition.** In the idempotent description the sandwich acts componentwise,

$$
\operatorname{H}_{\tilde U}(\tilde Q)_+ = \tilde U_+\,\tilde Q_+\,\tilde U^{\natural}_- , \qquad \operatorname{H}_{\tilde U}(\tilde Q)_- = \tilde U_-\,\tilde Q_-\,\tilde U^{\natural}_+ ,
$$

so that the polar data of the element appear as follows.

| polar datum of $\tilde U$ | what the sandwich sees |
|---|---|
| the two components $\tilde U_+,\tilde U_-$ | the one-sided multiplications $\tilde U_+(\cdot)\tilde U^{\natural}_-$ and $\tilde U_-(\cdot)\tilde U^{\natural}_+$ on the two halves |
| the scale $N_+N_-$ | the dilation $N_+N_-$ of the split-biquaternion norm |
| the central unitary factor | nothing: it is the kernel, and the sandwich is blind to it |
| the two unit-sphere parts | the rotation parts of the action |

**Proof.** Multiplication is componentwise in the idempotent description, and the Hermitian conjugation interchanges the components with a quaternion conjugation, $(\tilde U^{*})_+ = \tilde U^{\natural}_-$ and $(\tilde U^{*})_- = \tilde U^{\natural}_+$; the display follows. The invisibility of the central unitary factor is the kernel theorem and the scaling is the defect theorem.

### The Relation to the Biquaternion Dagger Sandwich

In the biquaternion case the dagger sandwich of a unit-norm element is the action of $SL(2,\mathbb{C})$ on the Hermitian matrices, with image the proper orthochronous Lorentz group $SO^{+}(1,3)$, and on the unit-norm slice its kernel is $\{\pm e_t\}$; the unit-norm slice there is $SL(2,\mathbb{C})$, three complex dimensions. Here the unit-norm slice is the six-dimensional $S^3\times S^3$ and the sandwich on it is **not** generally an automorphism, since $\tilde U^{*}\neq\tilde U^{-1}$ unless $\tilde U$ is unitary; the Lorentzian form $g$ is preserved on the unitary group $\{\tilde U : \tilde U\tilde U^{*} = e_t\}\cong Sp(1)\times\mathbb{R}$, where the sandwich is the inner automorphism and its image is the compact rotation group $SO(3)$ of the spacelike three-plane, fixing the timelike $je_t$ (*The Unitary Group and the Elliptic Rotations*). The doubling of the angle and the two-to-one cover are the same in both cases; the difference is which slice of the algebra carries the Lorentz action.

## The Hyperboloid, the Null Cone and the Rulings

The subsets of $\mathbb{M}_-$ on which $g$ takes constant values carry the geometry of the Lorentzian form.

**Definition.** In the Lorentzian four-space $(\mathbb{M}_-,g)$ the **null cone** is $C_0 = \{\tilde{Q}\in\mathbb{M}_- : g(\tilde{Q},\tilde{Q}) = 0\}$, and the **hyperboloids** are the level sets $C_{\pm1} = \{\tilde{Q}\in\mathbb{M}_- : g(\tilde{Q},\tilde{Q}) = \pm1\}$.

**Theorem.** In coordinates $\tilde{Q} = a\,je_t + v$ with $a\in\mathbb{R}$ and $v\in\operatorname{Im}\mathbb{H}$, the form is $g(\tilde{Q},\tilde{Q}) = \lvert v\rvert^2 - a^2$, so that the level sets are

$$
C_{-1} = \{a^2 = 1 + \lvert v\rvert^2\}, \qquad C_{+1} = \{\lvert v\rvert^2 = 1 + a^2\}, \qquad C_0 = \{\lvert v\rvert = \lvert a\rvert\}.
$$

The set $C_{-1}$ is a **hyperboloid of two sheets**, each sheet diffeomorphic to $\mathbb{R}^3$; the set $C_{+1}$ is a **hyperboloid of one sheet**, diffeomorphic to $S^2\times\mathbb{R}$; and $C_0$ is the cone over the two-sphere $S^2$ with apex at the origin. The group $SO^{+}(3,1)$ acts transitively on each sheet of $C_{-1}$ and on $C_{+1}$, with isotropy $SO(3)$ at a point of a sheet of $C_{-1}$ and isotropy $SO(2,1)$ at a point of $C_{+1}$; the elliptic one-parameter subgroups are those fixing a timelike direction, the hyperbolic ones those fixing a spacelike direction, and the parabolic ones those fixing a null direction of $C_0$.

*Proof.* The coordinate expression for $g$ is the one computed in the previous section. The equation $g(\tilde{Q},\tilde{Q}) = -1$ is $a^2 = 1 + \lvert v\rvert^2$, giving the two sheets $a = \pm\sqrt{1+\lvert v\rvert^2}$, each parametrised by $v\in\mathbb{R}^3$ and therefore diffeomorphic to $\mathbb{R}^3$. The equation $g(\tilde{Q},\tilde{Q}) = +1$ is $\lvert v\rvert^2 = 1 + a^2$; for each $a\in\mathbb{R}$ this is the sphere of radius $\sqrt{1+a^2}$ in the $v$-variable, so the assignment $\tilde{Q}\mapsto(v/\lvert v\rvert, a)$ is a diffeomorphism $C_{+1}\to S^2\times\mathbb{R}$, and $C_{+1}$ is connected. The equation $g(\tilde{Q},\tilde{Q}) = 0$ is $\lvert v\rvert = \lvert a\rvert$, the cone over $S^2$. The transitivity and isotropy statements are the orbit theory of the Lorentzian form, treated in *Pseudo-Riemannian and Lorentzian Geometry*; the classification of one-parameter subgroups by the type of the vectors they fix is the standard normal form theory of $\mathrm{SO}(3,1)$, in the three cases listed.

Two warnings are needed, because they are the points at which the split biquaternion geometry differs from what the definite case would suggest.

**Proposition.** Every zero divisor of $\mathbb{H}_{\mathbb{D}}$ is isotropic for the ambient form $g$: if $\tilde{Q}$ is a zero divisor then $g(\tilde{Q},\tilde{Q}) = 0$. The converse fails, and the null cone of $g$ is strictly larger than the zero divisor set; moreover the two ideals meet the Lorentzian four-plane $\mathbb{M}_-$ only at the origin, so the null vectors of $(\mathbb{M}_-,g)$ are not zero divisors.

*Proof.* By *Split-Biquaternion Zero Divisors* the zero divisors are exactly the elements with $\tilde Q_+ = 0$ or $\tilde Q_- = 0$, that is, the union of the two ideals $\mathbb{H}\tilde\Pi_1$ and $\mathbb{H}\tilde\Pi_2$. Let $\tilde Q = \tilde Q_-\tilde\Pi_2$, so that $\tilde Q_+ = 0$. Since ${}^{*} = {}^{\natural}\,\bar{\cdot}$ and $\bar{\cdot}$ interchanges $\tilde\Pi_1$ and $\tilde\Pi_2$, one has $\tilde{Q}^{*} = \tilde{Q}^{\natural}_-\tilde\Pi_1$, whence

$$
\tilde Q\tilde{Q}^{*} = \tilde Q_-\tilde{Q}^{\natural}_-\tilde\Pi_2\tilde\Pi_1 = 0,
$$

because $\tilde\Pi_2\tilde\Pi_1 = 0$; therefore $g(\tilde Q,\tilde Q) = \mathrm{Sc}(0) = 0$. The same argument applies to the other ideal. For the failure of the converse, the element $\tilde{Q} = \vec e_x + je_t$ satisfies $g(\tilde{Q},\tilde{Q}) = 1 - 1 = 0$, so it lies on the null cone of $g$ in $\mathbb{M}_-$, while $\tilde{Q}_+ = \vec e_x + e_t$ and $\tilde{Q}_- = \vec e_x - e_t$ are both non-zero, so $\tilde{Q}$ is not a zero divisor. Finally, if $\tilde Q = \tilde Q_+\tilde\Pi_1$ lies in $\mathbb{M}_-$, then writing $\tilde Q = a + jb$ gives $a = b = \tfrac{1}{2}\tilde Q_+$; the condition $a\in\operatorname{Im}\mathbb{H}$ forces $\tilde Q_+\in\operatorname{Im}\mathbb{H}$ and the condition $b\in\mathbb{R}$ forces $\tilde Q_+\in\mathbb{R}$, so $\tilde Q_+ = 0$ and $\tilde Q = 0$; the same holds for the other ideal.

The second warning is that the non-compactness appears only on the isometry-group side. The unit sphere of the algebra is compact, being $S^3\times S^3$; the Lorentzian hyperboloids $C_{\pm1}$ are non-compact and are orbits of the non-compact group $SO^{+}(3,1)$; and the zero divisor cone, which is the union of the two isotropic ideals, lives in the ambient eight-dimensional space and meets $\mathbb{M}_-$ only at the origin, so it is not the null cone of the Lorentzian form. In the quaternion case the compact sphere $S^3$ is simultaneously the set of units and an orbit of the compact rotation group; here the set of units and the Lorentzian hyperboloid are different objects, one compact and one not, and the bridge between them is the idempotent decomposition.

## Summary

The Lorentz group is the isometry group of a non-degenerate symmetric bilinear form of signature $(3,1)$; it is a Lie group of dimension six with Lie algebra $\mathrm{SO}(3,1)\cong\mathrm{SL}_2(\mathbb{C})$ as complex Lie algebras, its identity component $SO^{+}(3,1)$ has maximal compact subgroup $SO(3)$, and the neutral signature $(2,2)$ gives $SO^{+}(2,2)\cong(SL_2(\mathbb{R})\times SL_2(\mathbb{R}))/\{\pm1\}$. The two signatures are the two real forms of the same complex group.

The split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$ carries the Hermitian scalar form $g(\tilde Q_1,\tilde Q_2) = \mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$, of signature $(4,4)$, diagonal in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z,je_t,j\vec e_x,j\vec e_y,j\vec e_z)$. The Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$ are four-dimensional, orthogonal, complementary, and carry the forms of signature $(1,3)$ and $(3,1)$; the $\mathbb{D}$-span of any two quaternion coordinates is a neutral four-plane of signature $(2,2)$. Hence $O(3,1)$ and $O(2,2)$ both occur as isometry groups of forms that the algebra presents.

The unit sphere $\{\tilde S : \langle\tilde S\rangle_{\natural} = e_t\}\cong S^3\times S^3$ is compact and six-dimensional, the product of the two idempotent components. The unitary group $\{\tilde S : \tilde S\tilde{S}^{*} = e_t\}\cong Sp(1)\times\mathbb{R}$ acts on $\mathbb{M}_-$ by isometries, fixes the timelike vector $je_t$, and realises exactly the compact group $SO(3)$ of spacelike rotations; the split complex units $\exp(\theta j)$ preserve the neutral four-planes and realise there the diagonal $SO(1,1)$ inside $SO(1,1)\times SO(1,1)$, and the two families commute. The parabolic one-parameter subgroups are not realised in the algebra, because $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$ is semisimple and has no non-zero nilpotent element.

The dagger sandwich $\operatorname{H}_{\tilde U}(\tilde Q) = \tilde U\tilde Q\tilde U^{*}$ of a general unit is a linear representation of the unit group, multiplicative exactly on the unitary subgroup, where it is the inner automorphism $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{-1}$. It preserves the two sectors $\mathbb{M}_{\pm}$ and no other of the four distinguished subspaces, and it scales the split-biquaternion norm by the real defect factor $N_+(\tilde U)N_-(\tilde U)$, which vanishes exactly on the zero divisors and is a nonzero real number of either sign on the units; the Hermitian form $g$ is preserved by every unitary element. Its kernel is the group of central unitary elements, the split complex units of modulus one, an $\mathbb{R}\times\mathbb{Z}/2$ in the centre, which on the unit-norm slice reduces to $\{\pm e_t\}$. In the idempotent description the sandwich acts componentwise as $\tilde Q_+\mapsto\tilde U_+\tilde Q_+\tilde U^{\natural}_-$ and $\tilde Q_-\mapsto\tilde U_-\tilde Q_-\tilde U^{\natural}_+$, so it sees every polar factor of the element except the central unitary one.

In $(\mathbb{M}_-,g)$ the level set $g = -1$ is a hyperboloid of two sheets, each an $\mathbb{R}^3$, and $g = +1$ is a hyperboloid of one sheet, an $S^2\times\mathbb{R}$; the null cone is the cone over $S^2$. Every zero divisor of the algebra is isotropic for the ambient form $g$, so the union of the two ideals lies inside the ambient null cone and meets $\mathbb{M}_-$ only at the origin; the Lorentzian null cone is strictly larger than the zero divisor set, since $\vec e_x + je_t$ is null and not a zero divisor. The compact unit sphere and the non-compact Lorentzian hyperboloids are different objects, bridged by the idempotent decomposition.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}} = \mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}$ | The split biquaternion algebra, real dimension $8$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$ |
| $j$ | Split complex unit, $j^2 = +e_t$, central |
| $\tilde Q = \sum_{\mu\in\{t,x,y,z\}}Q_\mu e_\mu = a + jb = \tilde Q_+\tilde\Pi_1 + \tilde Q_-\tilde\Pi_2$ | General split biquaternion |
| $\tilde\Pi_{1,2} = \tfrac{1}{2}(1\pm j)$ | Idempotents, $\tilde\Pi_1\tilde\Pi_2 = 0$ |
| ${}^{\natural},\ \bar{\cdot},\ {}^{*} = {}^{\natural}\,\bar{\cdot},\ {}^{\flat} = -{}^{*}$ | The four conjugations |
| $\langle\tilde Q\rangle_{\natural} = \tilde Q\tilde{Q}^{\natural}$ | Split-Biquaternion norm |
| $g(\tilde Q_1,\tilde Q_2) = \langle\tilde Q_1,\tilde Q_2\rangle_{*} = \mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ | Hermitian form, signature $(4,4)$ |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Hermitian and anti-Hermitian subspaces, signatures $(1,3)$, $(3,1)$ |
| $\mathbb{D}e_\mu\oplus\mathbb{D}e_\nu$ | Neutral four-plane, signature $(2,2)$ |
| $O(n,m)$, $SO(n,m)$, $SO^{+}(n,m)$ | Orthogonal group of a form, its determinant-one part, its identity component |
| $\mathrm{SO}(n,m)$ | Lie algebra of $g$-skew endomorphisms, dimension $\tfrac{1}{2}\langle N-1\rangle_{\natural}$ |
| $\mathrm{U}(\mathbb{H}_{\mathbb{D}}) = \{\tilde S : \tilde S\tilde{S}^{*} = e_t\}\cong Sp(1)\times\mathbb{R}$ | Unitary group |
| $\operatorname{H}_{\tilde U}(\tilde Q) = \tilde U\tilde Q\tilde U^{*}$ | The dagger sandwich of a general unit; the inner automorphism on the unitary subgroup |
| $N_+(\tilde U)N_-(\tilde U)$ | The defect of the sandwich, the real scaling of the split-biquaternion norm |
| kernel of $\operatorname{H}$ | The central unitary group, the split complex units of modulus one |
| $\exp(\psi j) = \cosh\psi + j\sinh\psi$ | Split complex unit, hyperbolic one-parameter group |
| $S(\mathbb{H}_{\mathbb{D}})\cong S^3\times S^3$ | Norm-one unit sphere |
| $C_0$, $C_{\pm1}$ | Null cone and hyperboloids in $\mathbb{M}_-$ |
| $\mathbb{H}\tilde\Pi_1$, $\mathbb{H}\tilde\Pi_2$ | The two ideals, the set of zero divisors |



## Further Reading

- Robert Gilmore, *Lie Groups, Lie Algebras, and Some of Their Applications* (Wiley, 1974), for the isometry groups of quadratic forms and the classification of one-parameter subgroups of the Lorentz group.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the restricted Lorentz group, its maximal compact subgroup and the associated symmetric spaces.
- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 1955), for the orthogonal groups and the classification of their real forms.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the identification of $\mathrm{SO}(3,1)$ with $\mathrm{SL}_2(\mathbb{C})$ and the two real forms.
- Michael Eastwood and Paul Tod, "Edth-a differential operator on the sphere", *Mathematical Proceedings of the Cambridge Philosophical Society* **92** (1982), 317–330, for the doubly ruled complex quadric and the two real forms.
- Dirk J. Struik, *Lectures on Classical Differential Geometry* (Dover, 1988), for the doubly ruled quadrics and their two families of lines.
- Rafael López, "Differential geometry of curves and surfaces in Lorentz–Minkowski space" (arXiv:0810.3351), for the hyperboloids and the null cone of a Lorentzian four-space.
- Walter Benz, *Classical Geometries in Modern Contexts* (Birkhäuser, 2005), for the neutral signature geometry and the Kleinian quadric.
- I. L. Kantor and A. S. Solodovnikov, *Hypercomplex Numbers: An Elementary Introduction to Algebras* (Springer, 1989), for inner automorphisms and the unitary group of an algebra with conjugation.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, 1997), for the two-sided action of the quaternion sphere and the double cover $Sp(1)\to SO(3)$.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the sandwich action of versors on a Clifford algebra and the doubling of the angle.
