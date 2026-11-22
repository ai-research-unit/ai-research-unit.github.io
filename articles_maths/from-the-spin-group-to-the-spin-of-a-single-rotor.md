# __From the Spin Group to the Spin of a Single Rotor__

## Introduction

The spin group is the group of unit quaternions, that is the sphere $S^3$. This article follows one thread from that group to the number $\tfrac12$, and then from $\tfrac12$ to the pair $0$ and $1$: why an element of the group must act by a two-sided product, how the three real $4\times4$ generators of left multiplication carry that action, and how the quadratic Casimir of those three generators returns spin $\tfrac12$. It then takes the square of that carrier, and the square splits as $0\oplus1$ and nothing else. That is the Clebsch–Gordan series $\tfrac12\otimes\tfrac12=0\oplus1$ of a square of the half-integer slot, stated at the level of the algebra in *The Clebsch–Gordan Decomposition of the Biquaternion Algebra*.

**The thread in one paragraph.** To act on an algebra while preserving its multiplication, an element must act on both sides. One-sided multiplication is not an algebra map. The two-sided product is therefore forced, and it is the only inner-type action available. The spin group is the compact group of elements whose two-sided product is conjugation by the inverse with no scalar in front. Left multiplication by such an element is a real $4\times4$ orthogonal matrix, the three generators are real antisymmetric matrices, and the sum of their squares is a multiple of the identity. That multiple is $-\tfrac34$, and the Hermitian normalization is $+\tfrac34$. The number $\tfrac34$ is $s(s+1)$ at $s=\tfrac12$. Read with the series, the two results are one statement: $\tfrac12$ is the label of the slot, and $\tfrac12\otimes\tfrac12=0\oplus1$ is the square of that slot, so the Casimir identifies the factor and the split of the square gives the two integer labels.

**What the article does not claim.** Three sentences are excluded by construction, and each is repaired in *Corrections*. The spin group is $S^3=\mathrm{Spin}(3)$; it is isomorphic to $SU(2)$, and $SU(2)$ is the image of one of its displays. The spin group is not any matrix group; it is $S^3$, and a matrix group is an image of it. The three $L$-generators do not give all spins; they give one spin, on one carrier. That one spin is the label of the slot that the series squares, and the labels $0$ and $1$ are labels of summands of the square, not labels of a one-sided carrier.

**Roadmap.** The forcing of the two-sided form comes first, with the four conjugations of the biquaternion algebra and the two two-sided operators that matter. Then the spin group, its identification with the spin group, and its double cover. Then the $L$-generators, the Casimir, and the extraction of $\tfrac12$. Then two rotors, the split into $0\oplus1$, and the reason the split is forced. Then what the generators do not give, the corrections, and the numerical check.

## Why the Two-Sided Action Is Necessary

**The question.** Let $A$ be an associative algebra with a unit over a field, and let $R\in A$ be invertible. The element $R$ is to act on $A$ by a map that preserves the multiplication, that is by an algebra automorphism of the form built from $R$ alone. Which forms are available?

**Proposition (one-sided multiplication is not multiplicative).** Let $\Lambda(X)=RX$. Then $\Lambda$ is multiplicative, $\Lambda(XY)=\Lambda(X)\Lambda(Y)$ for all $X,Y$, if and only if $R$ is the unit.

*Proof.* Suppose $RXY=RXRY$ for all $X,Y$. Take $Y=e$. Then $RX=RXR$ for all $X$, so $XR=X$ for all $X$ after multiplying on the left by $R^{-1}$. Taking $X=e$ gives $R=e$. Conversely $R=e$ gives the identity map. ∎

**Corollary.** No one-sided multiplication by an invertible element acts on the algebra by an automorphism, apart from the identity. The failure is not a matter of normalization: the product $R(XY)$ has one factor $R$, and the product $(RX)(RY)$ has two, and the count cannot be repaired.

**Proposition (the two-sided product is multiplicative).** Let $\Theta(X)=RXR^{-1}$. Then

$$
\Theta(X)\Theta(Y)=RXR^{-1}\,RYR^{-1}=RXYR^{-1}=\Theta(XY),
$$

so $\Theta$ is an algebra automorphism for every invertible $R$. The map $R\mapsto\Theta$ is a homomorphism whose kernel is the centre.

*Proof.* The displayed computation is the whole proof of multiplicativity. The map is a homomorphism because $\Theta_R\Theta_S=\Theta_{RS}$, and its kernel is the set of $R$ with $RXR^{-1}=X$ for all $X$, that is the centre. ∎

**The conclusion.** A two-sided product is forced by the multiplication and nothing else is available. This is a theorem about associative algebras, not a convention of this corpus, and it is the reason every inner action in what follows is written with two factors.

### The Four Conjugations and the Two Operators

**The marks.** The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes\mathbb{H}$ carries an identity, a quaternion conjugation $\natural$ that negates the vector coefficients, a complex conjugation of the coefficients, and their composite, the Hermitian adjoint $*=\bar{\cdot}\circ\natural$. On a real quaternion the last two agree with the first, and all three are the quaternion conjugation.

**Two two-sided operators.** Two of these marks produce a two-sided operator that is used in the corpus, and they are not the same operator:

