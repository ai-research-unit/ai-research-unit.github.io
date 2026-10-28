# __The Spin of a Biquaternion__

## Introduction

A biquaternion has no spin. A **carrier** of the algebra has one: the spin is half the highest weight of the frame root on that carrier, and the carrier decides whether that half is an integer or a half-integer. The general definition of carrier, weight and spin is *The Weight of a Frame Root and the Spin Quantum Number*; this article computes them for $\mathbb{B}$ and identifies the carriers on which they occur.

The computation has one striking output. The spin-$\tfrac12$ structure of the biquaternion is its Peirce frame: the half-root $\tfrac12\tilde\Xi=\tfrac12(\tilde\Pi_+-\tilde\Pi_-)$ and the two nilpotents $\vec\Upsilon_x,\vec\Upsilon_y$ form an $\mathfrak{sl}_2$ triple, and the two Peirce planes are its two-dimensional modules for the left action. No extra structure is needed, and no form is used.

The article is organized as follows. §*The Spin Operator* defines the Hermitian element $\tilde S_{\vec u}$ and its commutator algebra. §*The Spin Triple of the Frame* proves the $\mathfrak{sl}_2$ relations from the Peirce table. §*The Three Elementary Carriers* computes the spin on the spinor, the vector and the centre. §*The Casimir* separates the central element from the Casimir operator. §*The Spin Projectors* and §*The Rotor and the Half-Angle* read the measurement and the rotation. §*Tensor Products and the Roster* gives the spins of the tensor powers. §*The Approaches in the Corpus* compares the six ways in which the corpus states the same root, and §*What the Word Spin Names* separates the four uses of the word.

Throughout $\hbar=1$; the element is $\hbar\tilde S_{\vec u}$, and the operator on a carrier is the action of that element, left multiplication on a spinor or the commutator on the vector. The article uses the product, the Peirce frame and the left and adjoint actions. It uses no form, no norm and no Hilbert structure; the expectation values belong to *$M_2(\mathbb{C})$ Representation : Spin, Qubits and the Bloch Vector*.

## The Spin Operator

**For a real unit vector $\vec u$, the spin operator is the Hermitian element $\tilde S_{\vec u}=\tfrac12 i\vec u$; it is half the frame root of the pair $\tilde\Pi_\pm(\vec u)$.**

**Definition.** Let $\vec u=u_x\vec e_x+u_y\vec e_y+u_z\vec e_z$ with real coefficients and $\vec u^2=-e_t$, that is $u_x^2+u_y^2+u_z^2=1$. The **spin operator along $\vec u$** is

$$
\tilde S_{\vec u}=\frac{i}{2}\vec u=\frac{1}{2}\bigl(iu_x\vec e_x+iu_y\vec e_y+iu_z\vec e_z\bigr).
$$

The three coordinate operators are $\tilde S_k=\tfrac{i}{2}\vec e_k$. The factor $\tfrac12$ is the half of the frame root $\tilde\Xi$ defined next, and the factor $i$ turns the anti-Hermitian unit $\vec e_k$ into a Hermitian element, $\tilde S_{\vec u}^{*}=\tilde S_{\vec u}$.

**The frame root.** The element $\tilde\Xi=2\tilde S_{\vec u}=i\vec u$ is a root of $+1$, since $\tilde\Xi^2=i^2\vec u^2=(-1)(-1)=e_t$. Its idempotents are

$$
\tilde\Pi_+(\vec u)=\frac{e_t+\tilde\Xi}{2}=\frac{e_t+i\vec u}{2},\qquad
\tilde\Pi_-(\vec u)=\frac{e_t-\tilde\Xi}{2}=\frac{e_t-i\vec u}{2},
$$

and the spin operator is their half-difference,

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

**The half-root and the two nilpotents of the frame form an $\mathfrak{sl}_2$ triple, and the relations are the Peirce table.**

**Definition.** Let $\tilde\Pi_\pm$ be a complete pair, $\tilde\Xi=\tilde\Pi_+-\tilde\Pi_-$, and let $\vec\Upsilon_-\in\mathbb B_{+-}$ and $\vec\Upsilon_+\in\mathbb B_{-+}$ be the normalised nilpotents, $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$ and $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$. The **spin triple of the frame** is

$$
\Bigl(\tfrac12\tilde\Xi,\ \vec\Upsilon_-,\ \vec\Upsilon_+\Bigr).
$$

