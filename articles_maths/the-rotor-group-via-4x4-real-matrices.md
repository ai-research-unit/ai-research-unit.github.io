# __The Rotor Group via $4\times4$ Real Matrices__

## Introduction

The rotor group is the group of unit quaternions. It is the sphere $S^3$ with the multiplication of $\mathbb{H}$, and its real dimension is three. The group has many matrix displays, and the one every text prints first is the complex one: the $2\times2$ matrices of $SU(2)$. That display is a good one, and it is not the only one. This article develops a second display in full, the $4\times4$ **real** left-regular matrices, and states exactly what the second display buys and what it costs.

**A group is not its matrices.** The rotor group is $S^3$. The group $SU(2)$ is the image of $S^3$ under one particular map, the $2\times2$ complex display. The two are isomorphic, and the isomorphism is a choice of display, not a definition. The sentence "the rotor group is $SU(2)$" is therefore true up to isomorphism and misleading in practice, because it makes the display look like the object. When the display is mistaken for the object, the properties of the display are read as properties of the group. The worst of those readings is the belief that the group has a preferred axis, which it does not.

**What the second display is.** Left multiplication by a unit quaternion is an isometry of $\mathbb{H}$ read as a four-dimensional real Euclidean space, so it is a $4\times4$ real orthogonal matrix of determinant one. The assignment $\tilde q\mapsto L(\tilde q)$ is multiplicative, injective, and carries the sign, $L(-\tilde q)=-L(\tilde q)$. Its image is a three-dimensional subgroup of the six-dimensional $SO(4)$, written here $SO_R(4)_{\mathrm{left}}$. The three infinitesimal generators $L_x,L_y,L_z$ are real antisymmetric matrices with integer entries.

**What the article argues.** The $4\times4$ real display is a faithful writing of the same group, with the same Lie algebra up to isomorphism, the same exponential and the same composition law. It differs from the $2\times2$ display in three ways that matter, and the rest follows from them: the field is $\mathbb{R}$ and not $\mathbb{C}$, the matrix is twice as large, and no generator is diagonal. The third difference is the one that matters, and it is a theorem and not a preference, because a real diagonal antisymmetric matrix is zero. In the complex display exactly one generator is diagonal, and the display therefore marks an axis. The mark is the choice of a complex structure on $\mathbb{H}$, which is a point of $S^2$.

**Roadmap.** The next section fixes the vocabulary and refuses the conflation. Then come the complex display, briefly, because the comparison needs it; the real display in full; the two side by side; the structural theorems; the two lists of what changes and what does not; the worked examples; the trade; the sentences that must not be written; the numerical check.

## The Rotor Group and Its Matrix Representations

**Definition (rotor group).** The **rotor group** is

$$
\mathrm{Rot}:=\{\tilde q\in\mathbb{H}:\langle\tilde q\rangle_{\natural}=1\}=\{\tilde q\in\mathbb{H}:\lvert\tilde q\rvert=1\}=S^3,
$$

the unit quaternions under quaternion multiplication, of real dimension three. The corpus writes it $Sp(1)$ and calls its elements versors or rotors. This article writes $\mathrm{Rot}$ to keep the name of the group apart from the names of its displays.

**Definition (matrix display).** A **matrix display** of the rotor group is a homomorphism into $GL(V)$, for a real or complex vector space $V$, from $\mathrm{Rot}$ or from a product of copies of it. The rotor group is not any one of its displays. Four of them matter here.

- The **defining display** is $\mathsf M_2:\mathrm{Rot}\to SU(2)\subset M_2(\mathbb{C})$, left multiplication on $\mathbb{H}$ read as a complex plane. It is written $\mathsf M_2$ because it is the restriction to $\mathrm{Rot}$ of the $2\times2$ element display fixed in *Matrix Representations Conventions*.
- The **left regular display** is $L:\mathrm{Rot}\to SO_R(4)_{\mathrm{left}}\subset SO(4)$, left multiplication on $\mathbb{H}$ read as a real four-dimensional space. It is the subject of this article.
- The **adjoint, or vector, display** is $\operatorname{Ad}:\mathrm{Rot}\to SO(3)$, the conjugation $\tilde q\mapsto[\tilde X\mapsto\tilde q\tilde X\tilde q^{-1}]$ on the imaginary part. It is the classical two-to-one cover, and it is not injective.
- The **two-sided display** is $\rho:\mathrm{Rot}\times\mathrm{Rot}\to SO(4)$, $(\tilde q_L,\tilde q_R)\mapsto[\tilde X\mapsto\tilde q_L\tilde X\tilde q_R^{-1}]$. It is surjective with kernel $\{\pm(\mathrm{I}_4,\mathrm{I}_4)\}$.

**The rule.** The article never writes "the rotor group is $SU(2)$" and never writes "$SU(2)=S^3$". It writes: the rotor group is $S^3$, and $SU(2)$ is its defining display. The same rule separates $S^3$ from the left regular image. The rule is not pedantry. Every error listed under *Pitfalls and Corrections* is a consequence of breaking it, and each is repaired by asking which map is meant.

**Remark (the corpus writes $Sp(1)\cong SU(2)$, and that is consistent).** The quaternion articles of the corpus say that the group $Sp(1)$ of unit quaternions is $SU(2)$. Read as an isomorphism the sentence is true, since $\mathsf M_2$ is an isomorphism onto $SU(2)$. Read as an identity of objects it is the conflation this article refuses. The two readings differ exactly when two displays are compared, which is the whole subject here.

### The Four Displays and Their Kernels

**The table.** The four displays differ in their targets and in their kernels, and the kernels are the quickest way to see that they are different maps.

| display | map | target | kernel | image |
|---|---|---|---|---|
| defining | $\mathsf M_2$ | $SU(2)\subset M_2(\mathbb{C})$ | $\{1\}$ | all of $SU(2)$ |
| left regular | $L$ | $SO_R(4)_{\mathrm{left}}\subset SO(4)$ | $\{1\}$ | the left copy |
| adjoint | $\operatorname{Ad}$ | $SO(3)$ | $\{\pm1\}$ | all of $SO(3)$ |
| two-sided | $\rho$ | $SO(4)$ | $\{\pm(\mathrm{I}_4,\mathrm{I}_4)\}$ | all of $SO(4)$ |

**What the kernel column says.** Two of the four displays carry the sign and two do not, in the following sense. The adjoint display is two-to-one because $\tilde q$ and $-\tilde q$ induce the same conjugation, and the two-sided display is two-to-one for the same reason on both factors. The defining and the left regular displays are injective, so on their images they are isomorphisms of groups and not coverings. This is the first thing the left regular display shares with the defining one and does not share with the adjoint one: it is a faithful writing, and the sign is visible in the matrix.