$$
\Theta_{\natural}(\tilde Q):\ \tilde X\mapsto\tilde Q\tilde X\tilde Q^{\natural},
\qquad
\Theta_{*}(\tilde Q):\ \tilde X\mapsto\tilde Q\tilde X\tilde Q^{*}.
$$

**Proposition (the $\natural$-operator is the inverse-conjugation up to the norm).** For invertible $\tilde Q$,

$$
\tilde Q\tilde X\tilde Q^{\natural}=\langle\tilde Q\rangle_{\natural}\ \tilde Q\tilde X\tilde Q^{-1},
$$

where $\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2$ is the value of the quaternion norm on $\tilde Q$.

*Proof.* $\tilde Q\tilde Q^{\natural}=\langle\tilde Q\rangle_{\natural}e_t$, so $\tilde Q^{\natural}=\langle\tilde Q\rangle_{\natural}\tilde Q^{-1}$, and the scalar comes out on the right. ∎

**Corollary (where the $\natural$-operator is an automorphism).** $\Theta_{\natural}(\tilde Q)$ is an algebra automorphism exactly when $\langle\tilde Q\rangle_{\natural}=1$, and then it is conjugation by the inverse. Off that surface it is a scaled automorphism, the scale being the norm.

**Corollary (where the $*$-operator is an automorphism).** $\Theta_{*}(\tilde Q)$ is conjugation by the inverse exactly when $\tilde Q^{*}=\tilde Q^{-1}$, and it is an automorphism exactly then. Independently of that, it always preserves the Hermitian adjoint,

$$
\Theta_{*}(\tilde X^{*})=\tilde Q\tilde X^{*}\tilde Q^{*}=\bigl(\tilde Q\tilde X\tilde Q^{*}\bigr)^{*}=\Theta_{*}(\tilde X)^{*} .
$$

**The two structures.** The two operators preserve two different things, and neither preserves both in general. $\Theta_{\natural}$ preserves the product on the norm-one surface. $\Theta_{*}$ preserves the involution $*$ always. A reader who wants an automorphism uses the first; a reader who wants Hermitian elements carried to Hermitian elements uses the second.

**The rotor sector.** Let $\tilde u$ be a real unit quaternion. Then $\tilde u^{*}=\tilde u^{\natural}=\tilde u^{-1}$, since $\natural$ is the quaternion conjugation of a real element and the complex conjugation does nothing. On the rotor sphere the two operators coincide, and each of them is conjugation by the inverse. This is the sense in which a rotor acts on the algebra by an inner automorphism: no scale, no choice between the two forms, and the product preserved.

**The boost sector, and a correction.** The brief that commissioned this article says that a boost satisfies $\tilde U_{\mathrm b}^{\natural}\ne\tilde U_{\mathrm b}^{-1}$ while $\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b}$. The second half is right: a boost $\tilde U_{\mathrm b}=\cosh\tfrac\phi2\,e_t+i\sinh\tfrac\phi2\,\vec n$ with real unit $\vec n$ is Hermitian. The first half is wrong. Its $\natural$-conjugate is $\cosh\tfrac\phi2\,e_t-i\sinh\tfrac\phi2\,\vec n$, and the product of the two is $\cosh^2-\sinh^2=1$, because $(i\vec n)^2=+e_t$. So $\tilde U_{\mathrm b}^{\natural}=\tilde U_{\mathrm b}^{-1}$ as well. Both sectors sit on the norm-one surface of the $\natural$-form, and $\natural$ is the inverse on both.

**What actually separates the sectors.** The separation is not "$\natural$ versus inverse". It is which of the two operators is the one that does the job. On a boost the $\natural$-operator is conjugation by the inverse and is an automorphism; the $*$-operator is not, since $\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b}\ne\tilde U_{\mathrm b}^{-1}$, and it does something else: it carries the Hermitian part of the algebra to itself. On a general element of the Lorentz group, which is neither real nor Hermitian, the two operators differ from each other, and both differ from the identity. The $\natural$-operator is still the inverse-conjugation, because the whole group sits on the norm-one surface; the $*$-operator is not.

**The statement the article keeps.** The two-sided form is compulsory for any inner-type action. It is conjugation by the inverse exactly on the norm-one surface of the mark used, which for the rotor sphere holds for both marks at once. The spin group is the compact group of elements for which the two-sided action is an automorphism with no scalar, and part of the reason the number $\tfrac12$ appears is that this group is a sphere and not a linear space.

## The Spin Group

**Definition (spin group).** The **spin group** is

$$
\mathrm{Spin}(3):=\{\tilde q\in\mathbb{H}:\langle\tilde q\rangle_{\natural}=1\}=\{\tilde q\in\mathbb{H}:\lvert\tilde q\rvert=1\}=S^3,
$$

the unit quaternions under quaternion multiplication. Its real dimension is three. The corpus also writes it $Sp(1)$ and calls its elements versors.

**The group and its displays.** $\mathrm{Spin}(3)$ is the sphere. It is not a set of matrices. A **matrix display** is a homomorphism from it into $GL(V)$, for a real or complex space $V$. The $2\times2$ complex display has image $SU(2)$, and the $4\times4$ real left-regular display has image a three-dimensional subgroup of $SO(4)$. Both are images; neither is the group.