For the standard frame, $\tfrac12\tilde\Xi=\tfrac{i}{2}\vec e_z=\tilde S_z$, and the nilpotents are $\vec\Upsilon_x$ and $\vec\Upsilon_y$.

**Theorem.** The triple satisfies

$$
[\tfrac12\tilde\Xi,\vec\Upsilon_-]=\vec\Upsilon_-,\qquad [\tfrac12\tilde\Xi,\vec\Upsilon_+]=-\vec\Upsilon_+,\qquad [\vec\Upsilon_-,\vec\Upsilon_+]=\tilde\Xi .
$$

*Proof.* The corner signs give $\tilde\Xi\vec\Upsilon_-=\vec\Upsilon_-$ and $\vec\Upsilon_-\tilde\Xi=-\vec\Upsilon_-$, so $[\tilde\Xi,\vec\Upsilon_-]=2\vec\Upsilon_-$ and $[\tfrac12\tilde\Xi,\vec\Upsilon_-]=\vec\Upsilon_-$. The second relation is the same computation on $\mathbb B_{-+}$, $[\tilde\Xi,\vec\Upsilon_+]=-2\vec\Upsilon_+$. The third is the normalised Peirce product, $[\vec\Upsilon_-,\vec\Upsilon_+]=\vec\Upsilon_-\vec\Upsilon_+-\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_+-\tilde\Pi_-=\tilde\Xi$.

**Remark (normalisation).** The triple is not unique. The reciprocal rescaling $\vec\Upsilon_-\mapsto\mu\vec\Upsilon_-$, $\vec\Upsilon_+\mapsto\mu^{-1}\vec\Upsilon_+$ preserves the two products and hence the three relations. What is canonical is $\tilde\Xi$ and the unordered pair of nilpotent lines.

**The ladder on the spinor.** On $S_+=\mathbb B\tilde\Pi_+$, with the couple $(\tilde\Pi_+,\vec\Upsilon_+)$ as basis, the left multiplications are

$$
L_{\tilde\Xi/2}=\begin{pmatrix}\tfrac12&0\\0&-\tfrac12\end{pmatrix},\qquad
L_{\vec\Upsilon_-}=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
L_{\vec\Upsilon_+}=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
$$

The operator $L_{\vec\Upsilon_-}$ raises the nilpotent to the idempotent and $L_{\vec\Upsilon_+}$ lowers the idempotent to the nilpotent. The same two matrices act on $S_-=\mathbb B\tilde\Pi_-$ in the couple $(\vec\Upsilon_-,\tilde\Pi_-)$, with the two basis vectors exchanged in their roles.

**Remark (the triple is the frame).** This is the precise sense in which spin is native to the biquaternion: the two nilpotents that give the Peirce coordinates are the ladder operators, and the root that labels the pair is the Cartan generator. The spin-$\tfrac12$ of the algebra is not an add-on; it is the frame read as a Lie triple.

## The Three Elementary Carriers

**The algebra has two natural actions and four elementary carriers: two spinor planes with weights $\pm\tfrac12$, the traceless part with weights $+1,0,-1$, and the centre with weight $0$.**

The two actions are not interchangeable. Left multiplication is associative and carries each spinor plane into itself; the commutator is a Lie action and carries the traceless part and the centre into themselves. The two readings of the same eight real dimensions are collected in the table of §*The Table*.

### The Spinor

**The plane $S_+=\mathbb B\tilde\Pi_+$ is a spin-$\tfrac12$ carrier, and so is $S_-$.**

On $S_+$ the operator $L_{\tilde\Xi/2}$ has the two weights $+\tfrac12$ on $\tilde\Pi_+$ and $-\tfrac12$ on $\vec\Upsilon_+$. The highest weight is $\tfrac12$, so $j=\tfrac12$, and the dimension is $2j+1=2$. The two weight lines are one-dimensional, and the ladder of §*The Spin Triple of the Frame* joins them, so the carrier is irreducible. The same computation on $S_-$ gives the weights $+\tfrac12$ on $\vec\Upsilon_-$ and $-\tfrac12$ on $\tilde\Pi_-$.

**Remark (the two planes are isomorphic).** The two planes are distinct subspaces, but they are isomorphic as left modules: the exchange of §*Right Multiplication* of *Spinors as Peirce Coordinates in the Biquaternion Algebra* is a bijection and commutes with the left action. The left regular module therefore decomposes as

$$
\mathbb B=S_+\oplus S_-=2\cdot\tfrac12 .
$$

### The Vector