## The Defining Display

**The matrices.** The corpus fixes the $2\times2$ display once, on the four units,

$$
\mathsf M_2(e_t)=I_2,\qquad
\mathsf M_2(\vec e_x)=\begin{pmatrix}0&-i\\-i&0\end{pmatrix},\qquad
\mathsf M_2(\vec e_y)=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
\mathsf M_2(\vec e_z)=\begin{pmatrix}-i&0\\0&i\end{pmatrix},
$$

and extends it by linearity. For a real quaternion $\tilde q=q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$,

$$
\mathsf M_2(\tilde q)=q_tI_2+q_x\mathsf M_2(\vec e_x)+q_y\mathsf M_2(\vec e_y)+q_z\mathsf M_2(\vec e_z)
=\begin{pmatrix}q_t-iq_z&-iq_x-q_y\\-iq_x+q_y&q_t+iq_z\end{pmatrix}.
$$

**The group.** The display is multiplicative, since it is the restriction of an algebra isomorphism. For unit $\tilde q$ the matrix is unitary, $\mathsf M_2(\tilde q)^{\dagger}\mathsf M_2(\tilde q)=\mathsf M_2(\tilde q^{\natural})\mathsf M_2(\tilde q)=\mathrm{I}_2$, and its determinant is $\langle\tilde q\rangle_{\natural}=1$. So $\mathsf M_2$ carries $\mathrm{Rot}$ into $SU(2)$, and it is onto because every $SU(2)$ matrix has the displayed shape with real $q_\mu$ and unit norm. It is injective because the four entries recover $(q_t,q_x,q_y,q_z)$.

**The generators.** Write $J_k:=\mathsf M_2(\vec e_k)$, so $J_k$ is the image of the $k$-th basis vector and not a new object. The three are anti-Hermitian, $J_k^{\dagger}=-J_k$, and each squares to $-\mathrm{I}_2$. Since the display is multiplicative and $\vec e_x\vec e_y=\vec e_z$, the bracket is

$$
[J_x,J_y]=2J_z,\qquad[J_y,J_z]=2J_x,\qquad[J_z,J_x]=2J_y,
$$

that is $[J_i,J_j]=2\varepsilon_{ijk}J_k$. The factor of two is the factor of two of the quaternion bracket, $\vec e_x\vec e_y-\vec e_y\vec e_x=2\vec e_z$, and it appears here for the same reason it appears on the $4\times4$ side. It is not a property of the size of the matrix.

**Remark (the normalized generators and the familiar bracket).** The rotation generator of the corpus is $\tfrac12\vec u$ acting by commutator, and the same normalization here is $\tfrac12J_k$. For the normalized generators the bracket is the familiar one,

$$
[\tfrac12J_x,\tfrac12J_y]=\tfrac12J_z,
$$

that is $[\tfrac12J_i,\tfrac12J_j]=\varepsilon_{ijk}\tfrac12J_k$. Both normalizations are correct and they describe one algebra. The choice is a choice of basis, and the article keeps the unnormalized pair $J_k$, $L_k$ so that the two displays are compared at the same normalization.

**The exponential.** For a unit imaginary quaternion $\vec u=n_x\vec e_x+n_y\vec e_y+n_z\vec e_z$ and a real $\theta$, the matrix $N=n_xJ_x+n_yJ_y+n_zJ_z$ satisfies $N^2=-\mathrm{I}_2$, so the exponential series collapses,

$$
\exp(\theta N)=\cos\theta\,\mathrm{I}_2+\sin\theta\,N=\mathsf M_2\bigl(\cos\theta\,e_t+\sin\theta\,\vec u\bigr).
$$

The parameter $\theta$ is the half angle. The conjugation action of $\tilde q=\cos\theta+\sin\theta\vec u$ rotates the imaginary part by $2\theta$, which is the classical statement that a rotor of angle $\theta$ produces a rotation of angle $2\theta$.

**The diagonal generator, and the frame.** Of the three generators exactly one is diagonal, $J_z=\operatorname{diag}(-i,i)$, and the other two have zero diagonal. The display therefore marks the axis $\vec e_z$: a reader of the matrix can see which direction the display prefers. Nothing in the group prefers it. The marking is a property of the display, and *Structural Theorems* states the precise sense in which it is a choice of complex structure on $\mathbb{H}$.

## The Left Regular Display

**The matrix.** On the real basis $\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z)$ of $\mathbb{H}$, left multiplication by $\tilde q$ is the linear map $X\mapsto\tilde qX$. Its matrix has the products $\tilde qe_\nu$ as columns, which is the rule of the axis-free frame of *Matrix Representations Conventions*,

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

This is the matrix $L_{\mathrm{axf}}(\tilde q)$ of that article read at real coefficients: the corpus builds it for the biquaternion algebra, and this article uses the copy carried by the real quaternion subalgebra. The first column is $(q_t,q_x,q_y,q_z)^{\mathsf T}$, the coordinate column of $\tilde q$ itself, because $\tilde qe_t=\tilde q$. The other three columns are the products with the three vector units.

**The three generators.** The generators are the matrices of the three vector units, $L_k:=L(\vec e_k)$,

$$
L_x=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\qquad
L_y=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
L_z=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}.
$$

**The properties of the generators.** Each of the four statements below is a one-line consequence of the multiplication table and is checked exactly under *Verification*.

1. **Real and antisymmetric.** $L_k\in M_4(\mathbb{R})$ and $L_k^{\mathsf T}=-L_k$. The entries are the structure constants, hence integers.
2. **Square minus one.** $L_k^2=-\mathrm{I}_4$, because $\vec e_k^2=-e_t$ and the display is multiplicative, so applying left multiplication by $\vec e_k$ twice is left multiplication by $-e_t$.
3. **The bracket.** $[L_x,L_y]=2L_z$ and cyclically, because $L(\tilde q)L(\tilde p)=L(\tilde q\tilde p)$ and $\vec e_x\vec e_y=\vec e_z$.
4. **Signed permutations with zero diagonal.** Each $L_k$ has exactly one nonzero entry in each row and in each column, that entry $\pm1$, and a zero diagonal. It follows that none of them is diagonal.