**The spin group.** In the Clifford algebra $\mathrm{Cl}(V)$ of a real space with a positive definite form, the **spin group** is

$$
Spin(n):=\{v_1v_2\cdots v_{2k}\in\mathrm{Cl}(V):\ v_i\in\mathbb{R}^n,\ \lVert v_i\rVert=1,\ k\ge0\},
$$

the group of products of an even number of unit vectors. The name **rotor** is the geometric-algebra name for an element of this group. For $n=3$ the two descriptions coincide: $\mathrm{Cl}(\mathbb{R}^3)$ has the even part isomorphic to $\mathbb{H}$, the unit vectors are the unit imaginary quaternions, and a product of two of them is a unit quaternion. So $Spin(3)\cong S^3=\mathrm{Spin}(3)$. For general $n$ the spin group is not a sphere, and the identification with the spin group is a statement about $n=3$.

**Theorem (the double cover).** The map

$$
\rho:Spin(n)\to SO(n),\qquad \rho(s)(v)=s\,v\,s^{-1},
$$

is a surjective homomorphism of Lie groups with kernel $\{+1,-1\}$.

*Proof.* A product of an even number of unit vectors is invertible, and its inverse is a product of an even number of unit vectors, so $Spin(n)$ is a group. The map is a homomorphism because conjugation is one, and it lands in $O(n)$ because it preserves the form. Its image lies in $SO(n)$ because each reflection $v\mapsto -v$ is replaced by two factors and the determinant is a square. It is onto by the Cartan–Dieudonné theorem, which writes every rotation as an even number of reflections. The kernel is the set of $s$ acting trivially, that is the set of $s$ central in $\mathrm{Cl}(V)$, which is $\{+1,-1\}$. ∎

**The two turns.** A rotation by a full turn of $2\pi$ in $SO(n)$ corresponds to the element $-1$ of $Spin(n)$, since the rotor of angle $\theta$ is $\cos\tfrac\theta2+\sin\tfrac\theta2\,\vec u$ and at $\theta=2\pi$ it is $-e_t$. Only the rotor of angle $4\pi$ is $+e_t$. This is the geometric content of the word *double*: the sphere covers the rotation group twice, and one turn upstairs is half a turn downstairs.

**The Lie algebra.** $\mathfrak{spin}(n)$ is spanned by the bivectors $e_ie_j$ with $i<j$, of dimension $\binom n2$, and it is isomorphic to $\mathfrak{so}(n)$. For $n=3$ the dimension is three and the algebra is the one computed in the next section.

**Remark (the word *spin*).** The name of the group and the name of the number come from the same place: the cover is two-to-one, so a representation of the cover that does not descend to the rotation group is available, and its lowest one carries the number $\tfrac12$. Nothing in the definition of the sphere mentions $\tfrac12$. The number is a property of a carrier, and the next three sections construct the carrier.

## The Left-Regular Generators

**The matrix.** On the real basis $\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z)$ of $\mathbb{H}$, left multiplication by $\tilde q$ is the linear map $X\mapsto\tilde qX$, and its matrix has the products $\tilde qe_\nu$ as columns,

$$
L(\tilde q)_{\mu\nu}=\bigl[\tilde qe_\nu\bigr]_{\mu},
\qquad
L(\tilde q)=
\begin{pmatrix}
q_t&-q_x&-q_y&-q_z\\
q_x&q_t&-q_z&q_y\\
q_y&q_z&q_t&-q_x\\
q_z&-q_y&q_x&q_t
\end{pmatrix}.
$$

The first column is the coordinate column of $\tilde q$ itself, since $\tilde qe_t=\tilde q$, so the matrix determines the quaternion and the display is injective.

**The three generators.** With $L_k:=L(\vec e_k)$,

$$
L_x=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\qquad
L_y=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
L_z=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}.
$$

Each is real, antisymmetric, and a signed permutation matrix, and each has zero diagonal. The entries are the structure constants of $\mathbb{H}$, hence integers.

**The four properties.** Each is a one-line consequence of $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$.

1. $L_k\in M_4(\mathbb{R})$ and $L_k^{\mathsf T}=-L_k$.
2. $L_k^2=-\mathrm{I}_4$, because applying left multiplication by $\vec e_k$ twice is left multiplication by $\vec e_k^2=-e_t$.
3. $[L_x,L_y]=2L_z$, and cyclically, because $L$ is multiplicative and $\vec e_x\vec e_y=2\vec e_z$ in the commutator.
4. No $L_k$ is diagonal, and this is not an accident of the display: a real diagonal antisymmetric matrix is zero.

**The algebra and the group.** Define

$$
\mathfrak{g}_L:=\operatorname{span}_{\mathbb{R}}\{L_x,L_y,L_z\},\qquad
\mathrm{Spin}(3)_L:=\exp(\mathfrak{g}_L)=\{\,L(\tilde q):\tilde q\in\mathrm{Spin}(3)\,\}\subset SO(4).
$$

