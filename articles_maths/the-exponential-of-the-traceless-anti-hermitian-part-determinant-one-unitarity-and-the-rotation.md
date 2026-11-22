# __The Exponential of the Traceless Anti-Hermitian Part: Determinant One, Unitarity and the Rotation__

## Introduction

**The traceless condition on a generator makes the determinant of its exponential one, the anti-Hermitian condition makes that exponential unitary, and the two conditions together single out the three-dimensional algebra $\mathfrak{su}(2)$. The exponential of that algebra is the group $\mathrm{SU}(2)$, the unit quaternions, whose elements are the rotors; a rotor acts on three-space as a rotation, two rotors to each rotation.**

The article treats the two conditions one at a time, proves what each one carries into the group, computes their intersection with its dimension, and states what neither condition gives alone. It then derives the closed form of the exponential on the intersection, writes the generator in the Pauli coordinates, reads the result in the biquaternion algebra, and identifies the rotation as the conjugation action of the group on the traceless Hermitian matrices. It assumes the determinant identity $\det e^{X}=e^{\operatorname{tr}X}$ of *The Exponential of a $2\times2$ Matrix and Its Image*, the split $M_2(\mathbb{C})=\operatorname{Herm}_2\oplus\mathfrak{u}(2)$ of *The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian at $n=2$*, and the Pauli coordinates of *$M_2(\mathbb{C})$ Pauli Representation*. The real antisymmetric case is *The Exponential of $\operatorname{Skew}_2$: the Single Rotation Plane*, and the two signs of the rotor are *The Rotor as a Square Root of a Rotation: the Two Signs and the Double Cover*.

## The Two Conditions Separately

### The Trace and the Determinant

**Proposition.** If $\operatorname{tr}X=0$ then $\det e^{X}=1$.

**Proof.** The identity $\det e^{X}=e^{\operatorname{tr}X}$ gives $\det e^{X}=e^{0}=1$.

**Corollary.** The exponential carries the traceless part into $\mathrm{SL}_2(\mathbb{C})$, and every element of $\mathrm{SL}_2(\mathbb{C})$ is the exponential of a traceless matrix.

**Proof.** The first statement repeats the proposition. The second is the theorem that the exponential of the traceless part is the special linear group, proved in *The Exponential and the Lie Group Structure*, §*The Case $n=2$*, where the Peirce coordinates of $e^{X}$ satisfy $\alpha_+\alpha_-=1$.

**Remark (the exact condition).** The determinant of $e^{X}$ is one exactly when the trace lies in $2\pi i\mathbb{Z}$. Among the preimages of the determinant one the traceless matrices form a linear subspace of complex dimension three: they are the derived algebra $[\mathfrak{gl}_2,\mathfrak{gl}_2]$, and they are the kernel of the trace.

**Remark (the trace is not a length).** The trace is additive, complex-valued and invariant under conjugation, so it measures no length and no angle. What it controls is the one multiplicative invariant of the group, the determinant.

### The Conjugate Transpose and Unitarity

**Proposition.** If $X^{*}=-X$ then $e^{X}$ is unitary.

**Proof.** Conjugation commutes with the exponential, since it is an anti-automorphism of order two and the series has real coefficients: $(e^{X})^{*}=e^{X^{*}}$. With $X^{*}=-X$ this reads $(e^{X})^{*}=e^{-X}$. The matrices $X$ and $-X$ commute, so $e^{X}e^{-X}=e^{0}=I$, and the two displays give $(e^{X})^{*}=(e^{X})^{-1}$.

**Remark (the condition on the generator is sufficient and not necessary).** The exponential is not injective, so a unitary exponential need not have an anti-Hermitian generator. The idempotent $P=\begin{pmatrix}1&1\\0&0\end{pmatrix}$ has eigenvalues $1$ and $0$, so $X=2\pi iP$ satisfies $e^{X}=I+(e^{2\pi i}-1)P=I$, while $X^{*}$ and $-X$ differ in the upper right corner. The defect is the period lattice and nothing else.

**Corollary (nothing is lost by the choice).** The anti-Hermitian part maps onto the unitary group.

