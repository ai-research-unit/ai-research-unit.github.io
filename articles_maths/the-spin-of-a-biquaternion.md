# __The Spin of a Biquaternion__

## Introduction

A biquaternion has no spin. A **carrier** of the algebra has one: the spin is the highest weight of the spin element of a frame pair on that carrier. This article states the definition used throughout the corpus and computes the carriers of $\mathbb{B}$; it also states which spins occur on $\mathbb{B}$ alone. The general setting of carrier, weight and highest weight is *The Weight of a Frame Root and the Spin Quantum Number*.

The output is exact. **The algebra has three elementary carrier types, represented by four spaces, and their spins are $0$, $\tfrac12$ and $1$.** The centre $\mathbb C e_t$ under the adjoint action gives $0$; each Peirce plane $S_\pm=\mathbb B\tilde\Pi_\pm$ under left multiplication gives $\tfrac12$; the traceless part $V=\ker\operatorname{tr}$ under the adjoint action gives $1$. An **elementary carrier** is an isomorphism class of nonzero irreducible invariant subspaces of $\mathbb B$ under one of the two actions, left multiplication or the commutator; the classes are the trivial one, the two-dimensional simple one and the adjoint one, and there is no fourth. Every finite-dimensional associative module of $\mathbb B\cong M_2(\mathbb C)$ is a direct sum of copies of the two-dimensional simple module, so the left action sees only $\tfrac12$. The adjoint action adds the trivial centre and the three-dimensional traceless part, so it sees $0$ and $1$. The complete elementary list of $\mathbb B$ alone is therefore $\{0,\tfrac12,1\}$.

These are also the spins of every observed elementary particle. The Higgs boson is $0$; the six quarks and the six leptons are $\tfrac12$; the photon, the $W^\pm$, the $Z$ and the eight gluons are $1$. No observed elementary particle has any other spin. The match is structural, not predictive: the algebra supplies the three labels, and it does not select the particle content, the masses, the generations or the couplings.

The computation has one further striking output. The spin-$\tfrac12$ structure of the biquaternion is its Peirce frame: the product of the two nilpotents $\vec\Upsilon_x,\vec\Upsilon_y$ splits into a symmetric and an antisymmetric part, and the antisymmetric part $\tilde S_{\vec u}=\tfrac12[\vec\Upsilon_-,\vec\Upsilon_+]$ is the spin element. It and the two nilpotents form an $\mathfrak{sl}_2$ triple, the frame root is twice the spin element, $\tilde\Xi=2\tilde S_{\vec u}$, and the two Peirce planes are its two-dimensional modules for the left action. No extra structure is needed, and no form is used.

The article is organized as follows. §*The Spin Element* defines the Hermitian spin element $\tilde S_{\vec u}$ and its commutator algebra. §*The Spin Triple of the Frame* derives it as the antisymmetric part of the nilpotent product and proves the $\mathfrak{sl}_2$ relations from the Peirce table. §*The Three Elementary Carriers* computes the spin on the spinor, the vector and the centre, and §*The Three and Only Three* proves that no fourth value occurs on $\mathbb B$ alone. §*The Casimir* separates the central element from the Casimir operator. §*The Spin Projectors* and §*The Rotor and the Half-Angle* read the measurement and the rotation. §*Tensor Products and the Roster* gives the spins of the tensor powers. §*The Element on the Carrier* computes the rank of left multiplication on a spinor plane, shows that $N$-degeneracy lowers it without changing the spin, and separates the zero field from the spin-$0$ carrier. §*The Observed Elementary Spins* matches the three values to the particle content. §*The One Definition of Spin* states the definition and the carriers, §*What Is Not a Definition* lists what the word does not name, and §*What the Word Names* separates the four uses of the word.

Throughout $\hbar=1$; the element is $\hbar\tilde S_{\vec u}$, and the operator on a carrier is the action of that element, left multiplication on a spinor or the commutator on the vector. The article uses the product, the Peirce frame and the left and adjoint actions. It uses no form, no norm and no Hilbert structure; the expectation values belong to *$M_2(\mathbb{C})$ Representation : Spin, Qubits and the Bloch Vector*.

## The Spin Element

**For a real unit vector $\vec u$, the spin element is the Hermitian element $\tilde S_{\vec u}=\tfrac12 i\vec u$; it is the antisymmetric part of the product of the two nilpotents of the frame, and half the frame root.**

**Definition.** Let $\vec u=u_x\vec e_x+u_y\vec e_y+u_z\vec e_z$ with real coefficients and $\vec u^2=-e_t$, that is $u_x^2+u_y^2+u_z^2=1$. The **spin element along $\vec u$** is

$$
\tilde S_{\vec u}=\frac{i}{2}\vec u=\frac{1}{2}\bigl(iu_x\vec e_x+iu_y\vec e_y+iu_z\vec e_z\bigr).
$$

The three coordinate elements are $\tilde S_k=\tfrac{i}{2}\vec e_k$. The factor $\tfrac12$ is the antisymmetrisation of the product of the two nilpotents, $\tilde S_{\vec u}=\tfrac12[\vec\Upsilon_-,\vec\Upsilon_+]$, and it is half the frame root $\tilde\Xi$ defined next. The factor $i$ turns the anti-Hermitian unit $\vec e_k$ into a Hermitian element, $\tilde S_{\vec u}^{*}=\tilde S_{\vec u}$.

**The frame root.** The element $\tilde\Xi=2\tilde S_{\vec u}=i\vec u$ is a root of $+1$, since $\tilde\Xi^2=i^2\vec u^2=(-1)(-1)=e_t$. Its idempotents are

$$
\tilde\Pi_+(\vec u)=\frac{e_t+\tilde\Xi}{2}=\frac{e_t+i\vec u}{2},\qquad
\tilde\Pi_-(\vec u)=\frac{e_t-\tilde\Xi}{2}=\frac{e_t-i\vec u}{2},
$$

and the spin element is their half-difference,

$$
\tilde S_{\vec u}=\frac{\tilde\Pi_+(\vec u)-\tilde\Pi_-(\vec u)}{2}.
$$

For $\vec u=\vec e_z$ the pair is the standard pair and $\tilde S_z=\tfrac{i}{2}\vec e_z$.

**The commutator algebra.** In the base the products are $\vec e_j\vec e_k=-\delta_{jk}e_t+\epsilon_{jkl}\vec e_l$, with the cyclic convention $\vec e_x\vec e_y=\vec e_z$. Hence

$$
\tilde S_j\tilde S_k=\tfrac14\delta_{jk}e_t-\tfrac14\epsilon_{jkl}\vec e_l,
$$

and therefore

$$
[\tilde S_j,\tilde S_k]=i\epsilon_{jkl}\tilde S_l,\qquad
\{\tilde S_j,\tilde S_k\}=\tfrac12\delta_{jk}e_t .
$$

The commutator is the angular-momentum algebra of a spin-$\tfrac12$; the anticommutator is the Clifford relation of the same three directions. The commutator is anti-Hermitian and lies in the anti-Hermitian subspace $\mathbb M_-$; the observables $\tilde S_k$ lie in the Hermitian subspace $\mathbb M_+$. The same three directions therefore appear twice, as the generators $\vec e_k$ and as the observables $i\vec e_k$, and the two appearances differ by the factor $i$.

## The Spin Triple of the Frame

**The product of the two nilpotents splits into a symmetric and an antisymmetric part, and the antisymmetric part is the spin element; the two nilpotents and the spin element form the canonical triple of the frame.**