The algebra has real dimension three, the group has real dimension three, and $L$ is an isomorphism of Lie groups onto its image. The image is one of the two isoclinic copies of $S^3$ in the six-dimensional $SO(4)$.

**The exponential in closed form.** For a unit imaginary quaternion $\vec u$ and real $\theta$, the matrix $U=n_xL_x+n_yL_y+n_zL_z$ satisfies $U^2=-\mathrm{I}_4$, so

$$
\exp(\theta U)=\cos\theta\,\mathrm{I}_4+\sin\theta\,U=L\bigl(\cos\theta\,e_t+\sin\theta\,\vec u\bigr).
$$

The exponential is surjective onto the group and is not injective: the spheres of radius $2\pi k$ in $\mathfrak{g}_L$ go to $\mathrm{I}_4$, and the sphere of radius $\pi$ goes to $-\mathrm{I}_4$. The sign of a rotor is visible in the matrix, $L(-\tilde q)=-L(\tilde q)$, and the trace separates the two, $\operatorname{tr}L(\tilde q)=4q_t$.

## The Casimir and the Number One Half

**Step 1: normalize the generators.** The standard convention is $[J_i,J_j]=\varepsilon_{ijk}J_k$. The displayed bracket is twice that, so

$$
J_k:=\tfrac12L_k,\qquad [J_i,J_j]=\varepsilon_{ijk}J_k .
$$

**Step 2: form the quadratic Casimir.** Set

$$
\mathbf{J}^2:=J_x^2+J_y^2+J_z^2=\tfrac14\bigl(L_x^2+L_y^2+L_z^2\bigr).
$$

The element is invariant: it commutes with each $J_k$, because $\sum_k[J_i,J_k^2]=0$ by antisymmetry of $\varepsilon$. So its value is the same on every vector of an irreducible carrier, and it is a scalar there.

**Step 3: evaluate.** Since $L_k^2=-\mathrm{I}_4$, the sum of the three squares is $-3\mathrm{I}_4$, and

$$
\mathbf{J}^2=-\tfrac34\,\mathrm{I}_4 .
$$

The sign is the sign of the real normalization. The three $J_k$ are real antisymmetric, so they are anti-Hermitian, and the sum of their squares is negative definite.

**Step 4: read the number.** The spectral theorem for the compact group is stated with Hermitian generators, so pass to

$$
H_k:=iJ_k=\tfrac i2L_k .
$$

The three are Hermitian, since $L_k$ is real antisymmetric, and they obey the physicists' bracket,

$$
[H_i,H_j]=i\varepsilon_{ijk}H_k ,
$$

and their Casimir is the negative of the previous one,

$$
\mathbf{H}^2=H_x^2+H_y^2+H_z^2=\tfrac34\,\mathrm{I}_4 .
$$

On an irreducible carrier $\mathbf{H}^2=s(s+1)$ times the identity, by the definition of the spin of the carrier. Therefore

$$
s(s+1)=\tfrac34 \quad\Longrightarrow\quad s=\tfrac12 ,
$$

since $s\ge0$, the other root being $-\tfrac32$.

**The weights, as a second reading.** The eigenvalues of $H_z$ on $\mathbb{R}^4$ are $+\tfrac12$ twice and $-\tfrac12$ twice, so the weight set is $\{\pm\tfrac12\}$ and the carrier has complex dimension $2s+1=2$. The real dimension is $4$, twice the complex dimension, because the left-regular carrier is quaternionic: multiplication by $i$ is a real operator that commutes with the action and is not a scalar, so every complex dimension counts twice.

**Why the number is not read off a basis.** The three eigenvalues $\pm\tfrac12$ do not depend on the axis: the axis is a unit imaginary quaternion $\vec u$, the generator $U$ is conjugate to $L_z$ inside $\mathfrak{g}_L$, and conjugation preserves the spectrum. The spin is a property of the carrier, not of a direction, and no frame is chosen in the computation.

**Why the eigenvalue is the whole story.** The carrier $\mathbb{R}^4$ is irreducible for the rotor action, as proved in *The Spin Group via 4×4 Real Matrices*. On an irreducible carrier the Casimir has one eigenvalue, so $\tfrac34$ is not an average over a spectrum but the spectrum. Had the carrier split, the sum of the squares would have had several eigenvalues and the spin would not be a single number.

**The statement.** The left-regular representation on $\mathbb{R}^4$ carries spin $\tfrac12$. The three $L$-generators are the spin-$\tfrac12$ generators in real $4\times4$ form, and the number is read from $\sum_kL_k^2=-3\mathrm{I}_4$ with no complex number and no array.

## Two Rotors: Spin Zero and Spin One

**The composite.** Two rotors are two systems, each carrying spin $\tfrac12$ on its own spinor space $S$. The space $S$ is $\mathbb{R}^4$ read as a complex two-space through one of the complex structures of the previous article, and its two weight lines are the two weight spaces of $H_u$; the corpus's spinor plane is one of them, read over the reals. The composite carrier is the tensor square $S\otimes S$, of complex dimension four. The group acts by $g\cdot(x\otimes y)=gx\otimes gy$, and the generator of the axis $\vec u$ acts by

$$
A_{\mathrm{tot}}=A\otimes\mathrm{I}+\mathrm{I}\otimes A ,
$$