**Proof.** A unitary matrix is normal, so $U=V\operatorname{diag}(e^{i\theta_1},e^{i\theta_2})V^{*}$ with $V$ unitary and the arguments taken in $(-\pi,\pi]$. The matrix $L=V\operatorname{diag}(i\theta_1,i\theta_2)V^{*}$ is anti-Hermitian and $e^{L}=U$.

### The Intersection of the Two Conditions

**Theorem.** The traceless anti-Hermitian matrices are the intersection

$$
\mathfrak{su}(2)=\mathfrak{u}(2)\cap\mathfrak{sl}_2(\mathbb{C}),
$$

taken in the real vector space $M_2(\mathbb{C})$, and the intersection has real dimension three.

**Proof.** An anti-Hermitian matrix is $A=ibI+i\sum_{k=1}^{3}a_k\sigma_k$ with $b,a_1,a_2,a_3$ real, because $iA$ is Hermitian and a Hermitian matrix of order two is $cI+\vec v\cdot\vec\sigma$ with $c$ and $\vec v$ real. The trace is $2ib$, so $A$ is traceless exactly when $b=0$. The remaining three generators $i\sigma_1,i\sigma_2,i\sigma_3$ are traceless and anti-Hermitian, and they are linearly independent over $\mathbb{R}$.

**Corollary.** The sum $\mathfrak{u}(2)+\mathfrak{sl}_2(\mathbb{C})$ is the set of matrices whose trace is purely imaginary, of real dimension seven.

**Proof.** Write $X=\tfrac12(\operatorname{tr}X)I+\bigl(X-\tfrac12(\operatorname{tr}X)I\bigr)$. The second summand is traceless, hence in $\mathfrak{sl}_2(\mathbb{C})$. The first is $\lambda I$ with $\lambda=\tfrac12\operatorname{tr}X$, and it lies in $\mathbb{R}iI$, which is contained in $\mathfrak{u}(2)$, exactly when $\lambda$ is purely imaginary. Conversely a sum of an anti-Hermitian and a traceless matrix has purely imaginary trace. The dimension is that of one real linear condition in the eight real dimensions of the algebra: $4+6-3=7$.

**Remark (the trace measures the centre and nothing else).** On $\mathfrak{u}(2)$ the trace is twice the coefficient of $iI$, since $\operatorname{tr}(ibI+i\sum_k a_k\sigma_k)=2ib$. So the traceless condition removes exactly one direction from $\mathfrak{u}(2)$, the central line $\mathbb{R}iI$, and it removes nothing else. This is the precise sense in which the trace controls the determinant: the exponential of $iI$ is the scalar $e^{ib}I$, of determinant $e^{2ib}$, and it is the only direction of $\mathfrak{u}(2)$ that moves the determinant.

### Neither Condition Alone

The two conditions look independent, so their intersection could be anything. The dimension count answers this: the intersection removes one line from a four-dimensional algebra, and the missing piece is the phase. The table separates the three cases, and each row names the one thing its condition fails to give.

The three algebras are the traceless matrices $\mathfrak{sl}_2(\mathbb{C})$ of real dimension six, the anti-Hermitian matrices $\mathfrak{u}(2)$ of real dimension four, and their intersection $\mathfrak{su}(2)$ of real dimension three.

| generator | exponential | determinant | failure |
|---|---|---|---|
| traceless | $\mathrm{SL}_2(\mathbb{C})$ | one | not unitary: $e^{\operatorname{diag}(t,-t)}=\operatorname{diag}(e^{t},e^{-t})$ is Hermitian positive and is unitary only for $t=0$ |
| anti-Hermitian | $\mathrm{U}(2)$ | $e^{2ib}$ on $ibI$ | not of determinant one: $e^{ibI}=e^{ib}I$ |
| both | $\mathrm{SU}(2)$ | one | none: unitary and of determinant one |

**Remark (the two failures are of different kinds).** The failure of the traceless condition is a scaling, and it is unbounded: the matrix $\operatorname{diag}(e^{t},e^{-t})$ has determinant one and stretches one direction while shrinking the other. The failure of the anti-Hermitian condition is a phase, and it is bounded: the determinant of a unitary matrix is a unit complex number, so the defect is one circle. The traceless condition removes that circle, and what remains is compact.