**Definition.** Let $\tilde\Pi_\pm$ be a complete pair, $\tilde\Xi=\tilde\Pi_+-\tilde\Pi_-$, and let $\vec\Upsilon_-\in\mathbb B_{+-}$ and $\vec\Upsilon_+\in\mathbb B_{-+}$ be the normalised nilpotents, $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$ and $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$. The **spin pair of the frame** is $(\vec\Upsilon_-,\vec\Upsilon_+)$, and its **spin element** is the antisymmetric part of the product,

$$
\tilde S_{\vec u}=\tfrac12\bigl(\vec\Upsilon_-\vec\Upsilon_+-\vec\Upsilon_+\vec\Upsilon_-\bigr)=\tfrac12[\vec\Upsilon_-,\vec\Upsilon_+].
$$

The **spin triple of the frame** is $(\tilde S_{\vec u},\vec\Upsilon_-,\vec\Upsilon_+)$. Since $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$ and $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$, the spin element is the half-difference of the two idempotents, $\tilde S_{\vec u}=\tfrac12(\tilde\Pi_+-\tilde\Pi_-)=\tfrac12\tilde\Xi$. For the standard frame, $\tilde\Xi=i\vec e_z$, and the nilpotents are $\vec\Upsilon_x$ and $\vec\Upsilon_y$.

**Theorem.** The triple is a spin triple in the sense of §*The One Definition of Spin*:

$$
[\tilde S_{\vec u},\vec\Upsilon_-]=\vec\Upsilon_-,\qquad [\tilde S_{\vec u},\vec\Upsilon_+]=-\vec\Upsilon_+,\qquad [\vec\Upsilon_-,\vec\Upsilon_+]=2\tilde S_{\vec u}.
$$

In the doubled notation of the Peirce tables, with $\tilde\Xi=2\tilde S_{\vec u}$, the same relations read $[\tilde\Xi,\vec\Upsilon_-]=2\vec\Upsilon_-$, $[\tilde\Xi,\vec\Upsilon_+]=-2\vec\Upsilon_+$ and $[\vec\Upsilon_-,\vec\Upsilon_+]=\tilde\Xi$.

*Proof.* The corner signs give $\tilde\Xi\vec\Upsilon_-=\vec\Upsilon_-$ and $\vec\Upsilon_-\tilde\Xi=-\vec\Upsilon_-$, so $[\tilde\Xi,\vec\Upsilon_-]=2\vec\Upsilon_-$ and hence $[\tilde S_{\vec u},\vec\Upsilon_-]=\vec\Upsilon_-$. The second relation is the same computation on $\mathbb B_{-+}$, $[\tilde S_{\vec u},\vec\Upsilon_+]=-\vec\Upsilon_+$. The third is the normalised Peirce product, $[\vec\Upsilon_-,\vec\Upsilon_+]=\vec\Upsilon_-\vec\Upsilon_+-\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_+-\tilde\Pi_-=2\tilde S_{\vec u}$.

**Remark (normalisation).** The pair is not unique. The reciprocal rescaling $\vec\Upsilon_-\mapsto\mu\vec\Upsilon_-$, $\vec\Upsilon_+\mapsto\mu^{-1}\vec\Upsilon_+$ preserves the two products and hence the three relations. What is canonical is $\tilde S_{\vec u}$ and the unordered pair of nilpotent lines. The product is nonzero, $[\vec\Upsilon_-,\vec\Upsilon_+]=\tilde\Xi\neq0$, because a complete pair has $\tilde\Pi_+\neq\tilde\Pi_-$: $\tilde\Pi_+\tilde\Pi_-=0$ and $\tilde\Pi_++\tilde\Pi_-=e_t$. The pair therefore meets the nonzero condition of *The General Definition of Spin*.

**Remark (the spin element and the root).** The frame root is twice the spin element, $\tilde\Xi=2\tilde S_{\vec u}$. On a carrier the eigenvalues of $\tilde S_{\vec u}$ are the weights, and $j$ is the highest; the eigenvalues of $\tilde\Xi$ are twice the weights. The doubled form $\tilde\Xi$ is the one in which the frame root and the Peirce idempotents are written, and in the principal chains of $M_n$ it gives integer weights; it is the same triple, with $H=2S$ in the notation of the general article.

**The ladder on the spinor.** On $S_+=\mathbb B\tilde\Pi_+$, with the couple $(\tilde\Pi_+,\vec\Upsilon_+)$ as basis, the left multiplications are

$$
L_{\tilde\Xi}=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
L_{\vec\Upsilon_-}=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
L_{\vec\Upsilon_+}=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
$$

The weights of $L_{\tilde\Xi}$ are $\pm1$, so the weights of $L_{\tilde S_{\vec u}}$ are $\pm\tfrac12$. The operator $L_{\vec\Upsilon_-}$ raises the nilpotent to the idempotent and $L_{\vec\Upsilon_+}$ lowers the idempotent to the nilpotent. The same two matrices act on $S_-=\mathbb B\tilde\Pi_-$ in the couple $(\vec\Upsilon_-,\tilde\Pi_-)$, with the two basis vectors exchanged in their roles.

**Remark (the triple is the frame).** This is the precise sense in which spin is native to the biquaternion: the two nilpotents that give the Peirce coordinates are the ladder operators, and the antisymmetric part of their product, half the root that labels the pair, is the Cartan generator. The spin-$\tfrac12$ of the algebra is not an add-on; it is the frame read as a Lie triple.

## The Three Elementary Carriers

**The algebra has three elementary carrier types: the two spinor planes with weights $\pm\tfrac12$ of $\tilde S_{\vec u}$, the traceless part with weights $+1,0,-1$, and the centre with weight $0$.**

Three natural actions occur — left multiplication, right multiplication and the commutator — but the right action repeats the left one. In this article dimensions are complex: the centre has complex dimension one, the plane two, the traceless part three; over the reals they are two, four and six. The physical scalar and vector are real forms of the centre and of the traceless part. Left multiplication is associative and carries each spinor plane into itself; the commutator is a Lie action and carries the traceless part and the centre into themselves; right multiplication by the root is constant on each plane, $+1$ on $S_+$ and $-1$ on $S_-$, and reads the same simple module from the other side, so it adds no carrier type. The readings of the same eight real dimensions are collected in the table of §*The Table*.

### The Spinor

**The plane $S_+=\mathbb B\tilde\Pi_+$ is a spin-$\tfrac12$ carrier, and so is $S_-$.**

On $S_+$ the operator $L_{\tilde S_{\vec u}}$ has the two weights $+\tfrac12$ on $\tilde\Pi_+$ and $-\tfrac12$ on $\vec\Upsilon_+$; the weights of $L_{\tilde\Xi}$ are their doubles, $+1$ and $-1$. The highest weight is $\tfrac12$, so $j=\tfrac12$, and the dimension is $2j+1=2$. The two weight lines are one-dimensional, and the ladder of §*The Spin Triple of the Frame* joins them, so the carrier is irreducible. The same computation on $S_-$ gives the weights $+\tfrac12$ on $\vec\Upsilon_-$ and $-\tfrac12$ on $\tilde\Pi_-$.

**Remark (the two planes are isomorphic).** The two planes are distinct subspaces, but they are isomorphic as left modules: the exchange of §*Right Multiplication* of *Spinors as Peirce Coordinates in the Biquaternion Algebra* is a bijection and commutes with the left action. The left regular module therefore decomposes as

$$
\mathbb B=S_+\oplus S_-=2\cdot\tfrac12 .
$$

### The Vector

**The traceless part $V=\mathbb B_{+-}\oplus\mathbb C\tilde\Xi\oplus\mathbb B_{-+}$ is a spin-$1$ carrier for the commutator.**