**Remark (what is not true of the generators).** It is tempting to say that each generator has a zero row and a zero column at the coordinate it fixes. It does not, since $L_x$ has a nonzero entry in every row and every column. What is true is stronger and more useful. In the basis $(e_t,\vec e_k,\vec e_i,\vec e_j)$, with $(i,j,k)$ cyclic, the generator $L_k$ is block diagonal with two copies of one and the same $2\times2$ rotation block, and its two nonzero entries per block sit off the diagonal. The fixed coordinate does not appear as a zero line; it appears as the cut between the two blocks.

**The algebra.** Define

$$
\mathfrak{g}_L:=\operatorname{span}_{\mathbb{R}}\{L_x,L_y,L_z\}\subset\mathfrak{so}(4,\mathbb{R}),
$$

of real dimension three. A general element is $aL_x+bL_y+cL_z$ with real $a,b,c$, the antisymmetric matrix

$$
aL_x+bL_y+cL_z=
\begin{pmatrix}0&-a&-b&-c\\a&0&-c&b\\b&c&0&-a\\c&-b&a&0\end{pmatrix}.
$$

The bracket closes on $\mathfrak{g}_L$ with $[L_i,L_j]=2\varepsilon_{ijk}L_k$, so $\mathfrak{g}_L$ is a three-dimensional real Lie algebra. It is isomorphic to $\mathfrak{su}(2)$ by $L_k\mapsto J_k$, and isomorphic to $\mathfrak{so}(3)$ by the map to the cross-product generators. The isomorphism is not an equality: $\mathfrak{g}_L$ is a subspace of $\mathfrak{so}(4,\mathbb{R})$ and $\mathfrak{su}(2)$ is a subspace of $\mathfrak{u}(2)$, and the two subspaces are written in matrices of different sizes.

**The group.** Define

$$
SO_R(4)_{\mathrm{left}}:=\exp(\mathfrak{g}_L)=\{\,L(\tilde q):\tilde q\in\mathrm{Rot}\,\}\subset SO(4),
$$

of real dimension three inside the six-dimensional $SO(4)$. That the two descriptions agree is a theorem of *Structural Theorems*. The closed form below gives $\exp(\mathfrak{g}_L)\subset\{L(\tilde q):\tilde q\in\mathrm{Rot}\}$, and the other inclusion follows from the polar form of a unit quaternion.

**The exponential, in closed form.** Let $\vec u$ be a unit imaginary quaternion and $\theta$ real. Since $\vec u^2=-e_t$, the matrix $U=n_xL_x+n_yL_y+n_zL_z$ satisfies $U^2=-\mathrm{I}_4$, and the series collapses,

$$
\exp(\theta U)=\cos\theta\,\mathrm{I}_4+\sin\theta\,U=L\bigl(\cos\theta\,e_t+\sin\theta\,\vec u\bigr).
$$

Every unit quaternion is $\cos\theta\,e_t+\sin\theta\,\vec u$ with $0\le\theta\le\pi$, so the exponential is surjective onto the group, with an explicit preimage for every element. It is not injective: $\exp(\theta U)=\exp((\theta+2\pi)U)$ for every $\theta$, and $\exp(\pi U)=-\mathrm{I}_4$ for every invertible $\vec u$. The kernel of the exponential is therefore the union of the spheres of radius $2\pi k$ in $\mathfrak{g}_L$,

$$
\{X\in\mathfrak{g}_L:\exp X=\mathrm{I}_4\}=\{2\pi k\,\vec u\cdot L:\ k\in\mathbb{Z},\ \vec u\in S^2\}.
$$

**Remark (surjective, and still not a diffeomorphism).** The exponential of a compact group is always surjective, and this group is compact, so surjectivity here is not an accident of the display. The map is nevertheless neither injective nor a local diffeomorphism at the spheres of radius $\pi$: the sphere $\lvert X\rvert=\pi$ collapses to the single matrix $-\mathrm{I}_4$. A reader who has been warned that the exponential is not surjective in general should read the warning as a statement about non-compact groups, and this example as the compact case where the map is onto and still far from injective.

## The Parallel

**The two displays side by side.** The table below is the article in one screen. The right column is what the rest of the article develops.

| item | $\mathsf M_2$, defining | $L$, left regular |
|---|---|---|
| group | $SU(2)\subset M_2(\mathbb{C})$ | $SO_R(4)_{\mathrm{left}}\subset SO(4)$ |
| Lie algebra | $\mathfrak{su}(2)=\operatorname{span}_{\mathbb{R}}\{J_x,J_y,J_z\}$ | $\mathfrak{g}_L=\operatorname{span}_{\mathbb{R}}\{L_x,L_y,L_z\}$ |
| group as an exponential | $SU(2)=\exp(\mathfrak{su}(2))$ | $SO_R(4)_{\mathrm{left}}=\exp(\mathfrak{g}_L)$ |
| matrix size | $2\times2$ | $4\times4$ |
| field | $\mathbb{C}$ | $\mathbb{R}$ |
| carrier | $\mathbb{C}^2$, real dimension four | $\mathbb{R}^4$ |
| group dimension | $3$ | $3$ |
| ambient dimension | $4$ real, $\mathfrak{u}(2)$ | $6$ real, $\mathfrak{so}(4)$ |
| faithful | yes | yes |
| bracket of the raw generators | $2\varepsilon_{ijk}$ | $2\varepsilon_{ijk}$ |
| bracket after halving | $\varepsilon_{ijk}$ | $\varepsilon_{ijk}$ |
| a diagonal generator | yes, $J_z$ | no |
| determinant of a unit element | $1$ | $1$ |
| trace | $2q_t$ | $4q_t$ |

**The two rows that are easy to get wrong.** The bracket row is the same on both sides, and it is the same because the bracket of the two displays is the image of one and the same quaternion bracket. A table that shows $\varepsilon_{ijk}$ on one side and $2\varepsilon_{ijk}$ on the other is comparing two normalizations of the generators, not two representations. The trace row differs, and it differs by the factor of the size: the trace of a left multiplication is four times the scalar part, the trace of the defining display is twice it. Both recover $q_t$, which is what the trace is for.

**The exponential side by side.** For a unit axis and an angle the two closed forms are one formula in two sizes,

$$
\exp(\theta N)=\cos\theta\,\mathrm{I}_2+\sin\theta\,N,
\qquad
\exp(\theta U)=\cos\theta\,\mathrm{I}_4+\sin\theta\,U .
$$

The identity is the same, $N^2=-\mathrm{I}_2$ and $U^2=-\mathrm{I}_4$. The images are the same element of the group, $\cos\theta+\sin\theta\vec u$. Only the size of the identity matrix changes.

## Structural Theorems