**Remark (on real elements the two conditions coincide).** For a matrix of $M_2(\mathbb{R})$, $\operatorname{tr}A$ is real, and $A^{*}=-A$ gives $\operatorname{tr}A=-\operatorname{tr}A$, hence $\operatorname{tr}A=0$. So on the real matrices the anti-Hermitian condition already implies the traceless one, and the two conditions are genuinely two only over $\mathbb{C}$. The extra circle of the previous remark is the imaginary scalar direction of the biquaternion algebra, and it is that direction which the trace condition kills.

## The Exponential of the Intersection

### The Square of a Generator

**Lemma.** A traceless matrix of order two satisfies $A^{2}=-\det(A)I$.

**Proof.** Cayley–Hamilton at order two reads $A^{2}-(\operatorname{tr}A)A+\det(A)I=0$, and the middle term vanishes. This is the traceless square $N^{2}=-\det(N)I$ of *The Element: Rank, Trace, Determinant, Characteristic Polynomial at $n=2$*.

**Corollary.** For $A\in\mathfrak{su}(2)$ nonzero one has $A^{2}=-r^{2}I$ with $r^{2}=\det A>0$.

**Proof.** The eigenvalues of $A$ are purely imaginary, $i\rho$ and $-i\rho$ with $\rho$ real and nonzero, by the spectral theorem for the anti-Hermitian case, so the determinant is $\rho^{2}$. The determinant is also $-\tfrac12\operatorname{tr}(A^{2})$, so its positivity is the negative definiteness of the trace form on $\mathfrak{su}(2)$.

### The Closed Form

**Theorem.** Let $A\in\mathfrak{su}(2)$ with $r=\sqrt{\det A}$. Then

$$
e^{A}=\cos r\,I+\frac{\sin r}{r}\,A,
$$

and at $r=0$ the right side is read as $I$.

**Proof.** By the corollary $A^{2}=-r^{2}I$, so $A^{2k}=(-1)^{k}r^{2k}I$ and $A^{2k+1}=(-1)^{k}r^{2k}A$. The series splits into the even and the odd parts, and the two are the cosine and the sine series in $r$.

**Corollary.** The exponential of $A$ is unitary with determinant one, its eigenvalues are $e^{ir}$ and $e^{-ir}$, and its values depend on $A$ only through $r$ and the unit direction $A/r$.

**Proof.** The coefficients are real, and $\hat A=A/r$ is anti-Hermitian with $\hat A^{2}=-I$, so $(e^{A})^{*}=\cos r\,I-\sin r\,\hat A$ and

$$
(e^{A})^{*}e^{A}=\cos^{2}r\,I-\sin^{2}r\,\hat A^{2}=I.
$$

The determinant is $e^{\operatorname{tr}A}=1$. The eigenvalues follow from the trace $2\cos r$ and the determinant one, or from the spectral theorem; they depend on $A$ only through $r$ and $\hat A$.

**Remark (the period).** The closed form shows $e^{(r+2\pi)\hat A}=e^{r\hat A}$ for every unit $\hat A$ of the algebra, so the exponential is not injective on $\mathfrak{su}(2)$ and its kernel contains $2\pi\hat A$ for every unit $\hat A$. The differential is singular exactly at $r\in\pi\mathbb{Z}\setminus\{0\}$, and those generators exponentiate to the two points $\pm I$ of the group.

### The Image Is $\mathrm{SU}(2)$

**Theorem.** The exponential maps $\mathfrak{su}(2)$ onto $\mathrm{SU}(2)$.

**Proof.** The image is contained in $\mathrm{SU}(2)$ by the two propositions of the first part. For the converse, $U$ is normal, so by the common spectral theorem it is $V\operatorname{diag}(\lambda,\lambda^{-1})V^{*}$ with $V$ unitary and $|\lambda|=1$. Write $\lambda=e^{i\theta}$. Then $U=\cos\theta\,I+\sin\theta\,\hat A$ where $\hat A=iV\sigma_3V^{*}$. The matrix $V\sigma_3V^{*}$ is Hermitian, traceless and of square $I$, so $\hat A$ is anti-Hermitian, traceless and of square $-I$: it lies in $\mathfrak{su}(2)$. The closed form gives $U=e^{\theta\hat A}$.