The space $V$ is the pure part, the kernel of the trace, of complex dimension three. On the basis $(\vec\Upsilon_-,\tilde\Xi,\vec\Upsilon_+)$ the commutator $\mathrm{ad}_{\tilde S_{\vec u}}$ is diagonal with weights $+1,0,-1$: the spin element acts on the two nilpotents by $\pm1$ and on the root by $0$. The highest weight is $1$, so $j=1$, and the dimension is $3$. The ladder is $\mathrm{ad}_{\vec\Upsilon_-}$ raising and $\mathrm{ad}_{\vec\Upsilon_+}$ lowering.

The space $V$ is not a Peirce corner and not an associative module: left multiplication by $\tilde\Pi_+$ sends $\tilde\Xi$ to $\tilde\Pi_+$, which has trace one. It is a module for the Lie triple only, and that is the carrier on which the integer spin lives.

### The Centre

**The centre $\mathbb C_{\mathbb B}=\mathbb C e_t$, the real span of $e_t$ and $ie_t$, is the spin-$0$ carrier.**

Every inner derivation annihilates the centre, so $\mathrm{ad}_{\tilde S_{\vec u}}=0$ there and the only weight is $0$. The highest weight is $0$, so $j=0$, and the dimension is one. A scalar field with no internal quantum number can be placed here. The physical Higgs is a Lorentz scalar, but it also carries electroweak quantum numbers that the centre does not supply.

### The Table

| carrier | action | complex dimension | weights of $\tilde S_{\vec u}$ | $j$ | Casimir |
|---|---|---|---|---|---|
| $S_+$ | $L$ | $2$ | $+\tfrac12,-\tfrac12$ | $\tfrac12$ | $\tfrac34$ |
| $S_-$ | $L$ | $2$ | $+\tfrac12,-\tfrac12$ | $\tfrac12$ | $\tfrac34$ |
| $V$ | $\mathrm{ad}$ | $3$ | $+1,0,-1$ | $1$ | $2$ |
| $\mathbb C_{\mathbb B}$ | $\mathrm{ad}$ | $1$ | $0$ | $0$ | $0$ |

**Remark (why the two readings differ by a factor two).** On the spinor the spin element $\tilde S_{\vec u}$ has weights $\pm\tfrac12$ under left multiplication; on the traceless part it has weights $+1,0,-1$ under the commutator. The half-integer spin is the left module, the integer spin the adjoint module. The factor two is the shift $L_{\tilde\Xi}=\mathrm{ad}_{\tilde\Xi}+R_{\tilde\Xi}$ of *The Weight of a Frame Root and the Spin Quantum Number*, read with $\tilde\Xi=2\tilde S_{\vec u}$: on the mixed corners the right weight is the negative of the left weight, so the commutator weight is twice the left weight; on the diagonal corners the two weights are equal, so the commutator weight vanishes. The shift explains the weights inside a plane. It does not by itself produce the vector: $V$ is the traceless part of $S\otimes S^{*}$, the adjoint of the defining module, and that is why its string is $+1,0,-1$ on the spin element, rather than a shifted spinor string.

**Remark (the two readings are not two decompositions of one module).** The left regular module is $S_+\oplus S_-$, of complex dimension four; the adjoint module is $V\oplus\mathbb C_{\mathbb B}$, also of complex dimension four. They are different actions on the same eight real dimensions. Only the first is an associative module; only the second contains the vector carrier.

## The Three and Only Three

**On $\mathbb B$ alone the elementary spins are exactly $0$, $\tfrac12$ and $1$. No fourth value occurs, and the reason is the module structure of $M_2(\mathbb C)$ together with the adjoint decomposition.**

**Definition (elementary carrier).** An **elementary carrier** of $\mathbb B$ is an isomorphism class of nonzero irreducible invariant subspaces of $\mathbb B$ under one of the two actions: left multiplication $L$ (associative) or the commutator $\mathrm{ad}$ (Lie). Two subspaces define the same carrier when the actions are isomorphic. *On $\mathbb B$ alone* means that the space is a subspace of $\mathbb B$ and the action is the restriction of one of these two. A general Lie-algebra module, such as the four-dimensional irreducible module of $\mathfrak{sl}_2(\mathbb C)$, is not of this form: its action is not the restriction of $\mathrm{ad}$ to a subspace of $\mathbb B$.

**The associative action sees only $\tfrac12$.** The algebra is simple, $\mathbb B\cong M_2(\mathbb C)$, so it has one isomorphism class of simple modules, of complex dimension two. Every finite-dimensional left module is a direct sum of copies of it. On the simple module the spin element $\tilde S=h/2$ is a traceless $2\times2$ matrix with $(2\tilde S)^{2}=1$; the weights of $\tilde S$ are $\pm\tfrac12$, and $j$ is the highest of them, $\tfrac12$. A unital one-dimensional module would be a unital algebra map $M_2(\mathbb C)\to\mathbb C$. Its kernel is a two-sided ideal, so by simplicity it is $0$ or the whole algebra; neither is possible for a unital map into a one-dimensional algebra. Hence no one-dimensional module exists, and $j=0$ is not available to the left action.

**The adjoint action adds $0$ and $1$.** As a Lie algebra, $\mathbb B=\mathbb C e_{t}\oplus V$ with $V=\ker\operatorname{tr}\cong\mathfrak{sl}_2(\mathbb C)$. The centre is trivial, so $j=0$. The traceless part is the three-dimensional irreducible module, with weights $+1,0,-1$ under $\mathrm{ad}_{h/2}$, so $j=1$. The adjoint action has no other irreducible invariant subspace.

**The right action adds nothing.** On $S_+$ the right action is the constant $R_{h}=+1$, that is $R_{\tilde S}=+\tfrac12$; on $S_-$ it is $R_{h}=-1$, that is $R_{\tilde S}=-\tfrac12$. The right regular module is the same two-dimensional simple module read from the other side, so the right action adds no carrier type and no value of $j$.

**The union.** The left action has one irreducible type: every minimal left ideal is isomorphic to $S_+=\mathbb B\tilde\Pi_+$, so $S_+$ and $S_-$ are two representatives of one carrier. The adjoint action has two irreducible types: the centre $\mathbb C_{\mathbb B}$ and the traceless part $V$. The algebra $\mathbb B$ itself is reducible under both, so it is not elementary. The elementary carriers are therefore the trivial, the two-dimensional simple and the adjoint, with $j=0$, $\tfrac12$ and $1$, and there are no others. Hence the elementary list is
$$
\{0,\tfrac12,1\},
$$
and no other value occurs on $\mathbb B$ alone. Higher spin is not forbidden; it is simply not elementary. It requires a tensor product or a larger algebra, and it is treated in §*Tensor Products and the Roster* and in the physics article *Higher Spin from Tensor Products*.

**What the list does not say.** It does not say that a particle of each spin exists, nor which particle has which spin. It says that if a field is placed on an elementary carrier of $\mathbb B$, its spin is one of the three, and that the three carrier types are exhausted.

## The Casimir

**The element $\tilde S_x^2+\tilde S_y^2+\tilde S_z^2$ is central and equals $\tfrac34 e_t$; the Casimir operator is the sum of the squares of the action, and it equals $j(j+1)$ on an irreducible carrier.**

Each coordinate operator squares to $\tfrac14 e_t$, because $(i\vec e_k)^2=i^2\vec e_k^2=(-1)(-1)=e_t$. Hence

$$
\tilde S_x^2+\tilde S_y^2+\tilde S_z^2=\tfrac34 e_t .
$$

The sum is a central element, and it acts by the scalar $\tfrac34$ on every carrier, whatever the action. It is therefore not the Casimir operator: the Casimir is the operator $\sum_k\rho(\tilde S_k)^2$, and it depends on the action $\rho$.