**Theorem (isomorphism).** The map $L:\mathrm{Rot}\to SO_R(4)_{\mathrm{left}}$ is an isomorphism of Lie groups. Both sides have real dimension three.

*Proof.* The display is multiplicative, $L(\tilde q)L(\tilde p)=L(\tilde q\tilde p)$, because the $\nu$-th column of the left side is the coordinate column of $\tilde q\tilde p e_\nu=\tilde q(\tilde pe_\nu)$ and the $\nu$-th column of the right side is $\tilde q$ acting on the coordinate column of $\tilde pe_\nu$. It is injective, since the first column recovers $\tilde q$. It is smooth, because the entries are the coordinates of $\tilde q$. A bijective smooth homomorphism of Lie groups with smooth inverse is an isomorphism, and here the inverse is the first column. Both sides are three-dimensional: the group is $S^3$, and the image is the exponential of a three-dimensional algebra. ∎

**Theorem (faithfulness and the sign).** $L$ is injective and $L(-\tilde q)=-L(\tilde q)$. Hence the display carries the sign, and every element of $S^3$ is recovered from its matrix, sign included.

*Proof.* Injectivity is the first column, as above. For the sign, $L(-\tilde q)$ is left multiplication by $-\tilde q$, which is the negative of left multiplication by $\tilde q$. ∎

**Remark (what faithfulness does and does not mean).** The adjoint display is not faithful: $\tilde q$ and $-\tilde q$ induce the same rotation of the imaginary part, which is the two-to-one cover $S^3\to SO(3)$. The left regular display is faithful because it does not confine itself to the imaginary part. Left multiplication by $\vec e_z$ sends $e_t$ to $\vec e_z$, so the scalar line is mixed into the vector part and the sign shows up as $L(-\tilde q)\neq L(\tilde q)$. A reader who looks only at the rotation induced on the imaginary part still cannot tell $\tilde q$ from $-\tilde q$. A reader who looks at the matrix can.

**Theorem (irreducibility).** $\mathbb{R}^4$ is an irreducible real representation of $\mathrm{Rot}$ under left multiplication. It does not split as a line plus a three-space.

*Proof.* Let $W\subset\mathbb{H}$ be a real subspace carried into itself by left multiplication by every unit quaternion, hence by every quaternion, since the unit sphere spans $\mathbb{H}$ over $\mathbb{R}$ and scalar multiples are limits. If $W\neq0$ choose $X\in W$ with $X\neq0$. Then $\tilde qX\in W$ for every $\tilde q$, and left multiplication by $X$ is a linear isomorphism of $\mathbb{H}$, so $W$ contains $\{\tilde qX\}=\mathbb{H}$. Hence $W=\mathbb{H}$. ∎

**Remark (where the line plus three-space splitting lives).** The splitting $\mathbb{H}=\mathbb{R}\oplus\operatorname{Im}\mathbb{H}$ is invariant under the **conjugation** action, not under the left action. Conjugation fixes $e_t$ and preserves the imaginary part, which is why the adjoint display is a three-dimensional representation with a trivial direction beside it. Left multiplication does not fix $e_t$; it sends it to $\vec e_z$ under $L_z$. The two statements are consistent: the same group acts on the same four-dimensional space in two ways, one reducible and one not.

**Theorem (isoclinic structure).** In the basis $(e_t,\vec e_k,\vec e_i,\vec e_j)$, with $(i,j,k)$ cyclic, each generator $L_k$ is block diagonal with two copies of the same $2\times2$ rotation block. Consequently every element of $SO_R(4)_{\mathrm{left}}$ rotates its two invariant planes by the same angle, and the group is one of the two isoclinic copies of $S^3$ in $SO(4)$.

*Proof.* For $L_z$ in the basis $(e_t,\vec e_z,\vec e_x,\vec e_y)$ the columns are the coordinate columns of $\vec e_ze_t=\vec e_z$, $\vec e_z\vec e_z=-e_t$, $\vec e_z\vec e_x=\vec e_y$ and $\vec e_z\vec e_y=-\vec e_x$, which give $\operatorname{diag}(R,R)$ with $R=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$. The other two are the same computation after a cyclic relabelling, and the relabelling is an automorphism of $\mathbb{H}$, so it conjugates the statement rather than changing it. For a general element, conjugating by $L(\tilde p)$ moves the axis to $\vec e_z$ and leaves $\theta$ unchanged, so the same basis gives $\operatorname{diag}(R_\theta,R_\theta)$ for the conjugate, hence equal angles in the two planes. ∎

**Remark (the spectrum reads the same fact).** The eigenvalues of $L(\tilde q)$ for $\tilde q=\cos\theta+\sin\theta\vec u$ are $e^{i\theta}$ and $e^{-i\theta}$, each with multiplicity two. A rotation of $\mathbb{R}^4$ by angles $\alpha,\beta$ in its two planes has eigenvalues $e^{\pm i\alpha},e^{\pm i\beta}$, and the two pairs coincide only when the angles agree up to sign. Equal multiplicity of the two pairs is isocliny.

**Theorem (the two copies and the double cover).** The map $(\tilde q_L,\tilde q_R)\mapsto[\tilde X\mapsto\tilde q_L\tilde X\tilde q_R^{-1}]$ is a surjection $S^3\times S^3\to SO(4)$ with kernel $\{\pm(\mathrm{I}_4,\mathrm{I}_4)\}$. The left copy $SO_R(4)_{\mathrm{left}}$ is the factor $\tilde q_R=e_t$, the right copy $SO_R(4)_{\mathrm{right}}$ is the factor $\tilde q_L=e_t$, and the two copies meet in $\{\pm\mathrm{I}_4\}$. Infinitesimally $\mathfrak{so}(4)=\mathfrak{g}_L\oplus\mathfrak{g}_R$ is a direct sum of two commuting three-dimensional ideals, each isomorphic to $\mathfrak{su}(2)$.

*Proof.* The map is a surjective homomorphism onto $SO(4)$ by the classical theorem, and its kernel is the set of pairs with $\tilde q_L\tilde X=\tilde X\tilde q_R$ for all $\tilde X$. Taking $\tilde X=e_t$ gives $\tilde q_L=\tilde q_R$, and then $\tilde q_L$ commutes with every $\tilde X$, so it is real of modulus one, hence $\pm e_t$. For the intersection, $L(\tilde q)=R(\tilde p)$ forces $\tilde q=\tilde p$ from the action on $e_t$, and then $\tilde q$ is central, so $\tilde q=\pm e_t$. The Lie algebra statement follows by differentiating and by counting dimensions, $3+3=6$. ∎