**Corollary.** The exponential restricted to the open ball of radius $\pi$ in $\mathfrak{su}(2)$ is a bijection onto $\mathrm{SU}(2)\setminus\{-I\}$.

**Proof.** The closed form gives injectivity for $r<\pi$, since the angle $\theta$ is then read in $(-\pi,\pi)$ from $\cos$ and $\sin$; and the value $-I$ is attained exactly at $r=\pi$ on each ray.

**Remark (the check).** The computation confirms the three statements in the $2\times2$ case on one hundred random elements of $\mathfrak{su}(2)$: the generator is anti-Hermitian and traceless, its square is $-r^{2}I$, and its exponential is unitary of determinant one with the closed form, to $10^{-12}$.

### The Pauli Coordinates of a Generator

**Definition.** With $\sigma_1,\sigma_2,\sigma_3$ the Pauli matrices and $a_1,a_2,a_3$ real, a generator of the intersection is

$$
A=i(a_1\sigma_1+a_2\sigma_2+a_3\sigma_3)
=\begin{pmatrix}ia_3 & a_2+ia_1\\ -a_2+ia_1 & -ia_3\end{pmatrix}.
$$

The conjugate transpose is $-A$, the trace is zero, the square is $-r^{2}I$ with $r^{2}=a_1^{2}+a_2^{2}+a_3^{2}$, and the determinant is $r^{2}$.

The three generators $A_k=i\sigma_k$ obey, with $\varepsilon_{abc}$ the alternating symbol,

| bracket | value |
|---|---|
| $[A_1,A_2]$ | $-2A_3$ |
| $[A_2,A_3]$ | $-2A_1$ |
| $[A_3,A_1]$ | $-2A_2$ |

so $[A_a,A_b]=-2\varepsilon_{abc}A_c$ and the structure constants are real numbers. The sign belongs to this normalisation of the generators: with the physicists' $J_k=\tfrac12\sigma_k$ the bracket is $[J_a,J_b]=i\varepsilon_{abc}J_c$, and $A_k=2iJ_k$ multiplies the bracket by $(2i)^{2}=-4$, which restores $-2\varepsilon_{abc}$. The algebra is closed under the bracket, and it is the compact real form of $\mathfrak{sl}_2(\mathbb{C})$.

**Remark (the reading of the corner entries).** The imaginary unit of the upper right corner belongs to the coefficient of $\sigma_1$, since $i\sigma_1=\begin{pmatrix}0&i\\i&0\end{pmatrix}$ carries $i$ in both off-diagonal slots while $i\sigma_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ is real there. An entry written $u+iv$ with $u,v$ real in the upper right corner is therefore read as $a_2=u$ and $a_1=v$. A display that puts $\theta_x+i\theta_y$ in that corner has the coefficient of $\sigma_2$ equal to $\theta_x$ and the coefficient of $\sigma_1$ equal to $\theta_y$, not the other way round; the same display with the two labels exchanged is unchanged in every other respect.

**Remark (the angle is the norm).** The radius $r$ of the closed form is the square root of the determinant, which is the Euclidean norm of the coefficient vector $(a_1,a_2,a_3)$. So the exponential of the generator of norm $r$ is the rotor of half-angle $r$, and that rotor acts as the rotation of angle $2r$ about the axis of its coefficients. The three coefficients are the axis of the rotation scaled by half its angle.

### The Biquaternion Reading

**Proposition.** Under the Pauli representation $\mathsf M_2(\tilde Q)=Q_tI-i\sum_k q_k\sigma_k$ one has $\operatorname{tr}\mathsf M_2(\tilde Q)=2Q_t$ and $\det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$, and the traceless anti-Hermitian matrices are exactly the images of the elements with $Q_t=0$ and $\vec q$ real.