| carrier | action | $\sum_k\rho(\tilde S_k)^2$ | $j(j+1)$ |
|---|---|---|---|
| $S_\pm$ | $L$ | $\tfrac34\,\mathrm{id}$ | $\tfrac34$ |
| $V$ | $\mathrm{ad}$ | $2\,\mathrm{id}$ | $2$ |
| $\mathbb C_{\mathbb B}$ | $\mathrm{ad}$ | $0$ | $0$ |

**Remark (the coincidence on the spinor).** On the spinor the Casimir operator equals multiplication by the central element, because the spinor is the defining representation of the triple and $\tfrac34$ is its Casimir eigenvalue. On the vector the two numbers separate: the central element still acts by $\tfrac34$, while the Casimir operator acts by $2$. The equality is a property of the fundamental representation, not an identity of the algebra.

## The Spin Projectors

**Left multiplication by the two idempotents of the direction is the spectral decomposition of the spin operator; the projectors are the idempotents themselves, and no form is needed.**

**Theorem.** On $S_+(\vec u)=\mathbb B\tilde\Pi_+(\vec u)$, the operators $L_{\tilde\Pi_+(\vec u)}$ and $L_{\tilde\Pi_-(\vec u)}$ are the spectral projectors of $L_{\tilde S_{\vec u}}$ for the eigenvalues $+\tfrac12$ and $-\tfrac12$.

*Proof.* The operator $L_{\tilde S_{\vec u}}=\tfrac12(L_{\tilde\Pi_+}-L_{\tilde\Pi_-})$ and the sum $L_{\tilde\Pi_+}+L_{\tilde\Pi_-}=L_{e_t}$ is the identity. Each $L_{\tilde\Pi_\pm}$ is idempotent, because $\tilde\Pi_\pm^2=\tilde\Pi_\pm$, and the two images are the lines $\mathbb C\tilde\Pi_+$ and $\mathbb C\vec\Upsilon_+$, which are the weight spaces of $L_{\tilde\Xi/2}$. A pair of complementary idempotents with these two images is the spectral pair.

**The standard frame.** In the couple $(\tilde\Pi_+,\vec\Upsilon_+)$ the two projectors are $\operatorname{diag}(1,0)$ and $\operatorname{diag}(0,1)$.

**A tilted direction.** Take $\vec u=(\vec e_x+\vec e_z)/\sqrt2$ and the standard carrier $S_+(\vec e_z)$. In the couple $(\tilde\Pi_+,\vec\Upsilon_y)$ the projector $L_{\tilde\Pi_+(\vec u)}$ is

$$
\frac{1}{4}\begin{pmatrix}2+\sqrt2&\sqrt2\\ \sqrt2&2-\sqrt2\end{pmatrix}
=\begin{pmatrix}0.8536&0.3536\\ 0.3536&0.1464\end{pmatrix}.
$$

The matrix is idempotent, symmetric, and its complement $L_{\tilde\Pi_-(\vec u)}$ is the other projector; the two sum to the identity. The entries are the algebraic form of the spin-up projector along the tilted direction, computed with no form.

**Remark (the opposite direction).** At $\vec u=-\vec e_z$ the two idempotents exchange, $\tilde\Pi_+(-\vec e_z)=\tilde\Pi_-(\vec e_z)$ and $\tilde\Pi_-(-\vec e_z)=\tilde\Pi_+(\vec e_z)$. The two projectors exchange their images, so the $+\tfrac12$ eigenspace of $L_{\tilde S_{-\vec e_z}}$ is the old $-\tfrac12$ line, and conversely. The spectral statement is read with the labels of the direction; the exchange is the reversal of the spin labels.

**What the projector does not give.** An expectation value requires a state and a form: the spinor adjoint of *Peirce Carriers and Inner Conjugation*, the normalisation, and the trace pairing. The projector is the algebraic half of the measurement; the probability is the metric half, and it belongs to *$M_2(\mathbb{C})$ Representation : Spin, Qubits and the Bloch Vector*.

## The Rotor and the Half-Angle

**The rotor $\exp(\tfrac{\theta}{2}\vec u)$ acts on the spinor by $\exp(-i\theta L_{\tilde S_{\vec u}})$ and on the vector by $\mathrm{Ad}_{\tilde u(\theta)}=\exp(-i\theta\,\mathrm{ad}_{\tilde S_{\vec u}})$; the exponent is the weight of the spin operator on the carrier, so the half-angle is a consequence, not a definition.**

Let $\tilde u(\theta)=\exp(\tfrac{\theta}{2}\vec u)=\cos\tfrac{\theta}{2}+\sin\tfrac{\theta}{2}\,\vec u$. Since $\vec u=-2i\tilde S_{\vec u}$,

$$
L_{\tilde u(\theta)}=\exp\!\left(\tfrac{\theta}{2}L_{\vec u}\right)=\exp\!\left(-i\theta L_{\tilde S_{\vec u}}\right).
$$

On $S_+$ the eigenvalues of $L_{\tilde S_{\vec u}}$ are $\pm\tfrac12$, so those of $L_{\tilde u(\theta)}$ are $e^{\mp i\theta/2}$. On $V$ the eigenvalues of $\mathrm{ad}_{\tilde S_{\vec u}}$ are $+1,0,-1$, so those of $\mathrm{Ad}_{\tilde u(\theta)}$ are $e^{\mp i\theta},1$.

**The half-angle is the exponential of the weight, not the spin.** The exponent in $L_{\tilde u}$ is $\theta/2$ because the weight of $L_{\tilde S}$ is $\tfrac12$; on the vector the weight is $1$ and the exponent is $\theta$. The same rotor has two exponents on two carriers. The half-angle is not a property of the rotor alone and it is not the spin quantum number; it is the exponential coordinate of the weight on the carrier.

**The double cover.** At $\theta=2\pi$ the rotor is $-e_t$; it acts on the spinor by $L_{\tilde u(2\pi)}=-\mathrm{id}$ and on the vector by $\mathrm{Ad}_{\tilde u(2\pi)}=\mathrm{id}$. The sign is the central sign of the double cover, visible on the spinor and invisible on the vector. The two periods separate the half-integer from the integer carriers; the spin-statistics theorem is not a consequence of the algebra and is treated with the physics.

## Tensor Products and the Roster

**Tensor products of the elementary carriers give the higher spins; on $\mathbb B$ itself the elementary carriers carry only $0,\tfrac12,1$.**

The tensor products are taken for the Lie triple, with $X\cdot(\xi\otimes\eta)=X\xi\otimes\eta+\xi\otimes X\eta$; they are not modules over the associative algebra, which has no coproduct. The weights of the spin element $\tilde S=\tilde\Xi/2$ add, and the weight string of the product is the sum of the strings of the factors.

| product | complex dimension | decomposition | spins |
|---|---|---|---|
| $S_+\otimes S_+$ | $4$ | $V\oplus\mathbb C_{\mathbb B}$ | $1,0$ |
| $S_+\otimes V$ | $6$ | $W_{3/2}\oplus W_{1/2}$ | $\tfrac32,\tfrac12$ |
| $V\otimes V$ | $9$ | $W_2\oplus V\oplus\mathbb C_{\mathbb B}$ | $2,1,0$ |

The check is the weight string. For $S_+\otimes V$ the sums are

$$
\{\tfrac12,-\tfrac12\}+\{1,0,-1\}
=\{\tfrac32,\tfrac12,-\tfrac12,-\tfrac32\}\cup\{\tfrac12,-\tfrac12\},
$$

which is the string of a spin-$\tfrac32$ together with the string of a spin-$\tfrac12$. For $V\otimes V$ the nine sums are

$$
\{2,1,0\}\cup\{1,0,-1\}\cup\{0,-1,-2\},
$$

which is the string of a spin-$2$, a spin-$1$ and a spin-$0$. For $S_+\otimes S_+$ the four sums are $\{1,0,0,-1\}$, the string of a spin-$1$ and a spin-$0$.