which is the Leibniz rule for a derivation written as a tensor: the generator acts on one factor at a time.

**Theorem (the split).** The tensor square decomposes as

$$
S\otimes S=\wedge^2S\ \oplus\ \mathrm{Sym}^2S ,
$$

of complex dimensions $1$ and $3$. Both summands are carried into themselves by the action, and the Casimir acts on them as the scalars $0$ and $2$.

*Proof.* The two subspaces are the eigenspaces of the swap $\sigma(x\otimes y)=y\otimes x$, with eigenvalues $-1$ and $+1$, and the action commutes with $\sigma$ because it acts on the two factors in the same way. Their dimensions are $\binom22=1$ and $\binom{2+1}{2}=3$. For the Casimir, expand the square of the total generator,

$$
\mathbf{H}^2_{\mathrm{tot}}=\sum_k\bigl(H_k\otimes\mathrm{I}+\mathrm{I}\otimes H_k\bigr)^2
=2\,\mathbf{H}^2\otimes\mathrm{I}+2\sum_k H_k\otimes H_k .
$$

The first term is $\tfrac32$ times the identity on the four-dimensional square. For the second, $\sum_kH_k\otimes H_k$ is the swap in the normalization of $\mathfrak{su}(2)$: it acts as $+\tfrac14$ on the symmetric part and as $-\tfrac34$ on the antisymmetric part, which is checked on a basis and which the trace identity $3\cdot\tfrac14+1\cdot(-\tfrac34)=0$ confirms. Adding, the symmetric part gets $\tfrac32+\tfrac12=2$ and the antisymmetric part gets $\tfrac32-\tfrac32=0$. ∎

**The swap projectors are the projectors of the algebra.** The two eigenspaces of $\sigma$ are the images of

$$
P_{+}=\tfrac12\bigl(\mathrm{id}+\sigma\bigr),\qquad P_{-}=\tfrac12\bigl(\mathrm{id}-\sigma\bigr),
$$

with $P_{\pm}^{2}=P_{\pm}$, $P_{+}P_{-}=0$ and $P_{+}+P_{-}=\mathrm{id}$, which is the algebra of an involution halved and the same construction as the two projectors $\tfrac12(\mathrm{id}\pm\natural)$ of *The Clebsch–Gordan Decomposition of the Biquaternion Algebra*. The antisymmetric summand is the singlet and the symmetric one is the triplet, so $P_{-}$ plays the role of $P_{0}$ and $P_{+}$ the role of $P_{1}$. The identification of the square $S\otimes S$ with the algebra passes through the isomorphism of the slot with its dual, and that is the place where a sign may enter; the assignment of summands does not depend on it.

**The spins.** The two values are $s(s+1)$ at the two integer spins,

$$
0=0\cdot(0+1),\qquad 2=1\cdot(1+1),
$$

so the antisymmetric part is spin $0$ and the symmetric part is spin $1$. In the physicist's notation the same statement reads $\tfrac12\otimes\tfrac12=0\oplus1$.

**The weight check.** The weights of the composite are the sums of the weights of the two factors, so the multiset is

$$
\tfrac12+\tfrac12=1,\qquad \tfrac12-\tfrac12=0,\qquad -\tfrac12+\tfrac12=0,\qquad -\tfrac12-\tfrac12=-1,
$$

that is $\{1,0,0,-1\}$, which is $\{0\}\cup\{\pm1,0\}$: one weight of the singlet and three of the triplet. The dimensions agree, $1+3=4$.

**The full turn, and what it proves.** The rotor of a full turn is $-e_t$. On the single spinor space it acts as $-1$, which is the reason the single rotor needs the double cover. On the tensor square it acts as $(-1)\otimes(-1)=+1$, so the composite is an action of the rotation group and not merely of its double cover. This is the precise sense in which two rotors make an integer-spin object: the sign that a single rotor carries cancels in pairs. It also fixes the parity: the antisymmetric summand is $+1$ and the symmetric summand is $+1$, and both are integer.

**The identification with the two integer carriers.** The singlet has dimension one and weight $\{0\}$; the triplet has dimension three and weights $\{\pm1,0\}$. Those are the data of the fixed line $\mathbb{R}e_t$ and of the vector part $\mathfrak{k}$ of the algebra, the two integer carriers of *From the Spin to the Carriers and the Closures*. Over $\mathbb{C}$ the composite is the complexification of those two real carriers: the complexification of the line has complex dimension one and the complexification of the vector part has complex dimension three. The identification is by the weight set and the dimension, which determine a carrier of the algebra among the three.

| composite | $\dim_\mathbb{C}$ | weights | $\mathbf{H}^2$ | $s$ | $2s+1$ | full turn |
| --- | --- | --- | --- | --- | --- | --- |
| $\wedge^2S$ | $1$ | $\{0\}$ | $0$ | $0$ | $1$ | $+1$ |
| $\mathrm{Sym}^2S$ | $3$ | $\{\pm1,0\}$ | $2$ | $1$ | $3$ | $+1$ |
| $S\otimes S$ | $4$ | $\{1,0,0,-1\}$ | $0,2$ | $0,1$ | $1+3$ | $+1$ |