**The traceless part $V=\mathbb B_{+-}\oplus\mathbb C\tilde\Xi\oplus\mathbb B_{-+}$ is a spin-$1$ carrier for the commutator.**

The space $V$ is the pure part, the kernel of the trace, of complex dimension three. On the basis $(\vec\Upsilon_-,\tilde\Xi,\vec\Upsilon_+)$ the commutator $\mathrm{ad}_{\tilde\Xi/2}$ is diagonal with weights $+1,0,-1$: the root acts on the two nilpotents by $\pm1$ and on itself by $0$. The highest weight is $1$, so $j=1$, and the dimension is $3$. The ladder is $\mathrm{ad}_E$ raising and $\mathrm{ad}_F$ lowering.

The space $V$ is not a Peirce corner and not an associative module: left multiplication by $\tilde\Pi_+$ sends $\tilde\Xi$ to $\tilde\Pi_+$, which has trace one. It is a module for the Lie triple only, and that is the carrier on which the integer spin lives.

### The Centre

**The centre $\mathbb C_{\mathbb B}=\mathbb C e_t$, the real span of $e_t$ and $ie_t$, is the spin-$0$ carrier.**

Every inner derivation annihilates the centre, so $\mathrm{ad}_{\tilde\Xi/2}=0$ there and the only weight is $0$. The highest weight is $0$, so $j=0$, and the dimension is one. The scalar field of the physics is this carrier.

### The Table

| carrier | action | complex dimension | weights of $\frac12\tilde\Xi$ | $j$ | Casimir |
|---|---|---|---|---|---|
| $S_+$ | $L_{\tilde\Xi/2}$ | $2$ | $+\tfrac12,-\tfrac12$ | $\tfrac12$ | $\tfrac34$ |
| $S_-$ | $L_{\tilde\Xi/2}$ | $2$ | $+\tfrac12,-\tfrac12$ | $\tfrac12$ | $\tfrac34$ |
| $V$ | $\mathrm{ad}_{\tilde\Xi/2}$ | $3$ | $+1,0,-1$ | $1$ | $2$ |
| $\mathbb C_{\mathbb B}$ | $\mathrm{ad}_{\tilde\Xi/2}$ | $1$ | $0$ | $0$ | $0$ |

**Remark (the factor two between the two readings).** On the spinor the root $\tilde\Xi$ has weights $\pm1$ and the operator $\tfrac12\tilde\Xi$ has weights $\pm\tfrac12$; on the traceless part $\mathrm{ad}_{\tilde\Xi}$ has weights $\pm2$ and $\mathrm{ad}_{\tilde\Xi/2}$ has weights $\pm1$. The half-integer spin is the left module, the integer spin the adjoint module, and the factor two is the shift $L_{\tilde\Xi}=\mathrm{ad}_{\tilde\Xi}+R_{\tilde\Xi}$ of *The Weight of a Frame Root and the Spin Quantum Number*: on the mixed corners the right weight is the negative of the left weight, so the commutator weight is twice the left weight; on the diagonal corners both vanish.

**Remark (the two readings are not two decompositions of one module).** The left regular module is $S_+\oplus S_-$, of complex dimension four; the adjoint module is $V\oplus\mathbb C_{\mathbb B}$, also of complex dimension four. They are different actions on the same eight real dimensions. Only the first is an associative module; only the second contains the vector carrier.

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

**Tensor products of the elementary carriers give the higher spins; the algebra itself carries only $0,\tfrac12,1$.**

The tensor products are taken for the Lie triple, with $X\cdot(\xi\otimes\eta)=X\xi\otimes\eta+\xi\otimes X\eta$; they are not modules over the associative algebra, which has no coproduct. The weights of $\frac12\tilde\Xi$ add, and the weight string of the product is the sum of the strings of the factors.

| product | complex dimension | decomposition | spins |
|---|---|---|---|
| $S_+\otimes S_+$ | $4$ | $V\oplus\mathbb C_{\mathbb B}$ | $1,0$ |
| $S_+\otimes V$ | $6$ | $S_{3/2}\oplus S_{1/2}$ | $\tfrac32,\tfrac12$ |
| $V\otimes V$ | $9$ | $S_2\oplus V\oplus\mathbb C_{\mathbb B}$ | $2,1,0$ |

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

## The Approaches in the Corpus

**The corpus states spin in six ways, and they are six readings of one frame root: the half-angle, the adjoint integer, the Peirce carrier, the highest weight, the Hermitian operator and the group element.**