**Theorem (no preferred axis).** No nonzero element of $\mathfrak{g}_L$ is a diagonal matrix, and no element of $SO_R(4)_{\mathrm{left}}$ other than $\pm\mathrm{I}_4$ is diagonal. The three generators have one shape, and the cyclic permutation of the three axes, which is an automorphism of $\mathbb{H}$, permutes them without a sign.

*Proof.* An element of $\mathfrak{g}_L$ is real and antisymmetric, since each $L_k$ is. A real diagonal antisymmetric matrix is zero. For the group, a diagonal orthogonal matrix has diagonal entries $\pm1$. The matrix $L(\tilde q)$ for $\tilde q\neq\pm e_t$ has the nonreal eigenvalues $e^{\pm i\theta}$, so it is not diagonal, while $L(\pm e_t)=\pm\mathrm{I}_4$. The cyclic permutation sends $L_k$ to $L_{k+1}$ exactly, because it is an algebra automorphism $\varphi$ and $L(\varphi\tilde q)=L(\varphi)L(\tilde q)L(\varphi)^{-1}$ with $L(\varphi)$ the corresponding permutation matrix. ∎

**Remark (what the theorem does not say).** It does not say that the group has no axis; a group has no axes at all. It says that the display cannot mark one, because marking requires a diagonal generator and a real antisymmetric matrix cannot be diagonal. The marking in the complex display is therefore a feature of the display and not of the group, and the next theorem says what it is.

**Theorem (frame dependence of the $2\times2$ display).** A complex $2\times2$ display of $\mathrm{Rot}$ requires a complex structure on $\mathbb{H}$, that is a unit imaginary quaternion $u$, that is a point of $S^2$. For each such $u$ the right multiplication $J_u(X)=Xu$ is a complex structure, every left multiplication is complex-linear for it, and in an adapted basis the generator $L(u)$ is diagonal with entries $\pm i$, while the other two are not. Different choices give conjugate displays. The real $4\times4$ display requires no such choice.

*Proof.* $J_u^2=-\mathrm{id}$ because $u^2=-e_t$, so $J_u$ makes $\mathbb{H}$ a complex two-space. Left and right multiplications commute, $L(\tilde q)J_u(X)=\tilde qXu=J_uL(\tilde q)(X)$, so each $L(\tilde q)$ is complex-linear and has a $2\times2$ matrix. The operator $L(u)$ is complex-linear and satisfies $L(u)^2=-\mathrm{id}$, so it is diagonal in an adapted complex basis with entries $\pm i$. The other two generators do not commute with $L(u)$, since $[L_x,L_y]=2L_z\neq0$, so they cannot be simultaneously diagonal with it. For the conjugacy, right multiplication by $p\in\mathrm{Rot}$ carries $J_u$ to $J_{p^{-1}up}$, and the conjugation action of $\mathrm{Rot}$ is transitive on $S^2$. ∎

**Remark (the exact content of "frame-free").** The three generators pairwise fail to commute, so no complex display can have two diagonal generators. Every complex display therefore has at most one, and the corpus's display has exactly one, $J_z$. The axis $\vec e_z$ is not preferred by the group; it is preferred by the display, and the preference is the choice of $u=\vec e_z$. A computation that must not appear to prefer an axis can be written in the $4\times4$ real display, where the preference cannot be expressed at all.

## What Changes and What Does Not

**What does not change.** The following are properties of the group, and the display does not touch them.

- **The group.** Both displays are $\mathrm{Rot}=S^3$ up to isomorphism, and both are faithful, so both carry the sign.
- **The dimension.** Three, in both.
- **The Lie algebra, up to isomorphism.** $\mathfrak{su}(2)$, $\mathfrak{g}_L$ and $\mathfrak{so}(3)$ are one algebra in three writings.
- **The bracket type.** $2\varepsilon_{ijk}$ for the raw generators on both sides, $\varepsilon_{ijk}$ after halving, on both sides.
- **Composition.** Matrix multiplication in both, and the product of the images is the image of the product.
- **The exponential.** The ordinary matrix exponential of a three-dimensional Lie algebra in both, with the same closed form.
- **The determinant and the trace.** Determinant one for a unit element in both, and trace $2q_t$ against $4q_t$, which is the size and not a difference of structure.

**What changes.** The following are properties of the display.

- **The field.** $\mathbb{C}$ becomes $\mathbb{R}$, so every entry of the real display is a real number and no imaginary unit appears.
- **The size.** $2\times2$ becomes $4\times4$.
- **The carrier.** $\mathbb{C}^2$ becomes $\mathbb{R}^4$. Both have real dimension four, so the carrier is the same real space. What changes is that the complex structure on it is no longer part of the display.
- **The diagonal generator.** One becomes none, and *Structural Theorems* proves that this is forced.
- **The ambient algebra.** $\mathfrak{u}(2)$, of real dimension four, becomes $\mathfrak{so}(4)$, of real dimension six. The image is three-dimensional in both, so the codimension grows from one to three.
- **The reducibility of the ambient action.** The conjugation action splits as a line plus a three-space and the left action does not. The display chosen determines which of the two actions the matrix exhibits.

**The one sentence that carries the section.** Nothing about the rotor group changes. The complex structure moves from being implicit in the display to being an explicit choice, and the real display is what the group looks like when that choice is not made.

## Worked Examples

### The Quarter Turn About $\vec e_z$

**The rotor.** The quarter turn in rotor language is $\tilde q=\cos\tfrac\pi4\,e_t+\sin\tfrac\pi4\,\vec e_z=\tfrac{1}{\sqrt2}(e_t+\vec e_z)$, of rotor angle $\pi/4$, inducing a rotation of angle $\pi/2$.

**The real display.** With $\theta=\pi/2$ and $\vec u=\vec e_z$,

$$
\exp\bigl(\tfrac\pi2L_z\bigr)=\mathrm{I}_4+L_z=\begin{pmatrix}1&0&0&-1\\0&1&-1&0\\0&1&1&0\\1&0&0&1\end{pmatrix},
\qquad
L(\tilde q)=\frac{1}{\sqrt2}\begin{pmatrix}1&0&0&-1\\0&1&-1&0\\0&1&1&0\\1&0&0&1\end{pmatrix}.
$$

The matrix rotates the plane $(e_t,\vec e_z)$ and the plane $(\vec e_x,\vec e_y)$, each by $\pi/2$, and the two blocks are equal: the element is isoclinic. The half-angle roots survive in the entries, $\tfrac{1}{\sqrt2}$ in each of the eight nonzero positions, and they do not cancel. They cancel only in a two-sided product, which is a different object and not the subject of this article.