**Proof.** The trace is $2Q_t$ by *$M_2(\mathbb{C})$ Pauli Representation*, §*The Trace*, and the determinant is the norm by §*The Determinant*. With $Q_t=0$ the matrix is $-i\sum_k q_k\sigma_k$, which is anti-Hermitian and traceless by the display of the previous section with $a_k=-q_k$. The minus sign in the definition of the representation is the corpus convention; it is what makes the images of the basis vectors $-i\sigma_k$, and it is the reason the identification of the coefficients is $a_k=-q_k$ and not $a_k=q_k$.

**Corollary.** The vector subspace of the biquaternion algebra, with real coefficients, is a Lie algebra isomorphic to $\mathfrak{su}(2)$ under the commutator, and the exponential of the image of that subspace is the set of unit quaternions.

**Proof.** The map is real linear and injective on the four real coordinates, and it carries the commutator to the commutator because it is a representation of the algebra. The image of the pure vector part is the intersection, and the exponential of the intersection is $\mathrm{SU}(2)$, which is the unit-norm part of the norm-one group: $\mathrm{U}(2)\cap\mathrm{SL}_2(\mathbb{C})=S^{3}$, by *Biquaternion Lie Group and Exponential Structure*, §*The $*$-Unitary Subgroup and the Defining Module*.

**Remark (the two conditions in the coordinates).** In the biquaternion coordinates the traceless condition is the vanishing of the scalar coefficient $Q_t$. The anti-Hermitian condition is that $Q_t$ is purely imaginary and that the three vector coefficients $q_x,q_y,q_z$ are real. The two together say that the scalar coefficient vanishes and the vector coefficients are real, which is the pure real quaternion. So the traceless condition removes exactly the circle of imaginary scalar coefficients from the anti-Hermitian set. The determinant of the generator is then the quaternion norm $\langle\tilde Q\rangle_{\natural}=q_x^{2}+q_y^{2}+q_z^{2}$, so the closed form reads

$$
e^{\mathsf M_2(\tilde q)}=\cos|\vec q|\,I+\frac{\sin|\vec q|}{|\vec q|}\,\mathsf M_2(\tilde q),
$$

which is the quaternion exponential $\cos\theta+\sin\theta\,\vec u$ written in matrices. The phase direction that the trace condition removes is the direction of imaginary scalar part $Q_t\in i\mathbb{R}$.

## The Rotation

### The Rotor and the Rotation Are Different Objects

**Remark (the exponential is a rotor, not a rotation).** The exponential of the traceless anti-Hermitian part lands in $\mathrm{SU}(2)$, whose elements are the rotors: unitary matrices of order two. A rotor is not a rotation matrix, and it is not an element of $\mathrm{SO}(3)$, which is a group of matrices of order three. A rotation is what a rotor does. The rotor acts on the three-dimensional real space of traceless Hermitian matrices by the sandwich $X\mapsto UXU^{*}$, and read in the basis $\sigma_1,\sigma_2,\sigma_3$ that action is a matrix of $\mathrm{SO}(3)$. The rotation is that matrix, not the rotor.

**Remark (why the two names are so easily confused).** In the real case of order two the rotors and the rotations are the same group, the circle $\mathrm{SO}(2)$, so the rotor is itself a rotation matrix; but it is the rotation of half the angle it represents, since it acts on the plane by multiplication $v\mapsto qv$ and the rotation is $q^{2}$. In every other case the two objects live in different spaces: the rotors in $\mathrm{SU}(2)$, of matrices of order two and of real dimension three, the rotations in $\mathrm{SO}(3)$, of matrices of order three and of the same real dimension three, joined by the covering of degree two.

### The Conjugation Action

**Proposition.** For $U\in\mathrm{SU}(2)$ and $X$ traceless Hermitian the matrix $UXU^{*}$ is traceless Hermitian, and $\det(UXU^{*})=\det X$.

**Proof.** $(UXU^{*})^{*}=UX^{*}U^{*}=UXU^{*}$ and $\operatorname{tr}(UXU^{*})=\operatorname{tr}(XU^{*}U)=\operatorname{tr}X$; the determinant is multiplicative and $\det U^{*}=(\det U)^{-1}=1$.

**Corollary.** The conjugation action of $\mathrm{SU}(2)$ preserves the form $X\mapsto-\det X$, which is positive definite on the three-dimensional real space of traceless Hermitian matrices.