**The algebra.** The left regular module is $2\cdot\tfrac12$ and the adjoint module is $1\oplus0$. Neither contains a spin-$\tfrac32$; the first higher spin appears in $S_+\otimes V$. The reason is that the elementary carriers of $\mathbb B$ are exhausted by the two planes, the traceless part and the centre: as an associative algebra $\mathbb B\cong M_2(\mathbb C)$ has one irreducible module, the spinor, and the triple generates an $\mathfrak{sl}_2$ whose finite-dimensional modules are the symmetric powers of the spinor. Higher spin is a property of a tensor power, that is of a larger algebra, not of $\mathbb B$.

## The Element on the Carrier: Norm, Rank and the Null Cone

**The root fixes the weights. The element $\tilde Q$ fixes the eigenvalues of $L_{\tilde Q}$, and its norm fixes the rank. The two are independent, and only the second changes on the null cone.**

**Setting.** Let
$$
N(\tilde Q)=Q_t^{2}+B^{2},\qquad B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2},
$$
so that $\tilde Q$ is **$N$-regular** when $N(\tilde Q)\neq0$ and **$N$-degenerate** when $N(\tilde Q)=0$. The spectrum is **regular** when $B^{2}\neq0$ and **degenerate** when $B^{2}=0$. In the $M_2(\mathbb{C})$ model $N$ is the determinant and $B^{2}$ is the discriminant of the characteristic polynomial.

**The matrix on a spinor plane.** In the basis $(\tilde\Pi_+,\vec\Upsilon_+)$ of $S_+$, left multiplication by $\tilde Q$ is
$$
L_{\tilde Q}\tilde\Pi_+ = Q_{++}\tilde\Pi_+ + Q_{-+}\vec\Upsilon_+,
\qquad
L_{\tilde Q}\vec\Upsilon_+ = Q_{+-}\tilde\Pi_+ + Q_{--}\vec\Upsilon_+,
$$
so
$$
\mathsf L_+=\begin{pmatrix}Q_{++}&Q_{+-}\\ Q_{-+}&Q_{--}\end{pmatrix},
\qquad
\det\mathsf L_+=Q_{++}Q_{--}-Q_{+-}Q_{-+}=N(\tilde Q).
$$
The same matrix occurs in the basis $(\vec\Upsilon_-,\tilde\Pi_-)$ of $S_-$. The determinant is the invariant, so the statement does not depend on the basis.

**Theorem (rank on a spinor plane).** For $\tilde Q\neq0$,
$$
\operatorname{rank}\bigl(L_{\tilde Q}|_{S_+}\bigr)
=\operatorname{rank}\bigl(L_{\tilde Q}|_{S_-}\bigr)
=\begin{cases}2,& N(\tilde Q)\neq0,\\ 1,& N(\tilde Q)=0.\end{cases}
$$
On the whole algebra the rank of $L_{\tilde Q}$ is $4$ in the $N$-regular case and $2$ in the $N$-degenerate case. At $\tilde Q=0$ all the ranks are $0$.

*Proof.* The determinant of a square matrix is nonzero exactly when the matrix is invertible, and $\det\mathsf L_+=N$. A nonzero singular $2\times2$ matrix has rank one. On $\mathbb B$ the map $L_{\tilde Q}$ is invertible exactly when $\tilde Q$ is a unit, and in $\mathbb B\cong M_2(\mathbb{C})$ this is exactly $N(\tilde Q)\neq0$; a nonzero singular matrix acts on $M_2(\mathbb{C})$ by left multiplication with rank $2$.

**The sandwich.** The Hermitian sandwich $\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$ has rank $4$ for $N$-regular $\tilde Q$. For nonzero $N$-degenerate $\tilde Q$ it has rank $1$ and its image is a null line, as computed in *The Two-Sided Operator of a N-Degenerate, Spectrally Regular Biquaternion* and in its spectrally degenerate companion. The right factor does not preserve the spinor planes, so this rank is not twice the rank on a plane; the two-sided collapse is stronger than the one-sided one.

**The vector carrier behaves differently.** On $V=\ker\operatorname{tr}$ the commutator $\mathrm{ad}_{\tilde Q}$ has rank $2$ for every non-central $\tilde Q$, whether $N$-regular or not, and rank $0$ exactly when $\tilde Q$ is central. The rank drop on the null cone is therefore a property of the spinor action alone: it is the disappearance of one of the two components of the spinor, not a change of carrier.

**The quantity that is $1$ and $\tfrac12$.** Half the rank,
$$
\frac12\operatorname{rank}\bigl(L_{\tilde Q}|_{S_\pm}\bigr),
$$
is $1$ on the $N$-regular set, $\tfrac12$ on the nonzero null cone and $0$ at $\tilde Q=0$. This is the quantity that varies between $1$ and $\tfrac12$ across the cone, and it is **not** the spin.

The reason is that the weights are those of the spin element. The commutation relations
$$
[\tilde S_{\vec u},\tilde\Pi_\pm]=0,\qquad
[\tilde S_{\vec u},\mathbb B_{+-}]=\mathbb B_{+-},\qquad
[\tilde S_{\vec u},\mathbb B_{-+}]=-\mathbb B_{-+}
$$
contain no $\tilde Q$. Hence for every $\tilde Q$, the eigenvalues of $L_{\tilde S_{\vec u}}$ on $S_\pm$ are $+\tfrac12$ and $-\tfrac12$, and the spin is $\tfrac12$ on both sides of the cone. A null spinor with one nonzero component still has weight $+\tfrac12$ or $-\tfrac12$; it has one component, not another spin. Half the rank counts the components; the highest weight gives the spin.

**The zero field is not spin $0$.** At $\tilde Q=0$ the half-rank is $0$, but the carrier is still $S_\pm$ with $j=\tfrac12$. Spin $0$ is the centre $\mathbb C_{\mathbb B}$ under the adjoint action, where the highest weight itself vanishes. The two zeros have different causes: one is a vanishing element, the other a trivial action.

**The four sectors.** The two conditions cut $\mathbb B$ into the four cells of *The N-Regular, Spectrally Regular Sector* and its companions. With $\tilde Q\neq0$:

| sector | $N$ | $B^{2}$ | $\operatorname{rank}L_{\tilde Q}|_{S_\pm}$ | $\operatorname{rank}\mathrm{ad}_{\tilde Q}|_{V}$ | $j$ on $S_\pm$ |
|---|---|---|---|---|---|
| $\Sigma_{11}$ | $\neq0$ | $\neq0$ | $2$ | $2$ | $\tfrac12$ |
| $\Sigma_{10}$ | $\neq0$ | $0$ | $2$ | $2$ | $\tfrac12$ |
| $\Sigma_{01}$ | $0$ | $\neq0$ | $1$ | $2$ | $\tfrac12$ |
| $\Sigma_{00}$ | $0$ | $0$ | $1$ | $2$ | $\tfrac12$ |

The rank columns are what the sectors change. The spin column is constant.

## The Observed Elementary Spins

**The three values match the spins of all observed elementary particles.**

| spin | established elementary particles | count |
|---|---|---|
| $0$ | Higgs boson $H$ | $1$ |
| $\tfrac12$ | quarks $u,d,c,s,t,b$; leptons $e,\mu,\tau,\nu_{e},\nu_{\mu},\nu_{\tau}$ | $12$ |
| $1$ | photon $\gamma$; $W^{+},W^{-},Z$; eight gluons $g$ | $12$ |

The quarks and the gluons are counted although they are observed only as confined constituents of hadrons and jets, never as free particles. No observed elementary particle carries another spin. The spin-$2$ graviton is not an observed particle; it is the quantum of the metric and it belongs to the tensor-square construction of *Tensor Products and the Roster*, not to $\mathbb B$ alone. Hadrons are bound states of quarks and gluons, not elementary particles: the $\Delta(1232)$ and the $\Omega^-$ have spin $\tfrac32$, the tensor mesons spin $2$, and the $N(1680)$ spin $\tfrac52$.