**The dimension arithmetic.** Each rotor has $2\cdot\tfrac12+1=2$ states, the pair has $2\cdot2=4$, and the two integer carriers have $2\cdot0+1=1$ and $2\cdot1+1=3$ states, with $1+3=4$. The identity $2s+1=\dim$ holds at every step, and it holds with the multiplicities, since the doublet appears twice in the composite.

**Why no other spin occurs.** The split is by the eigenvalues of the swap, which are $+1$ and $-1$, so there are exactly two summands, of dimensions $3$ and $1$, and their spins are forced by $2s+1$ to be $1$ and $0$. The tensor square has dimension four, and no third summand fits beside a summand of dimension three and a summand of dimension one.

## What the Generators Do Not Give

**One algebra, three carriers.** The Casimir is one element, and its value depends on the carrier on which it acts. On the three carriers of the algebra the values are

| carrier | $\dim_\mathbb{R}$ | $s$ | value of the Casimir |
| --- | --- | --- | --- |
| fixed line $\mathbb{R}e_t$ | $1$ | $0$ | $0$ |
| spinor plane, left-regular carrier | $4$ real, $2$ complex | $\tfrac12$ | $\tfrac34$ |
| vector part $\mathfrak{k}$ | $3$ | $1$ | $2$ |

The three values are $s(s+1)$ at $s=0,\tfrac12,1$. The same quadratic element gives all three, and the difference is the module, not the element.

**The $L$-generators are tied to one carrier.** The three matrices $L_k$ act on $\mathbb{R}^4$ and nowhere else. They are the spin-$\tfrac12$ generators, and the number they return is $\tfrac12$. They do not return $\tfrac32$, and no change of basis in $\mathbb{R}^4$ will make them do so, because the carrier is irreducible and its spin is fixed by its dimension and its weights.

**Other spins require other carriers.** To obtain spin $s$ the same procedure is applied on a carrier of complex dimension $2s+1$: form the Casimir of the representation, read its eigenvalue, solve $s(s+1)=\lambda$. The procedure is uniform; the input is the carrier. On the vector part the representation is the adjoint one, the Casimir value is $2$, and the spin is $1$.

**The quadratic is not injective.** The value $\lambda=s(s+1)$ determines $s$ only up to $s\mapsto-1-s$. The value $\tfrac34$ is compatible with $s=\tfrac12$ and with $s=-\tfrac32$. The largest weight being non-negative, or the dimension being $2s+1$, fixes the choice. A computation that reads the Casimir alone and reports a spin has used one datum where two are needed.

**The sign.** The value $-\tfrac34$ on the real antisymmetric generators and $+\tfrac34$ on the Hermitian ones differ by $i^2$, since $H_k=iJ_k$. Both are correct, and a reader who meets one in one article and the other in another has met one invariant in two normalizations. The magnitude $\tfrac34$ is what carries the spin.

**What the sphere gives and what a matrix gives.** Everything above is a statement about the sphere $S^3$ and about one display of it on $\mathbb{R}^4$. A reader who takes the display for the group will conclude that the spin is a property of a $4\times4$ matrix. It is not: it is a property of the carrier, and the same sphere has other carriers with other spins.

## Corrections

**The sentences that must not be written as they stand.** Each is a real error in the form given, and each is repaired by one of the sections above.

1. **"The spin group is $SU(2)$", written as an equality of objects.** As an isomorphism the sentence is true, $\mathrm{Spin}(3)\cong SU(2)$; as an equality it is false. $SU(2)$ is the image of one display, the $2\times2$ complex one, and the isomorphism is that display.
2. **"The spin group is a matrix group."** It is a subset of $\mathbb{H}$, which is an algebra. Every matrix group in this article is an image of it under a display.
3. **"$Spin(n)$ is $S^3$."** $Spin(3)$ is $S^3$. For $n\ge4$ the spin group is a cover of $SO(n)$ of dimension $\binom n2$, and it is not a sphere.
4. **"The $L$-generators give all spins."** They give $\tfrac12$, on $\mathbb{R}^4$. Another spin needs another carrier, and the same Casimir read there.
5. **"One-sided multiplication can act by an automorphism after a normalization."** It cannot, for an invertible element other than the unit; the count of factors forbids it.
6. **"The two-sided operator is conjugation by the inverse for a rotor and something else for a boost, because a boost has $\tilde U_{\mathrm b}^{\natural}\ne\tilde U_{\mathrm b}^{-1}$."** The premise is false: a boost has norm one, so $\tilde U_{\mathrm b}^{\natural}=\tilde U_{\mathrm b}^{-1}$ and the $\natural$-operator is conjugation by the inverse for it as well. The genuine difference between the sectors is that the $*$-operator, which is the one that carries Hermitian elements to Hermitian elements, is not conjugation by the inverse on a boost, since $\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b}\ne\tilde U_{\mathrm b}^{-1}$.
7. **"The Casimir eigenvalue is the spin."** It is $s(s+1)$. The spin follows after the root is chosen, and the quadratic has two roots.
8. **"The Casimir of the left-regular display is $+\tfrac34$."** It is $-\tfrac34$ for the real antisymmetric generators, and $+\tfrac34$ for the Hermitian ones $H_k=iJ_k$. Both are the same invariant in two normalizations.
9. **"Two rotors give spin $\tfrac12$ again, or spin $2$."** They give $0$ and $1$. The tensor square of a two-dimensional carrier has dimension four, and the two integer carriers exhaust it.
10. **"The sign of a full turn is a property of the spin group."** It is a property of a carrier. It is $-1$ on the single spinor plane and $+1$ on both summands of the tensor square, and the group is the same in the three cases.