**Proof.** A traceless Hermitian matrix is $X=r\,\vec n\cdot\vec\sigma$ with $r^{2}=-\det X$, by the Hermitian spectral theorem, so on this subspace the form is the square of the Euclidean norm of the coefficient vector, and it is positive definite there. It is not definite on the full Hermitian space, where $-\det I=-1$. The proposition says that the action preserves it.

**Theorem.** The homomorphism $\mathrm{SU}(2)\to\mathrm{SO}(3)$ given by the conjugation action on the traceless Hermitian matrices is surjective with kernel $\{\pm I\}$.

**Proof.** Every element of $\mathrm{SO}(3)$ is a rotation, and the closed form gives the action of a generator of norm $r$ as the rotation of angle $2r$ about the axis of its coefficients, by the computation of *The Rotor as a Square Root of a Rotation: the Two Signs and the Double Cover*, §*The Same Signs in $\mathrm{SU}(2)$*, so every angle and every axis occur. For the kernel, a matrix that commutes with the three matrices $\sigma_1,\sigma_2,\sigma_3$ commutes with a basis of $M_2(\mathbb{C})$ and is therefore scalar; a scalar unitary matrix of determinant one is $\pm I$. Both signs act trivially, since $(-U)X(-U)^{*}=UXU^{*}$.

**Corollary.** The rotors are the exponential of the traceless anti-Hermitian part, and the rotations of three-space are their conjugation action. The generator is defined only up to the periods of the exponential: the generators $\theta\hat A$ and $(\theta+\pi)\hat A$ give the two rotors of opposite sign and the same rotation.

**Proof.** The two statements are the theorem and the closed form read together. The rotation angle is twice the radius of the generator, so a generator of radius $\pi$ gives the identity rotation with the rotor $-I$, and the full circle $[0,2\pi)$ of the generator covers the rotation group twice.

**Remark (the check).** The computation confirms in the $2\times2$ case that the conjugation action preserves the trace, the Hermiticity and the determinant on one hundred random traceless Hermitian matrices, and that $U$ and $-U$ give the same image.

## The Pattern at General Order

**Proposition.** At every order $n$ the traceless anti-Hermitian matrices are $\mathfrak{su}(n)=\mathfrak{u}(n)\cap\mathfrak{sl}_n(\mathbb{C})$, of real dimension $n^{2}-1$, and their exponential is $\mathrm{SU}(n)$.

**Proof.** The two inclusions are the definitions; the trace of an anti-Hermitian matrix is purely imaginary, so the traceless part of $\mathfrak{u}(n)$ is the anti-Hermitian part of $\mathfrak{sl}_n$. The sum has real dimension $2n^{2}-1$, since its elements are the matrices with purely imaginary trace, so the intersection has dimension $n^{2}+2(n^{2}-1)-(2n^{2}-1)=n^{2}-1$. The surjectivity is the general statement that a unitary matrix has an anti-Hermitian logarithm which can be chosen traceless when the determinant is one.

**Remark (what the base case adds).** At $n=2$ the intersection is three-dimensional and the algebra is $\mathfrak{su}(2)$, so the group is the unit quaternions and the conjugation action is the rotation group of three-space. At $n=3$ the same two conditions give $\mathfrak{su}(3)$ and $\mathrm{SU}(3)$, as recorded in *The Exponential and the Lie Group of $M_3(\mathbb{C})$*, where the traceless anti-Hermitian case is stated with the group $\mathrm{SU}(3)$. The rotation reading does not carry over: on the traceless Hermitian matrices of order three the determinant is a cubic form and is no longer positive definite, so the preserved quantity of this article has no analogue there.

## Summary

The trace of a generator enters the group through $\det e^{X}=e^{\operatorname{tr}X}$, and the conjugate transpose enters through $(e^{X})^{*}=e^{X^{*}}$. So a traceless generator gives a determinant of one, an anti-Hermitian generator gives a unitary exponential, and the intersection of the two conditions is the three-dimensional algebra $\mathfrak{su}(2)$. The traceless condition removes exactly one line from the anti-Hermitian part, the central line $\mathbb{R}iI$ whose exponential is the scalar phase.