Five boundaries keep the match honest.

- **The match is a label match.** The Standard Model assigns the spins by hand. The algebra reproduces the set $\{0,\tfrac12,1\}$ and does not predict which particle has which spin, nor the masses, the generations, the charges or the colours.
- **The massless spin-$1$ count is two, not three.** The carrier $V$ has three states. For a massless vector field the longitudinal state is removed by gauge invariance, leaving the two helicities of the photon and the gluon. The algebra supplies the triplet; the massless restriction is a separate physical input, treated in *Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form*.
- **The weak chirality is not the Peirce index.** The two Peirce planes $S_\pm$ are isomorphic as left modules, so the left action does not distinguish them. The chirality that the weak interaction couples to is the Lorentz chirality, not the copy index.
- **Spin here is the rotation spin.** The number $j$ is the highest weight of the rotation generator $\tilde S_{\vec u}=\tilde\Xi/2$ for the subgroup $\mathrm{Spin}(3)\subset\mathbb B^{\times}$. The full Lorentz label is a pair $(j_L,j_R)$, and the massless case uses helicity. The table uses the rotation spin, which is the standard particle-data label.
- **Spin–statistics is not derived.** The half-integer carriers are associative modules and the integer carriers are adjoint modules, but the link from that split to Fermi and Bose statistics is an independent theorem, treated in *The Spin–Statistics Theorem in Biquaternionic Form*.

**What is claimed.** The set of elementary carrier spins of $\mathbb B$ is exactly the set of spins that have been observed for elementary particles. That is a structural alignment of the algebra with the observed spectrum. It is not a derivation of the spectrum.

## The One Definition of Spin

**The corpus has one definition of spin. Every other use of the word is the name of an element, of a carrier, or of a physical interpretation of the number that the definition supplies.**

**Definition (spin pair).** Let $\mathcal A$ be a complex algebra; for a real algebra $A$, take $\mathcal A=A\otimes_{\mathbb R}\mathbb{C}$. A **spin pair** of $\mathcal A$ is a pair $(U,V)$ of elements with

$$
[U,V]\neq0,\qquad [[U,V],U]=2U,\qquad [[U,V],V]=-2V .
$$

The letters $U,V$ here name the two ladder generators; they are not the carrier written $V$ in §*One Definition, Several Carriers*.

**Definition (spin element).** The **spin element** of the pair is its antisymmetric part,

$$
S=\tfrac12(UV-VU)=\tfrac12[U,V].
$$

The three relations $[S,U]=U$, $[S,V]=-V$ and $[U,V]=2S$ follow, and $(S,U,V)$ is the **spin triple** of the pair. Conversely, a triple with these three relations and $S\neq0$ is the triple of a spin pair.

**Definition (carrier, spin).** A **carrier** is a finite-dimensional complex module $(W,\rho)$ of $\mathcal A$, associative or Lie, whose restriction to the triple is a representation of $\mathfrak{sl}_2$. The **weights** of the carrier are the eigenvalues of $\rho(S)$. The **spin** of the carrier is

$$
\boxed{\;j=\lambda_{\max}\bigl(\rho(S)\bigr)=\max\operatorname{spec}\rho(S)\;}
$$

For an irreducible module the weight string is $j,j-1,\dots,-j$, so $\lambda_{\max}=-\lambda_{\min}=j$. Over $\mathbb{C}$ every finite-dimensional $\mathfrak{sl}_2$ module is completely reducible, so the highest-weight decomposition is automatic and no hypothesis on $W$ is needed beyond the triple and the representation.

**Remark (the nonzero condition).** If $[U,V]=0$, the antisymmetric part of the product vanishes and there is no spin element. The double-commutator conditions then force $U=V=0$: $[[U,V],U]=0=2U$ and $[[U,V],V]=0=-2V$. The zero pair is the zero representation of $\mathfrak{sl}_2$, not a spin structure, and the single condition $[U,V]\neq0$ excludes it.

**Remark (central element).** If a candidate spin element $s$ is central in $\mathcal A$, no spin pair has spin element $s$: centrality gives $[s,u]=0$ for every $u$, so $[s,u]=u$ forces $u=0$, and then $[u,v]=2s$ forces $s=0$. The eigenvalues of $\rho(s)$ are then all equal, the weight string is constant, and there is no spin. This is what excludes the idempotents $e=0$ and $e=e_t=1$: their frame roots $h=\mp1$ are central, so the candidates $s=h/2=\mp\tfrac12$ carry no pair and the formal values $j=\mp\tfrac12$ are not spins.

**Remark (reducible carrier).** For a reducible $W$ the number $j$ is the maximum over the irreducible summands; the full invariant is the multiset of their highest weights. The left regular module, for instance, is $2\cdot\tfrac12$: the weights of $\tilde S_{\vec u}$ are $+\tfrac12,-\tfrac12,+\tfrac12,-\tfrac12$, $j=\tfrac12$, and the multiset of highest weights is $\{\tfrac12,\tfrac12\}$.

**Proposition (frame root).** Let $e$ be an idempotent of $\mathbb{B}$ with frame root $h=2e-e_t$. If $(h/2,u,v)$ is a spin triple, then the spin is $j=\lambda_{\max}(\rho(h/2))$, and $h/2$ is the spin element. For $e=0$ and $e=e_t$ the root $h=\mp1$ is central and there is no pair.

**Proposition (principal chain).** For $M_n(\mathbb{C})$, let $J_3=\sum_{k=1}^{n}\bigl(\tfrac{n+1}{2}-k\bigr)E_{kk}$, $J_+=\sum_{k=1}^{n-1}\sqrt{k(n-k)}\,E_{k,k+1}$ and $J_-=\sum_{k=1}^{n-1}\sqrt{k(n-k)}\,E_{k+1,k}$. The triple $(J_3,J_+,J_-)$ is a spin triple, with $[J_3,J_\pm]=\pm J_\pm$ and $[J_+,J_-]=2J_3$. It is not a frame root for $n>2$: $J_3$ has eigenvalues $(n-1)/2,(n-3)/2,\dots,-(n-1)/2$, while a frame root $2e-e_t$ has eigenvalues $\pm1$ only. On the defining carrier $\mathbb{C}^n$ the spin is $(n-1)/2$; on the adjoint it is $0,1,\dots,n-1$ on $\mathrm{gl}_n$ and $1,\dots,n-1$ on $\mathfrak{sl}_n$.

**Remark (the balanced Peirce triple).** For even $n$ and an idempotent of rank $r=n/2$, the Peirce root $h$ is traceless and $h/2$ closes to a spin triple different from the principal one. Its adjoint carrier decomposes as $r^2(V_1\oplus V_0)$: the $r^2$ vectors of weight $+1$ generate $r^2$ copies of $V_1$, and the weight-$0$ space has dimension $2r^2$, of which $r^2$ vectors are the lowers of the $V_1$'s and $r^2$ are the highest weights of the $V_0$'s. The defining carrier is $r\cdot\tfrac12$, so the elementary spins are again $0,\tfrac12,1$. At $n=2$, $r=1$ and the decomposition is $V_1\oplus V_0$, the biquaternion case.

This is the only definition of spin in the corpus. The element $S$ is the **spin operator**: its eigenvalues are the weights, and its highest eigenvalue is $j$. The phrase "the spin of the electron" is the physics name for the number $j$ of the carrier that describes the electron; it is an interpretation of $j$, not a second definition.