## Verification

**How the numbers were obtained.** The two-sided identities were checked on random biquaternions with all sixteen real coefficients drawn independently, in double precision, and the algebraic ones were checked exactly with the structure constants of $\mathbb{H}$. The Casimir was formed from the three real matrices $L_k$ and from the Hermitian $H_k=iJ_k$, and the tensor square was built with the Leibniz generator $A\otimes\mathrm{I}+\mathrm{I}\otimes A$; the exponentials were computed from the series, not from the closed form.

| claim | what was computed | residual |
| --- | --- | --- |
| one-sided is not multiplicative | $\tilde R(\tilde X\tilde Y)$ against $(\tilde R\tilde X)(\tilde R\tilde Y)$, $200$ samples | fails in $200/200$ |
| $\natural$-operator is the scaled conjugation | $\tilde Q\tilde X\tilde Q^{\natural}$ against $\langle\tilde Q\rangle_{\natural}\tilde Q\tilde X\tilde Q^{-1}$ | $1.4\cdot10^{-14}$ |
| a rotor has $\natural$ as its inverse | $\tilde u^{\natural}-\tilde u^{-1}$ | $0$ |
| a boost is Hermitian | $\tilde U_{\mathrm b}^{*}-\tilde U_{\mathrm b}$, $\phi=0.5,\,2.0$ | $0$ |
| a boost has $\natural$ as its inverse | $\tilde U_{\mathrm b}^{\natural}-\tilde U_{\mathrm b}^{-1}$ | $4.4\cdot10^{-16}$ |
| a general Lorentz element has norm one | $\langle\tilde U_{\mathrm b}\tilde u\rangle_{\natural}-1$ | $1.3\cdot10^{-16}$ |
| the $*$-operator is not the inverse for it | $\tilde Q^{*}-\tilde Q^{-1}$ | $1.38$ |
| the $*$-operator preserves the star | $\Theta_{*}(\tilde X^{*})$ against $\Theta_{*}(\tilde X)^{*}$ | $2.0\cdot10^{-14}$ |
| the $\natural$-operator fails multiplicativity off norm one | $\Theta_{\natural}(\tilde X\tilde Y)$ against $\Theta_{\natural}(\tilde X)\Theta_{\natural}(\tilde Y)$ | relative error $20.4$ |
| the $\natural$-operator is multiplicative at norm one | the same, with a rotor | $1.8\cdot10^{-15}$ |
| the bracket of the halves | $[J_x,J_y]-J_z$ | $0$ |
| the Hermitian bracket | $[H_x,H_y]-iH_z$ | $0$ |
| the Casimir, real normalization | $\sum_kJ_k^2+\tfrac34\mathrm{I}_4$ | $0$ |
| the Casimir, Hermitian normalization | $\sum_kH_k^2-\tfrac34\mathrm{I}_4$ | $0$ |
| the weights | eigenvalues of $H_z$ | $\pm\tfrac12$, each twice |
| the tensor weights | eigenvalues of $H_z\otimes\mathrm{I}+\mathrm{I}\otimes H_z$ | $\{1,0,0,-1\}$ |
| the tensor Casimir | eigenvalues of $\mathbf{H}^2_{\mathrm{tot}}$ | $0$ once, $2$ thrice |
| the split | dimensions of the symmetric and antisymmetric parts | $3$ and $1$ |
| the split is invariant | commutator of the swap with the Casimir | $0$ |
| the full turn | $\exp(2\pi i\,\mathbf{H})$ on the tensor square | $+\mathrm{I}_4$ |
| the full turn on one rotor | $\exp(2\pi i\,H_z)$ on the spinor plane | $-\mathrm{I}_2$ |

**The two rows that carry the article.** The Casimir row is the extraction of the number: the sum of the three squares is a scalar, and the scalar is $\pm\tfrac34$. The tensor Casimir row is the split: two eigenvalues, $0$ and $2$, and no third, which is why the composite has exactly the two spins.

**One check that is not numerical.** The irreducibility of $\mathbb{R}^4$ and the completeness of the list of carriers are exact statements and no sample can confirm them. They are proved elsewhere in the corpus, and the numbers above confirm only the instances computed.

## Summary

The two-sided product is forced. A one-sided multiplication is multiplicative only for the unit, since $R(XY)$ carries one factor $R$ and $(RX)(RY)$ carries two. Conjugation, $\Theta(X)=RXR^{-1}$, is multiplicative for every invertible $R$.