**The complex display.** In the defining display the same element is diagonal,

$$
\mathsf M_2(\tilde q)=\frac{1}{\sqrt2}\bigl(\mathrm{I}_2+J_z\bigr)=\frac{1}{\sqrt2}\begin{pmatrix}1-i&0\\0&1+i\end{pmatrix}.
$$

The two matrices are one group element in two displays. One has eight nonzero entries and no zero pattern worth the name. The other has two nonzero entries, both on the diagonal, and the diagonal position is the mark of the axis $\vec e_z$.

**What the comparison shows.** The complex display is smaller and, for this element, simpler: a diagonal unitary is the easiest matrix to read. The real display is larger and, for this element, more informative about the action, since it shows the two planes and the equality of the two angles, which the diagonal display hides behind the modulus-one entries.

### The General Rotor

**The real display.** For $\tilde q=\cos\tfrac\theta2\,e_t+\sin\tfrac\theta2\,(n_x\vec e_x+n_y\vec e_y+n_z\vec e_z)$, with $c=\cos\tfrac\theta2$ and $s=\sin\tfrac\theta2$,

$$
L(\tilde q)=
\begin{pmatrix}
c&-sn_x&-sn_y&-sn_z\\
sn_x&c&-sn_z&sn_y\\
sn_y&sn_z&c&-sn_x\\
sn_z&-sn_y&sn_x&c
\end{pmatrix}.
$$

The matrix is orthogonal of determinant one, and its trace is $4c=4\cos\tfrac\theta2$. The trace therefore reads the scalar part, which is the cosine of the half angle, and the pair $L(\tilde q)$, $L(-\tilde q)$ has traces $\pm4\cos\tfrac\theta2$. That is the sign, visible in a single number.

**The complex display.** The same element is

$$
\mathsf M_2(\tilde q)=\begin{pmatrix}c-isn_z&-isn_x-sn_y\\-isn_x+sn_y&c+isn_z\end{pmatrix},
$$

of trace $2c$ and determinant one. The two displays agree on the scalar part up to the factor of the size, and they agree on the determinant exactly.

### The Three Coordinate Quarter Turns

**One family, not three cases.** For the three axes the quarter-turn rotors are $\tfrac{1}{\sqrt2}(e_t+\vec e_k)$, and the three matrices $L(\tfrac{1}{\sqrt2}(e_t+\vec e_k))=\tfrac{1}{\sqrt2}(\mathrm{I}_4+L_k)$ are obtained from one another by the cyclic permutation of the basis. The permutation is a change of basis and not a conjugation by an element of the group. The three axes are equivalent, and the display shows the equivalence as a relabelling of coordinates with no sign.

**The complex side, the same three.** In the defining display the three are $\tfrac{1}{\sqrt2}(\mathrm{I}_2+J_k)$, and only the third is diagonal. The first two are $\tfrac{1}{\sqrt2}\begin{pmatrix}1&-i\\-i&1\end{pmatrix}$ and $\tfrac{1}{\sqrt2}\begin{pmatrix}1&-1\\1&1\end{pmatrix}$, which are as far from diagonal as the real display is. The uniformity of the real display is therefore a statement about all three at once, while the complex display has one member of the family in a special form and two in a general one.

## What Is Lost and What Is Gained

**Nothing about the group is lost.** The left regular display is faithful, so the group and its multiplication are recovered exactly. The carrier $\mathbb{R}^4$ is the carrier $\mathbb{C}^2$ read over the reals, with the complex structure forgotten. The complex structure can be put back by choosing a point of $S^2$, and any two choices give conjugate displays. The complex module is therefore recoverable and not lost.

**What is lost is the illusion.** The $2\times2$ display makes the complex structure look like part of the group, because the entries are complex and one generator is diagonal. It is not part of the group: it is a choice, and the choice is a point of $S^2$. A writer who forgets this writes that the rotor group has a preferred axis, or that the $z$-generator is the distinguished one. The $4\times4$ display cannot support the illusion, because its entries are real and no generator can be diagonal.

**What is gained.** Five things, each a theorem of *Structural Theorems* or a line of *The Left Regular Display*.

- **Real entries.** The matrices are real, so the display is available in a real computation with no complex arithmetic and no conjugate pairs to track.
- **A uniform shape.** The three generators are signed permutations of one shape, and the cyclic relabelling permutes them with no sign. A computation written in this display cannot silently privilege one direction.
- **A faithful image with a visible sign.** $L(-\tilde q)=-L(\tilde q)$, and the trace separates the two, $\pm4\cos\tfrac\theta2$. The adjoint display cannot do this.
- **An ordinary matrix exponential.** The closed form is $\cos\theta\,\mathrm{I}_4+\sin\theta\,U$ with $U^2=-\mathrm{I}_4$, and the exponential is surjective onto the group with an explicit preimage.
- **The isoclinic structure, displayed.** The two equal blocks and the doubled spectrum are visible in the matrix, which is the structural reason the group is one of the two $S^3$'s in $SO(4)$. In the complex display the same fact is present and invisible.

**What is paid.** The matrices are twice as large, and the eigenvalue $\pm i$ of a generator appears as a real rotation block only after the plane is read off. A computation that needs the eigenbasis of a generator is better served by the complex display. A computation that must not choose an axis is better served by the real one. The two displays are tools for two jobs, and neither replaces the other.

## Pitfalls and Corrections

**The nine sentences that must not be written.** Each of them was written at some point in the drafting of this material, and each is wrong for a stated reason.