**Remark (why the antisymmetric part).** For the frame, the spin element is $\tilde S_{\vec u}=\tfrac12[\vec\Upsilon_-,\vec\Upsilon_+]$, the antisymmetric part of the nilpotent product. The symmetric part is $\tfrac12\{\vec\Upsilon_-,\vec\Upsilon_+\}=\tfrac12(\tilde\Pi_++\tilde\Pi_-)=\tfrac12 e_t$, a central scalar with no weight. The antisymmetric part is therefore the whole weight content of the product, and the factor $\tfrac12$ is the antisymmetrisation, not a normalisation choice. The doubled element $H=2S=\tilde\Xi$ is the form in which the frame root is written, and in the principal chains of $M_n$ it gives integer weights; it is the same triple and it names the same $j$.

## One Definition, Several Carriers

**The same definition is read on several carriers. The carriers differ; the number does not.**

| carrier | action $\rho$ | eigenvalues of $\rho(\tilde S_{\vec u})$ | spin $j$ | article |
|---|---|---|---|---|
| $S_+=\mathbb{B}\tilde\Pi_+$ | left multiplication $L$ | $+\tfrac12,-\tfrac12$ | $\tfrac12$ | *Spinors as Peirce Coordinates* |
| $S_-=\mathbb{B}\tilde\Pi_-$ | left multiplication $L$ | $+\tfrac12,-\tfrac12$ | $\tfrac12$ | *The Minimal Left Ideals* |
| $V=\mathbb{B}_{+-}\oplus\mathbb{C}\tilde\Xi\oplus\mathbb{B}_{-+}$ | commutator $\mathrm{ad}$ | $+1,0,-1$ | $1$ | *Integer-Spin Quantization* |
| $\mathbb{C} e_t$ | commutator $\mathrm{ad}$ | $0$ | $0$ | *The Scalar Field in the Centre* |
| $S_+^{\otimes n}$ | Lie triple on the tensor product | $\tfrac n2,\tfrac n2-1,\dots,-\tfrac n2$ | $\tfrac n2$ | *Higher Spin from Tensor Products* |

**The Lorentz layer has a second label.** A field in the representation $\tau^{l\bar l}$ restricts to the rotation subgroup as the string of spins $\lvert l-\bar l\rvert,\lvert l-\bar l\rvert+1,\dots,l+\bar l$. The number $j$ of this article is a highest weight, and on a single irreducible rotation carrier it is the top spin of such a string: $(\tfrac12,\tfrac12)$ contains a carrier of $j=1$, and the Rarita–Schwinger pair $\tau^{1,\frac12}\oplus\tau^{\frac12,1}$ contains a carrier of $j=\tfrac32$. The Bhabha–Gel'fand–Yaglom literature labels the whole representation by the other end, $s=\lvert l-\bar l\rvert$: $0$ for the vector and $\tfrac12$ for the Rarita–Schwinger pair. The two numbers agree on the defining module, where both are $\tfrac12$, and they differ as soon as the string has more than one term. This article writes the second as the **Bhabha spin**, or the **Lorentz difference**, never as $j$; which spin a Bhabha field propagates is fixed by its field equation and its subsidiary conditions, not by the label alone.

**The half-angle is a coordinate, not a second definition.** On $S_\pm$ the rotor $\exp(\tfrac{\theta}{2}\vec u)$ acts as $\exp(-i\theta L_{\tilde S_{\vec u}})$. The exponent $\theta/2$ is the exponential coordinate of the weight $\tfrac12$; it is not the weight and it is not $j$. On $V$ the same rotor produces the phase $\theta$, because the weight there is $1$. The half-angle is therefore a consequence of the weight, on the carrier where the weight is one half.

**The adjoint integer is the same definition.** On $V$ the spin element $\tilde S_{\vec u}$ has weights $+1,0,-1$, so $j=1$. Its highest eigenvalue is $j$, exactly as on $S_\pm$.

**The Peirce index is not a spin.** The right action of the root is $R_{\tilde\Xi}=+1$ on $S_+$ and $R_{\tilde\Xi}=-1$ on $S_-$, that is $R_{\tilde S_{\vec u}}=\pm\tfrac12$. That sign labels the two copies of one left module; it is neither a weight of $\tilde S_{\vec u}$ nor a chirality. The left weights of $\tilde S_{\vec u}$ are $+\tfrac12,-\tfrac12$ on both planes. The factor two is the identity $L_{\tilde\Xi}=\mathrm{ad}_{\tilde\Xi}+R_{\tilde\Xi}$ read on the two planes.

**The group fixes integrality, not the value.** The rotor group $\{\pm\exp(\tfrac{\theta}{2}\vec u)\}$ is the double cover of the rotation group. Its $2\pi$ element is $-e_t$ on the spinor and $+e_t$ on the vector; it separates half-integer from integer $j$. It does not supply $j$: the weight does.

**The Wigner label is the same number, read physically.** A particle of spin $s$ is described by a carrier of dimension $2s+1$ whose highest weight is $s$. The Standard Model assigns $s$ by hand. The algebra reproduces the set $\{0,\tfrac12,1\}$ and does not select which particle carries which value.

## What Is Not a Definition

- **Not the half-angle.** The half-angle $\theta/2$ is the exponential coordinate of the weight on a spin-$\tfrac12$ carrier. It is not $j$ and it is not a property of the rotor alone.
- **Not the doubled weight.** The frame root $\tilde\Xi=2\tilde S_{\vec u}$ has weights $+2,0,-2$ on $V$; the spin element $\tilde S_{\vec u}$ has weights $+1,0,-1$, and $j=1$ is the highest. Quoting the root weight $2$ as the spin forgets the factor two between the root and the spin element.
- **Not the Peirce index.** The right action of the root, $R_{\tilde\Xi}=\pm1$, equivalently $R_{\tilde S_{\vec u}}=\pm\tfrac12$, labels two isomorphic copies. It is not a weight of the spin element and it is not a chirality.
- **Not the spin vector.** The classical four-vector $S^\mu$, and the mean spin $\langle\vec S\rangle$ of a state, are intrinsic angular momenta. They are observables whose magnitude is fixed by $j$; the vector is not the number.
- **Not the $2+1$ statistics parameter.** The continuous $s$ of an anyon, defined by the rotation phase $\exp(2\pi i s)$, is a statistics parameter. It coincides with $j$ in $3+1$ dimensions and not in $2+1$.
- **Not the spin group.** The group $\mathrm{Spin}(3)$ fixes which $j$ are integral or half-integral under a full turn. It does not give the value of $j$.
- **Not the spinor, and not the element.** A spinor is a coordinate on a Peirce carrier. A biquaternion is an element. Neither has a spin; the carrier has one.

**Remark (spin is not a function of an element).** The phrase "the spin of $\tilde Q$" has no meaning. What has a spin is a carrier with an action; $\tilde Q$ acts on the carrier and its spectrum is read there. The phrase "the spin of a biquaternion" is shorthand for the carrier and its weight.

## What the Word Names

**The word appears in four grammatical roles. Only the second is the definition.**

- The **spin element** $\tilde S_{\vec u}=h/2$, an element of the algebra, Hermitian, half a root, and the antisymmetric part of the product of the two frame nilpotents. Its eigenvalues on a carrier define $j$.
- The **spin** $j$, the highest weight of $\tilde S_{\vec u}$ on a carrier. This is the definition.
- The **spinor**, a coordinate on a Peirce carrier, in the sense of *Spinors as Peirce Coordinates*. It is the carrier's coordinate, not the number.
- The **spin group** $\mathrm{Spin}(3)$, the double cover of the rotation group, a subgroup of the units of $\mathbb H$. It is the group that fixes integrality.