In the biquaternion algebra two two-sided operators are available. The $\natural$-operator equals the norm times conjugation by the inverse, so it is an automorphism exactly on the norm-one surface, where it is conjugation by the inverse; the rotor sphere and the boost hyperboloid both lie on that surface. The $*$-operator always preserves the Hermitian adjoint and is conjugation by the inverse exactly on the unitary elements. On the rotor sphere the two operators coincide, because a real unit quaternion has $\tilde u^{*}=\tilde u^{\natural}=\tilde u^{-1}$; that coincidence is what makes a rotor the element whose two-sided action is unambiguous.

The spin group is $S^3$, of real dimension three, and it is $Spin(3)$; for $n\ge4$ the spin group is a different object. The double cover $S^3\to SO(3)$ has kernel $\{\pm1\}$, a full turn upstairs is $-e_t$ downstairs the identity, and two turns upstairs are the identity. The Lie algebra is spanned by the three bivectors, which in the real left-regular display are the matrices $L_x,L_y,L_z$.

The Casimir of the halved generators is $\mathbf{J}^2=-\tfrac34\mathrm{I}_4$ in the real antisymmetric normalization and $\mathbf{H}^2=+\tfrac34\mathrm{I}_4$ in the Hermitian one. On the irreducible carrier $\mathbb{R}^4$ the Casimir is a scalar, $s(s+1)=\tfrac34$, and $s=\tfrac12$. The weights $\pm\tfrac12$ confirm it, and the dimension counts it twice because the carrier is quaternionic.

Two rotors give the tensor square, of dimension four, which splits by the swap into the antisymmetric part of dimension one and the symmetric part of dimension three. The Casimir takes the values $0$ and $2$ there, that is $s(s+1)$ at $s=0$ and $s=1$, and the full turn is $+1$ on both summands. The composite is therefore an action of the rotation group, and its two summands are the complexified fixed line and the complexified vector part.

What the $L$-generators do not give is the rest of the spectrum. They act on one carrier, they return one spin, and the same Casimir read on other carriers returns the others.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\mathbb{H}$, $\mathbb{B}$ | the quaternions and the biquaternions $\mathbb{C}\otimes\mathbb{H}$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the real basis, $\vec e_k^2=-e_t$, $\vec e_x\vec e_y=\vec e_z$ |
| $\natural$, $*$ | quaternion conjugation and the Hermitian adjoint $*=\bar{\cdot}\circ\natural$ |
| $\langle\tilde Q\rangle_{\natural}$ | the value of the quaternion norm, $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ |
| $\Theta_{\natural}$, $\Theta_{*}$ | $\tilde X\mapsto\tilde Q\tilde X\tilde Q^{\natural}$ and $\tilde X\mapsto\tilde Q\tilde X\tilde Q^{*}$ |
| $\mathrm{Spin}(3)=S^3=Sp(1)$ | the spin group: unit quaternions |
| $L(\tilde q)$, $L_x,L_y,L_z$ | the real left-regular matrix and its three generators |
| $\mathfrak{g}_L$, $\mathrm{Spin}(3)_L$ | $\operatorname{span}_{\mathbb{R}}\{L_k\}$ and $\exp(\mathfrak{g}_L)\subset SO(4)$ |
| $J_k=\tfrac12L_k$ | the normalized generators, $[J_i,J_j]=\varepsilon_{ijk}J_k$ |
| $H_k=iJ_k=\tfrac i2L_k$ | the Hermitian generators, $[H_i,H_j]=i\varepsilon_{ijk}H_k$ |
| $\mathbf{H}^2$ | the quadratic Casimir $\sum_kH_k^2$, equal to $s(s+1)$ on an irreducible carrier |
| $s$ | the spin of a carrier, read from the Casimir and the dimension |
| $S$ | the spinor space of complex dimension two, carrying $s=\tfrac12$ |
| $\wedge^2S$, $\mathrm{Sym}^2S$ | the antisymmetric and symmetric parts of the tensor square |

## Further Reading

- [The Spin Group via 4×4 Real Matrices](the-spin-group-via-4x4-real-matrices.html), for the left-regular display, its generators, its exponential and the proof that no generator is diagonal.
- [From the Spin to the Carriers and the Closures](the-carriers-the-representation-the-spin-and-the-closure.html), for the three carriers, the spin table, the quadratic element and the identity $2s+1=\dim_\mathbb{R}$.
- [Quaternion Rotations and Reflections](quaternion-rotations-and-reflections.html), for the group of unit quaternions and the double cover $Sp(1)\to SO(3)$.
- [The Two-Sided Operators and the Spin Group](the-two-sided-operators-and-the-spin-group.html), for the two-sided operators of the algebra and their relation to the spin group.
- [The Pin and Spin Groups of the Quaternion Algebra](the-pin-and-spin-groups-of-the-quaternion-algebra.html), for the Clifford description of the same groups.
- [The Lie Correspondence and the Adjoint Representation](the-lie-correspondence-and-the-adjoint-representation.html), for the exponential map and the place of a three-dimensional algebra inside a larger one.
- I. R. Porteous, *Clifford Algebras and the Classical Groups*, ch. 13 and 16, for the spin groups, the double covers and the two isoclinic copies of $S^3$ in $SO(4)$.
- S. Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, ch. II, for the Casimir element and the highest weight of an irreducible representation.