| approach | what it calls spin | the frame reading |
|---|---|---|
| half-angle of the rotor | the exponent $\theta/2$ of $\exp(\tfrac{\theta}{2}\vec u)$ | the weight $\pm\tfrac12$ of $L_{\tilde S_{\vec u}}$ on the spinor |
| adjoint on the material sector | the integer weights $+1,0,-1$ of the vector part and the $0$ of the centre | $\mathrm{ad}_{\tilde\Xi}$ on $V$ ($+2,0,-2$) and on $\mathbb C_{\mathbb B}$ ($0$), halved to $+1,0,-1$ and $0$ |
| Peirce carrier / minimal left ideal | the weight $\pm\tfrac12$ on the plane, the spinor being the coordinate | the left module $S_\pm$ |
| highest weight | $j=\lambda_{\max}/2$ | the general definition of *The Weight of a Frame Root and the Spin Quantum Number* |
| Hermitian operator | the element $\tilde S_{\vec u}=\tfrac12 i\vec u$ | the element whose left and adjoint actions give the weights |
| spin group | the double cover $\mathrm{Spin}(3)$ | the rotor group $\{\pm\exp(\tfrac{\theta}{2}\vec u)\}$; its $2\pi$ element is $-e_t$ on the spinor and $+e_t$ on the vector |

**The half-angle and the integer are the same root on two carriers.** The polar-word articles read the exponent $\theta/2$ of the one-sided operator; *Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form* reads the adjoint action on the material sector. The first is the weight of $L_{\tilde S}$ on $S_\pm$, the second the weight of $\mathrm{ad}_{\tilde S}$ on $V\oplus\mathbb C_{\mathbb B}$; the two differ by the chirality, $L_{\tilde\Xi}=\mathrm{ad}_{\tilde\Xi}+R_{\tilde\Xi}$, and the factor two is the difference of the two corner signs. Neither reading is more fundamental: the same element has both, and the carrier selects.

**The carrier is prior to the word.** The minimal-left-ideal article and the Peirce-carrier article describe the same two planes; the spinor is the coordinate on a plane, the operator is the element whose action gives the weight, and the group is the exponentiated rotor. The six readings agree because each lands on the same number, the highest weight of $\frac12\tilde\Xi$ on a carrier. That number is the definition.

## What the Word Spin Names

**The word names four different objects, and the article uses the first three.**

- The **spin operator** $\tilde S_{\vec u}$, an element of the algebra, Hermitian and half a root.
- The **spin quantum number** $j$, the highest weight of $\tilde S_{\vec u}$ on a carrier; it is a label of the carrier, not of an element.
- The **spinor**, a coordinate on a Peirce carrier, in the sense of *Spinors as Peirce Coordinates*.
- The **spin group** $\mathrm{Spin}(3)$, the double cover of the rotation group, a subgroup of the units of $\mathbb H$; it is the subject of *The Two-Sided Operators and the Spin Group* and is not an element of the algebra in the sense of the first three.

**Remark (chirality is a fifth word).** The chirality of a spinor plane is the eigenvalue of the right action of the root: $R_{\tilde\Xi}=+1$ on $S_+$ and $R_{\tilde\Xi}=-1$ on $S_-$. It is not the spin weight, which is the eigenvalue of the left action and is $+\tfrac12,-\tfrac12$ on both planes. The two planes have the same spin and opposite chirality; the two words are independent, and the factor two of §*The Table* is the identity $L_{\tilde\Xi}=\mathrm{ad}_{\tilde\Xi}+R_{\tilde\Xi}$ read on the two planes.

**Remark (spin is not a function of an element).** The phrase "the spin of $\tilde Q$" has no meaning. What has a spin is a carrier with an action; $\tilde Q$ acts on the carrier and its spectrum is read there. The phrase "the spin of a particle" is the physics name for the label of the carrier that describes it; the phrase "the spin of a biquaternion" is shorthand for the triple of its frame.

## Summary