1. **"The rotor group is $SU(2)$."** The rotor group is $S^3$. $SU(2)$ is its defining display, that is the image of $\mathsf M_2$. The two groups are isomorphic and the isomorphism is a choice.
2. **"$SU(2)=S^3$."** The same error in the other notation. $S^3$ is a subset of $\mathbb{H}$, $SU(2)$ is a subset of $M_2(\mathbb{C})$, and the identification is the display.
3. **"$SO_R(4)_{\mathrm{left}}$ is all of $SO(4)$."** It is the three-dimensional image, and $SO(4)$ is six-dimensional. The other three dimensions are the right regular copy, and the two copies commute.
4. **"$SO_R(4)_{\mathrm{left}}\cong\mathbb{H}$."** $\mathbb{H}$ is a four-dimensional vector space and the group is three-dimensional. The group acts on $\mathbb{H}$ and is not isomorphic to it. What is true is that the group is a subgroup of $GL(\mathbb{H})=GL(4,\mathbb{R})$.
5. **"The left action fixes the scalar line."** It does not, since $L_z$ sends $e_t$ to $\vec e_z$. The conjugation action fixes the scalar line, and the left action is irreducible precisely because it does not.
6. **"The left action splits as $\mathbf{1}\oplus\mathbf{3}$."** It is irreducible, by the left ideal argument of *Structural Theorems*. The splitting belongs to the conjugation action.
7. **"$L_{\mathrm{axf}}$ restricted to $SU(2)$."** This mixes a display of the algebra, defined on all of $\mathbb{H}$, with a subgroup that lives in a different algebra. The object is $\rho_L:\mathrm{Rot}\to SO(4)$, $\tilde q\mapsto[X\mapsto\tilde qX]$, with image $SO_R(4)_{\mathrm{left}}$.
8. **"$SOL(4)$" or "$SOR(4)$".** The names collide with successive over-relaxation and read as typographical errors. The names used here are $\mathfrak{g}_L$ and $SO_R(4)_{\mathrm{left}}$, each defined in one line.
9. **"$SO_R(4)_{\mathrm{left}}$ is unitary."** It is real orthogonal. It becomes unitary only after complexification, which is optional and outside this article.

**Three corrections to statements that circulate.** Three further sentences circulate and are false. They are not confusions of language; they are errors of fact, and both are cheap to check.

**Correction (the bracket is the same on both sides).** It is often said that the defining generators obey $[J_i,J_j]=\varepsilon_{ijk}J_k$ while the regular generators obey $[L_i,L_j]=2\varepsilon_{ijk}L_k$, and the pair is presented as a difference between the two displays. There is no such difference. Both brackets are twice the structure constants, because both displays are multiplicative and both are images of the same quaternion bracket $\vec e_x\vec e_y-\vec e_y\vec e_x=2\vec e_z$. The familiar $\varepsilon_{ijk}$ is what both become after the generators are halved, and the halving is the same operation on both sides.

**Correction (transposition does not negate one generator).** It is sometimes said that transposition changes the sign of one generator, as a way of saying that a reflection of one axis is available. It is not. The transpose of a left matrix is the left matrix of the conjugate, $L(\tilde q)^{\mathsf T}=L(\tilde q^{\natural})$, so transposition negates all three generators at once. The sign patterns produced by conjugating the triple by the eight unit quaternions are the four with an even number of minus signs: the identity and the three rotations by $\pi$. A single-axis negation never occurs, because the automorphism group of $\mathbb{H}$ is $SO(3)$ and a single reflection has determinant $-1$.

**Correction (no generator has a zero row).** It is sometimes said that each generator has a zero row and a zero column at the coordinate it fixes. Each generator has one nonzero entry in every row and every column. The fixed coordinate shows up as the cut between the two equal $2\times2$ blocks, not as a zero line.

## Verification

**How the numbers were obtained.** Every claim below was recomputed on one hundred random unit quaternions, drawn from a fixed seed, in double precision. The matrix $L(\tilde q)$ was built twice, once from the display above and once from its columns as the products $\tilde qe_\nu$, and the two agreed exactly. The exponential was computed twice, once from the closed form and once from the series to forty terms, so that the closed form is checked and not assumed. The quaternion product was taken from the multiplication table of the algebra, and no library quaternion type was used.

**The residuals.**

| claim | what was computed | largest residual |
|---|---|---|
| the display equals its columns | the display against the columns $\tilde qe_\nu$ | $0$ |
| multiplicativity | $L(\tilde q)L(\tilde p)-L(\tilde q\tilde p)$ | $2.2\cdot10^{-16}$ |
| orthogonality | $L^{\mathsf T}L-\mathrm{I}_4$ | $4.4\cdot10^{-16}$ |
| determinant one | $\det L-1$ | $6.7\cdot10^{-16}$ |
| trace | $\operatorname{tr}L-4q_t$ | $0$ |
| determinant, general element | $\det L-\lvert q\rvert^4$ | $5.7\cdot10^{-14}$ |
| the sign | $L(-\tilde q)+L(\tilde q)$ | $0$ |
| square minus one | $L_k^2+\mathrm{I}_4$ | $0$ |
| the bracket | $[L_x,L_y]-2L_z$, cyclically | $0$ |
| the exponential | $\exp(\theta L_z)-L(\cos\theta+\sin\theta\vec e_z)$ | $0$ |
| the exponential against its series | the series against $\cos\theta\,\mathrm{I}_4+\sin\theta\,U$ | $1.8\cdot10^{-15}$ |
| surjectivity of the exponential | $\exp(\theta\vec u\cdot L)-L(\tilde q)$ over the polar data | $1.2\cdot10^{-15}$ |
| the kernel | $\exp(2\pi L_z)-\mathrm{I}_4$ and $\exp(\pi L_z)+\mathrm{I}_4$ | $5.3\cdot10^{-15}$, $2.3\cdot10^{-16}$ |
| cyclic relabelling | $PL_xP^{-1}-L_y$, cyclically | $0$ |
| the quarter turn | $L(\tfrac{1}{\sqrt2}(e_t+\vec e_z))-\tfrac{1}{\sqrt2}(\mathrm{I}_4+L_z)$ | $0$ |
| the transpose | $L(\tilde q)^{\mathsf T}-L(\tilde q^{\natural})$ | $0$ |
| isocliny | the two diagonal blocks of each $L_k$, subtracted | $0$ |
| the spectrum | the eigenvalues of $L(\tilde q)$ at $\theta=0.7$ | $e^{\pm0.7i}$, each twice |
| the two copies commute | $L_kR_l-R_lL_k$ | $0$ |
| the two copies span | the rank of the six generators | $6$ |
| the two copies meet trivially | the dimension count for $\mathfrak{g}_L+\mathfrak{g}_R$ | $0$ |
| the commutant of $\mathfrak{g}_L$ | its dimension in $M_4(\mathbb{R})$ | $4$ |
| the conjugation action | against Rodrigues at the double angle | $5.6\cdot10^{-16}$ |
| the scalar line under conjugation | $\tilde qe_t\tilde q^{-1}-e_t$ | $3.3\cdot10^{-16}$ |
| the sign is invisible to conjugation | $\operatorname{Ad}(\tilde q)-\operatorname{Ad}(-\tilde q)$ | $0$ |
| the defining display | unitarity, determinant, bracket, $J_z$ diagonal | $3.3\cdot10^{-16}$, $4.4\cdot10^{-16}$, $0$, $0$ |
| the sign patterns | from the eight unit conjugations | only the four even patterns |