**Remark (the Peirce index is not a fifth role).** The right action of the root gives $R_{\tilde\Xi}=+1$ on $S_+$ and $-1$ on $S_-$. That sign is the **Peirce index**: the two planes are isomorphic, and the index distinguishes two copies of one module. It is not the spin weight, which is the left eigenvalue $+\tfrac12,-\tfrac12$ on both planes, and it is not a chirality. The chirality is the central sign $\chi=ij$, which grades $S$ against $S^{\mathrm{c}}$, as in *Chirality: The Conjugate Pair*.

## Summary

- The spin element along a real unit $\vec u$ is $\tilde S_{\vec u}=\tfrac12 i\vec u$; it is Hermitian, half the frame root $\tilde\Xi=i\vec u$, and the antisymmetric part of the product of the two frame nilpotents.
- The two normalised nilpotents form the spin pair; their antisymmetric part $\tilde S_{\vec u}=\tfrac12[\vec\Upsilon_-,\vec\Upsilon_+]$ is the spin element, and the triple $(\tilde S_{\vec u},\vec\Upsilon_-,\vec\Upsilon_+)$ satisfies $[\tilde S_{\vec u},\vec\Upsilon_-]=\vec\Upsilon_-$, $[\tilde S_{\vec u},\vec\Upsilon_+]=-\vec\Upsilon_+$ and $[\vec\Upsilon_-,\vec\Upsilon_+]=2\tilde S_{\vec u}$. The frame root is $\tilde\Xi=2\tilde S_{\vec u}$.
- The spin-$\tfrac12$ carrier is $S_+=\mathbb B\tilde\Pi_+$, on which $L_{\tilde S_{\vec u}}$ has weights $\pm\tfrac12$; the same holds for $S_-$, and the left regular module is $2\cdot\tfrac12$.
- The spin-$1$ carrier is the traceless part $V=\mathbb B_{+-}\oplus\mathbb C\tilde\Xi\oplus\mathbb B_{-+}$, on which $\mathrm{ad}_{\tilde S_{\vec u}}$ has weights $+1,0,-1$.
- The centre is the spin-$0$ carrier.
- The Casimir operator is $\sum_k\rho(\tilde S_k)^2$; it equals $\tfrac34$ on a spinor, $2$ on the vector and $0$ on the centre. The element $\sum_k\tilde S_k^2=\tfrac34 e_t$ is central and does not distinguish the carriers.
- The projectors of the spin are the idempotents $\tilde\Pi_\pm(\vec u)$ acting by left multiplication; no form is needed.
- The rotor $\exp(\tfrac{\theta}{2}\vec u)$ acts as $\exp(-i\theta L_{\tilde S_{\vec u}})$ on the spinor and as $\mathrm{Ad}_{\tilde u(\theta)}=\exp(-i\theta\,\mathrm{ad}_{\tilde S_{\vec u}})$ on the vector; the exponent is the weight, and the half-angle is a consequence.
- On $\mathbb B$ alone the elementary spins are exactly $0,\tfrac12,1$: the elementary carriers are the isomorphism classes of nonzero irreducible invariant subspaces under left multiplication or the commutator; the associative ones give only $\tfrac12$, and the adjoint ones give $0$ and $1$. There is no fourth elementary value.
- The three values are the spins of all observed elementary particles: $0$ for the Higgs, $\tfrac12$ for the quarks and leptons, $1$ for the photon, $W^{\pm}$, $Z$ and gluons. The match is structural and not predictive.
- Higher spins are not forbidden; they require a tensor product, and they are $\tfrac32,2,\dots$.
- Spin is a property of a carrier, not of an element; the right root eigenvalue is the Peirce index, not a chirality, and it is independent of the spin weight.
- The determinant of $L_{\tilde Q}$ on a spinor plane is the norm $N(\tilde Q)$: the rank is $2$ on the $N$-regular set and $1$ on the nonzero null cone, while the weights of the spin element stay $\pm\tfrac12$ and the spin stays $\tfrac12$. Half the rank is the quantity that is $1$ and $\tfrac12$; it counts components, not spin. Spin $0$ is the centre, not the zero element.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde S_{\vec u}=\tfrac12 i\vec u$ | the spin element along the real unit $\vec u$ |
| $\tilde\Xi=i\vec u=2\tilde S_{\vec u}$ | the frame root of the direction |
| $\tilde\Pi_\pm(\vec u)=\tfrac12(e_t\pm\tilde\Xi)$ | the idempotents of the direction |
| $\tilde S_{\vec u}$, $\vec\Upsilon_-$, $\vec\Upsilon_+$ | the spin triple of the frame |
| $S_\pm=\mathbb B\tilde\Pi_\pm$ | the spin-$\tfrac12$ carriers |
| $V=\mathbb B_{+-}\oplus\mathbb C\tilde\Xi\oplus\mathbb B_{-+}$ | the spin-$1$ carrier, the traceless part |
| $W_j$ | the spin-$j$ carrier in a tensor product |
| $j$ | the spin quantum number, the highest weight of the spin element $\tilde S_{\vec u}$ |
| $H=2\tilde S_{\vec u}$ | the doubled Cartan, equal to the frame root $\tilde\Xi$ |
| elementary carrier | a nonzero irreducible invariant subspace of $\mathbb B$ under $L$ or $\mathrm{ad}$; the spaces are $\mathbb C e_t$, $S_\pm$, $V$ |
| $\sum_k\rho(\tilde S_k)^2$ | the Casimir operator on the carrier |
| $N(\tilde Q)=Q_t^{2}+B^{2}$ | the norm, the determinant of $L_{\tilde Q}$ on $S_\pm$ |
| $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the discriminant of the spectrum |

## Further Reading

- [The Weight of a Frame Root and the Spin Quantum Number](the-weight-of-a-frame-root-and-the-spin-quantum-number.html), for the general definition of carrier, weight and spin.
- [Spin and the Three Elementary Carriers](../articles_physics/spin-and-the-three-elementary-carriers.html), for the same three carriers read physically, with the observed particle content.
- [Higher Spin from Tensor Products](../articles_physics/higher-spin-from-tensor-products-why-the-biquaternion-algebra-admits-only-spin-0-and-one-half.html), for the spins beyond the elementary list.
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the frame, the corners and the weight table.
- [Spinors as Peirce Coordinates in the Biquaternion Algebra](spinors-as-peirce-coordinates-in-the-biquaternion-algebra.html), for the two Peirce planes and their adapted bases.
- [The Minimal Left Ideals](the-minimal-left-ideals.html), for the irreducibility of the two planes.
- [The Category of Modules](the-category-of-modules.html), for the associative modules over $\mathbb B$.
- [The One-Sided Operator Exponential of a N-Regular, Spectrally Regular Biquaternion](the-one-sided-operator-exponential-of-a-n-regular-spectrally-regular-biquaternion.html), for the half-angle theorem.
- [Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form](../articles_physics/integer-spin-quantization-and-the-adjoint-action-on-the-material-sector-in-biquaternionic-form.html), for the integer-spin reading of the adjoint action.
- [Operators of the Polar Word: The Common Framework](operators-of-the-polar-word-the-common-framework.html), for the three operators and the polar word.
- [The Two-Sided Operator of a N-Degenerate, Spectrally Regular Biquaternion](the-two-sided-operator-of-a-n-degenerate-spectrally-regular-biquaternion.html), for the rank one of the sandwich on the null cone.
- [The N-Regular, Spectrally Regular Sector](the-n-regular-spectrally-regular-sector.html), for the four sectors and the two conditions.
- [$M_2(\mathbb{C})$ Representation : Spin, Qubits and the Bloch Vector](m2c-representation-spin-qubits-and-the-bloch-vector.html), for the Hermitian form and the expectation values.
- [Peirce Carriers and Inner Conjugation](peirce-carriers-and-inner-conjugation.html), for the spinor adjoint.