- The spin operator along a real unit $\vec u$ is $\tilde S_{\vec u}=\tfrac12 i\vec u$; it is Hermitian and half the frame root $\tilde\Xi=i\vec u$.
- The root and the two normalised nilpotents form the $\mathfrak{sl}_2$ triple $\tfrac12\tilde\Xi$, $\vec\Upsilon_-$, $\vec\Upsilon_+$, with $[\tfrac12\tilde\Xi,\vec\Upsilon_-]=\vec\Upsilon_-$, $[\tfrac12\tilde\Xi,\vec\Upsilon_+]=-\vec\Upsilon_+$ and $[\vec\Upsilon_-,\vec\Upsilon_+]=\tilde\Xi$.
- The spin-$\tfrac12$ carrier is $S_+=\mathbb B\tilde\Pi_+$, on which $L_{\tilde\Xi/2}$ has weights $\pm\tfrac12$; the same holds for $S_-$, and the left regular module is $2\cdot\tfrac12$.
- The spin-$1$ carrier is the traceless part $V=\mathbb B_{+-}\oplus\mathbb C\tilde\Xi\oplus\mathbb B_{-+}$, on which $\mathrm{ad}_{\tilde\Xi/2}$ has weights $+1,0,-1$.
- The centre is the spin-$0$ carrier.
- The Casimir operator is $\sum_k\rho(\tilde S_k)^2$; it equals $\tfrac34$ on a spinor, $2$ on the vector and $0$ on the centre. The element $\sum_k\tilde S_k^2=\tfrac34 e_t$ is central and does not distinguish the carriers.
- The projectors of the spin are the idempotents $\tilde\Pi_\pm(\vec u)$ acting by left multiplication; no form is needed.
- The rotor $\exp(\tfrac{\theta}{2}\vec u)$ acts as $\exp(-i\theta L_{\tilde S_{\vec u}})$ on the spinor and as $\mathrm{Ad}_{\tilde u(\theta)}=\exp(-i\theta\,\mathrm{ad}_{\tilde S_{\vec u}})$ on the vector; the exponent is the weight, and the half-angle is a consequence.
- The algebra carries the spins $0,\tfrac12,1$; tensor products give $\tfrac32,2,\dots$.
- Spin is a property of a carrier, not of an element; chirality is the right root eigenvalue and is independent of the spin weight.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde S_{\vec u}=\tfrac12 i\vec u$ | the spin operator along the real unit $\vec u$ |
| $\tilde\Xi=i\vec u=2\tilde S_{\vec u}$ | the frame root of the direction |
| $\tilde\Pi_\pm(\vec u)=\tfrac12(e_t\pm\tilde\Xi)$ | the idempotents of the direction |
| $\tfrac12\tilde\Xi$, $\vec\Upsilon_-$, $\vec\Upsilon_+$ | the $\mathfrak{sl}_2$ triple of the frame |
| $S_\pm=\mathbb B\tilde\Pi_\pm$ | the spin-$\tfrac12$ carriers |
| $V=\mathbb B_{+-}\oplus\mathbb C\tilde\Xi\oplus\mathbb B_{-+}$ | the spin-$1$ carrier, the traceless part |
| $S_j$ | the spin-$j$ carrier in a tensor product |
| $j$ | the spin quantum number, the highest weight of $\tfrac12\tilde\Xi$ |
| $\sum_k\rho(\tilde S_k)^2$ | the Casimir operator on the carrier |

## Further Reading

- [The Weight of a Frame Root and the Spin Quantum Number](the-weight-of-a-frame-root-and-the-spin-quantum-number.html), for the general definition of carrier, weight and spin.
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-in-the-biquaternion-algebra.html), for the frame, the corners and the weight table.
- [Spinors as Peirce Coordinates in the Biquaternion Algebra](spinors-as-peirce-coordinates-in-the-biquaternion-algebra.html), for the two spin-$\tfrac12$ planes and their weight bases.
- [The Minimal Left Ideals](the-minimal-left-ideals.html), for the irreducibility of the two planes.
- [The Category of Modules](modules-over-the-biquaternion-algebra.html), for the associative modules over $\mathbb B$.
- [The One-Sided Operator Exponential of a N-Regular, Spectrally Regular Biquaternion](the-one-sided-operator-exponential-of-a-n-regular-spectrally-regular-biquaternion.html), for the half-angle theorem.
- [Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form](../articles_physics/integer-spin-quantization-and-the-adjoint-action-on-the-material-sector-in-biquaternionic-form.html), for the integer-spin reading of the adjoint action.
- [Operators of the Polar Word: The Common Framework](operators-of-the-polar-word-the-common-framework.html), for the three operators and the polar word.
- [$M_2(\mathbb{C})$ Representation : Spin, Qubits and the Bloch Vector](m2c-representation-spin-qubits-and-the-bloch-vector.html), for the Hermitian form and the expectation values.
- [Peirce Carriers and Inner Conjugation](peirce-carriers-and-inner-conjugation.html), for the spinor adjoint.