**What the rows about the two copies say.** The commutant of $\mathfrak{g}_L$ in $M_4(\mathbb{R})$ has dimension four, which is the right regular family: the matrices commuting with all left multiplications are exactly the right multiplications. That is the infinitesimal form of the double centralizer statement behind $\mathfrak{so}(4)=\mathfrak{g}_L\oplus\mathfrak{g}_R$, and it is the reason the left copy is a proper subgroup of $SO(4)$ and not the whole of it.

**One check that is not numerical.** The irreducibility theorem and the theorem that no generator is diagonal are exact statements about all elements, and no sample can confirm them. They are proved under *Structural Theorems*, and the numbers above confirm only the instances computed: that the three generators have zero diagonal, that the sign patterns available from the eight unit conjugations are the four even ones, and that no real antisymmetric diagonal matrix occurs among the samples.

## Summary

The rotor group is $S^3$, of real dimension three, and it has several faithful matrix displays. The defining display is the $2\times2$ complex one, $\mathsf M_2:\mathrm{Rot}\to SU(2)$. The left regular display is the $4\times4$ real one, $L:\mathrm{Rot}\to SO_R(4)_{\mathrm{left}}\subset SO(4)$, built from the multiplication alone: the $\nu$-th column of $L(\tilde q)$ is the coordinate column of $\tilde qe_\nu$.

The two displays are the same group. Both are injective, so both carry the sign, $L(-\tilde q)=-L(\tilde q)$. Both have three-dimensional Lie algebras isomorphic to $\mathfrak{su}(2)$, with the bracket $2\varepsilon_{ijk}$ on the raw generators and $\varepsilon_{ijk}$ after halving, on both sides. Both exponentials are the ordinary matrix exponential, and both collapse to $\cos\theta$ times the identity plus $\sin\theta$ times the generator, because the generator squares to minus the identity.

The differences are three, and all three are properties of the display. The field is $\mathbb{R}$ instead of $\mathbb{C}$. The matrix is $4\times4$ instead of $2\times2$. And no generator is diagonal, where the complex display has exactly one. The third difference is forced: a real diagonal antisymmetric matrix is zero, so no element of $\mathfrak{g}_L$ can be diagonal, while the $2\times2$ display has $J_z=\operatorname{diag}(-i,i)$ and therefore marks the axis $\vec e_z$. The mark is the choice of a complex structure on $\mathbb{H}$, that is a point of $S^2$. Different choices give conjugate displays, and the real display makes no choice at all.

The structural results are these. The image is one of the two isoclinic copies of $S^3$ in $SO(4)$: in the basis $(e_t,\vec e_k,\vec e_i,\vec e_j)$ each generator is two copies of one $2\times2$ rotation, the spectrum is $e^{\pm i\theta}$ with multiplicity two, and the two invariant planes turn by the same angle. The two copies commute and span, $\mathfrak{so}(4)=\mathfrak{g}_L\oplus\mathfrak{g}_R$ with $3+3=6$, and they meet in $\{\pm\mathrm{I}_4\}$. The left action on $\mathbb{R}^4$ is irreducible, and the splitting $\mathbf{1}\oplus\mathbf{3}$ belongs to the conjugation action and not to the left one. The exponential is surjective with kernel the spheres of radius $2\pi k$, and it collapses the sphere of radius $\pi$ to $-\mathrm{I}_4$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathrm{Rot}=Sp(1)=S^3$ | the rotor group, the unit quaternions |
| $\mathbb{H}$, $e_t,\vec e_x,\vec e_y,\vec e_z$ | the quaternion algebra and its real basis, with $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$ |
| $\langle\tilde q\rangle_{\natural}$, $\tilde q^{\natural}$ | the quaternion norm and the conjugation |
| $\mathsf M_2$ | the defining display, $\mathrm{Rot}\to SU(2)\subset M_2(\mathbb{C})$ |
| $J_x,J_y,J_z$ | $\mathsf M_2(\vec e_k)$, the three defining generators, with $J_z$ diagonal |
| $L(\tilde q)$ | the left regular matrix, $L(\tilde q)_{\mu\nu}=[\tilde qe_\nu]_\mu$ |
| $L_x,L_y,L_z$ | $L(\vec e_k)$, the three real generators, none diagonal |
| $\mathfrak{g}_L$ | $\operatorname{span}_{\mathbb{R}}\{L_x,L_y,L_z\}$, real dimension three |
| $SO_R(4)_{\mathrm{left}}$ | $\exp(\mathfrak{g}_L)$, the three-dimensional image in $SO(4)$ |
| $SO(4)=SO_R(4)$ | the six-dimensional ambient orthogonal group |
| $R(\tilde q)$, $\mathfrak{g}_R$ | the right regular family and its algebra, the other copy |
| $\operatorname{Ad}$ | the conjugation display $\mathrm{Rot}\to SO(3)$, of kernel $\{\pm1\}$ |
| $J_u$ | the complex structure $X\mapsto Xu$ defined by a unit imaginary $u$ |

## Further Reading

- [Quaternion Rotations and Reflections](quaternion-rotations-and-reflections.html), for the group of unit quaternions, its polar form, the double cover $Sp(1)\to SO(3)$ and the two-sided action that exhausts $SO(4)$.
- [Matrix Representations Conventions](matrix-representations-conventions.html), for the axis-free frame, the rule $L_{\mathrm{axf}}(\tilde Q)_{\mu\nu}=[\tilde Qe_\nu]_\mu$, the $2\times2$ element display and the reasons no Pauli array is written in a body section.
- [Four-Dimensional Rotations](four-dimensional-rotations.html), for the normal form of a rotation of $\mathbb{R}^4$ as a pair of planar rotations and for the angle pair that the isoclinic case degenerates.
- [Why AXF Matrices instead of Pauli and Gamma Matrices](../articles_physics/why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the general argument that an array carries a frame, a dimension and an inertia inside a symbol, of which the theorem on the preferred axis is the three-dimensional instance.
- [The Lie Correspondence and the Adjoint Representation](the-lie-correspondence-and-the-adjoint-representation.html), for the exponential map, the adjoint representation and the place of a three-dimensional subgroup inside a six-dimensional group.
- S. Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, ch. II, for the exponential map of a compact group and the isoclinic subgroups of $SO(4)$.
- I. R. Porteous, *Clifford Algebras and the Classical Groups*, ch. 16, for the two isoclinic copies of $S^3$ in $SO(4)$ and the double cover of $SO(4)$ by $S^3\times S^3$.