On the intersection the square of a generator is $-r^{2}I$, the exponential is $\cos r\,I+\frac{\sin r}{r}A$, and the image is exactly $\mathrm{SU}(2)$; the map is not injective, and it is a bijection from the open ball of radius $\pi$ onto the group minus $-I$. In the Pauli coordinates the coefficients are real, the structure constants are $-2\varepsilon_{abc}$, and the radius is the Euclidean norm of the coefficient vector. In the biquaternion algebra the traceless anti-Hermitian matrices are the images of the pure real quaternions, and the exponential there is the quaternion exponential of a vector.

The rotation is the conjugation action of $\mathrm{SU}(2)$ on the traceless Hermitian matrices, which preserves the form $X\mapsto-\det X$, positive definite on that space, is surjective onto $\mathrm{SO}(3)$ with kernel $\{\pm I\}$, and turns the generator of radius $r$ into the rotation of angle $2r$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathfrak{u}(2)$ | the anti-Hermitian matrices, real dimension four |
| $\mathfrak{su}(2)$ | the traceless anti-Hermitian matrices, real dimension three |
| $\mathfrak{sl}_2(\mathbb{C})$ | the traceless complex matrices, real dimension six |
| $\sigma_1,\sigma_2,\sigma_3$ | the Pauli matrices |
| $A_k=i\sigma_k$ | the three generators of the intersection |
| $r$ | $\sqrt{\det A}$ for $A\in\mathfrak{su}(2)$, the norm of the coefficient vector |
| $\hat A$ | $A/r$, the unit direction of the generator |
| $\mathsf M_2(\tilde Q)$ | the $2\times2$ matrix of the biquaternion $\tilde Q$ |
| $\langle\tilde Q\rangle_{\natural}$ | the biquaternion norm, equal to $\det\mathsf M_2(\tilde Q)$ |
| $S^{3}$ | the unit quaternions, equal to $\mathrm{U}(2)\cap\mathrm{SL}_2(\mathbb{C})$ |

## Further Reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for the exponential map, the compact real forms and the determinant identity.
- Roger A. Horn and Charles R. Johnson, *Topics in Matrix Analysis* (Cambridge University Press, 1991), for the matrix exponential, the closed form on a matrix with $A^{2}=-r^{2}I$ and the determinant formula.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the double cover $\mathrm{SU}(2)\to\mathrm{SO}(3)$ treated with quaternions.
- [The Exponential of a $2\times2$ Matrix and Its Image](the-exponential-of-a-2x2-matrix-and-its-image.html), for the determinant formula and the behaviour on the two halves.
- [The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian at $n=2$](the-two-halves-over-c-hermitian-and-anti-hermitian-at-n-2.html), for the split and the decomposition $\mathfrak{u}(2)=\mathbb{R}iI\oplus\mathfrak{su}(2)$.
- [The Spectral Theorem: the Anti-Hermitian Case and the Two Imaginary Eigenvalues](the-spectral-theorem-the-anti-hermitian-case-and-the-two-imaginary-eigenvalues.html), for the Pauli coordinates and the traceless part.
- [$M_2(\mathbb{C})$ Pauli Representation](m2c-pauli-representation.html), for the trace, the determinant and the vector subspace in the biquaternion coordinates.
- [The Rotor as a Square Root of a Rotation: the Two Signs and the Double Cover](the-rotor-as-a-square-root-of-a-rotation-the-two-signs-and-the-double-cover.html), for the two signs, the double cover and the computation of the rotation angle.
- [The Exponential and the Lie Group Structure](the-exponential-and-the-lie-group-structure.html), for the exponential of the traceless part onto $\mathrm{SL}_2(\mathbb{C})$ and the statements at every order.
- [Biquaternion Lie Group and Exponential Structure](biquaternion-lie-group-and-exponential-structure.html), for $\mathrm{U}(2)\cap\mathrm{SL}_2(\mathbb{C})=S^{3}$ and the quaternion exponential.
- [The Exponential and the Lie Group of $M_3(\mathbb{C})$](the-exponential-and-the-lie-group-of-m3c.html), for the case $n=3$.
