# __Idempotents and the Boundary of the Polar Decomposition of Biquaternions__

## Introduction

The polar decomposition of a biquaternion is defined on the invertible elements, and its boundary is the set where the norm vanishes. The boundary is not a harmless edge. The boost parameter diverges there, the word loses its limit, and the elements that carry the limit are the rank-one elements: the **minimal idempotents**, the elements $\Pi$ with $\Pi^{2}=\Pi$, $\Pi\neq0$ and $\Pi\neq e_t$, which are the simplest zero divisors, and, in the degenerate case, the nilpotents. This article identifies the boundary, classifies its elements, and reads the polar data at it.

Three statements organise the article. First, the nonzero elements of norm zero are exactly the rank-one matrices under the matrix model, and they split into two strata: the complex multiples of the minimal idempotents, where the scalar part is nonzero, and the nilpotents, where the scalar part vanishes. Second, every minimal idempotent is $\tfrac12(e_t+\rho)$ with $\rho^{2}=e_t$ and $\rho\neq\pm e_t$, and the Hermitian ones are exactly $\tfrac12(e_t+i\vec u)$ with $\vec u$ a real unit vector; they form a sphere, the Bloch sphere of the algebra, which is also the celestial sphere of the null directions. Third, the Hermitian idempotents are the limits of the exponential word at infinite rapidity with the scale collapsing,

$$
\Pi=\lim_{\psi\to\infty}\frac{e^{i\frac{\psi}{2}\vec u}}{2\cosh\frac{\psi}{2}},
$$

and the rotor moves them to the other minimal idempotents; the two strata of the cone are the two possible limits, according to the relative orientation of the boost and the rotor.

The article treats the null cone and its two strata (§*The Null Cone and Its Two Strata*), the idempotents and their classification (§*The Idempotents*), the Hermitian idempotents and the sphere they form (§*The Hermitian Idempotents and the Sphere*), the Peirce decomposition they induce (§*The Peirce Decomposition*), the boundary of the polar word (§*The Boundary of the Polar Word*), the relation to the exponential (§*The Idempotents and the Exponential*) and the action of the group (§*The Action on the Idempotents*), with one worked example (§*Worked Example*).

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, $\vec e_x\vec e_y=\vec e_z$, and central imaginary $i$, $i^{2}=-1$; a general element is $\tilde Q=Q_te_t+\vec Q$ with $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ and complex coefficients. The conjugations are $\tilde Q^{\natural}=Q_te_t-\vec Q$, $\overline{\tilde Q}=\overline{Q_t}e_t+\overline{\vec Q}$ and $\tilde Q^{*}=\overline{\tilde Q^{\natural}}$. The norm is $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^{2}$, the polar word is $\tilde Q=r\zeta\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ of *Modulus–Unit Polar Decomposition of Biquaternions*, and the exponential form is that of *Exponential Polar Decomposition of Biquaternions*. The matrix model is $\mathsf M_2:\mathbb{B}\to M_2(\mathbb{C})$, $\mathsf M_2(e_t)=I_2$, $\mathsf M_2(\vec e_k)=-i\sigma_k$, with $\det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$ and $\operatorname{tr}\mathsf M_2(\tilde Q)=2Q_t$. Every numerical value displayed below was recomputed in double precision.

## The Null Cone and Its Two Strata

The **null cone** is the zero set of the norm,

$$
\mathcal N=\{\tilde Q\in\mathbb{B}:\langle\tilde Q\rangle_{\natural}=0\}.
$$

It is one complex equation, hence two real equations on the eight real dimensions of the algebra: a cone of real dimension six. In the matrix model it is the determinant-zero set, so its nonzero elements are exactly the rank-one matrices. These are exactly the zero divisors of the algebra, by the criterion of *Norm and Invertibility in the General Quaternionic Algebra*: a nonzero element is a zero divisor if and only if its norm vanishes.

The scalar part cuts the cone into two strata.

**Theorem (the two strata).** Let $\tilde Q\neq0$ with $\langle\tilde Q\rangle_{\natural}=0$.

1. If $Q_t\neq0$, then $\tilde Q=2Q_t\,\Pi$ with
$$
\Pi=\frac{\tilde Q}{2Q_t},
\qquad \Pi^{2}=\Pi,\qquad \Pi\neq0,\quad \Pi\neq e_t,
$$
a minimal idempotent. The scalar part of $\Pi$ is $\tfrac12$, its matrix image has trace $1$ and rank $1$, and $\tilde Q$ is a nonzero complex multiple of a minimal idempotent.
2. If $Q_t=0$, then $\tilde Q$ is a **nilpotent**, $\tilde Q^{2}=0$, with a purely vector, isotropic part: $\tilde Q=\vec Q$ and $\langle\vec Q\rangle_{\natural}=\vec Q\cdot\vec Q=0$.

**Proof.** In the matrix model, $\langle\tilde Q\rangle_{\natural}=\det\mathsf M_2(\tilde Q)$, so a nonzero null element has rank one. If $Q_t\neq0$ then the trace $2Q_t$ is nonzero, and the Cayley–Hamilton identity for a rank-one matrix gives $\mathsf M_2(\tilde Q)^{2}=\operatorname{tr}\mathsf M_2(\tilde Q)\,\mathsf M_2(\tilde Q)$, that is, $\tilde Q^{2}=2Q_t\tilde Q$; dividing by $2Q_t$ gives $\Pi^{2}=\Pi$, and $\Pi\neq0,e_t$ because $\tilde Q$ has rank one and trace $1$. The vanishing of the norm of $\Pi$ is the corollary of the classification below. If $Q_t=0$ then $\tilde Q^{2}=\vec Q^{2}=-\langle\vec Q\rangle_{\natural}e_t=0$, and the vector part is isotropic.

The two strata have different dimensions and different normal forms.

| stratum | condition | normal form | real dimension | matrix normal form |
|---|---|---|---|---|
| idempotent | $Q_t\neq0$ | $\tilde Q=2Q_t\Pi$, $\Pi^{2}=\Pi$ | $6$ | $cE_{11}$, $c\neq0$ |
| nilpotent | $Q_t=0$ | $\tilde Q=N$, $N^{2}=0$ | $4$ | $cE_{12}$, $c\neq0$ |

The idempotent stratum is open and dense in the cone; the nilpotent stratum is a closed subvariety of it, of real codimension two, and it lies in the closure of the idempotent stratum. The two strata are nevertheless disjoint, and the scalar part distinguishes them pointwise.

The scalar part is therefore the exact invariant that separates the two kinds of boundary point. This is the boundary form of the trichotomy of the exponential: a root of $-1$ lies in the interior, a nilpotent has square zero, and an idempotent is $\tfrac12(e_t+\rho)$ with $\rho$ a root of $+1$. The three values of the square are the three behaviours of the exponential, and the two behaviours that degenerate at the boundary are the two strata of the cone.

## The Idempotents

**Definition.** An **idempotent** is an element $\Pi\neq0$ with $\Pi^{2}=\Pi$. It is **minimal** when $\Pi\neq e_t$. The minimal idempotents of $\mathbb{B}$ are the rank-one projections of the matrix model.

**Theorem (the classification).** The minimal idempotents of $\mathbb{B}$ are exactly the elements

$$
\Pi=\frac{1}{2}\bigl(e_t+\rho\bigr),
\qquad \rho^{2}=e_t,\quad \rho\neq\pm e_t .
$$

**Proof.** If $\Pi^{2}=\Pi$, put $\rho=2\Pi-e_t$. Then

$$
\rho^{2}=4\Pi^{2}-4\Pi+e_t=e_t,
$$

and $\rho\neq\pm e_t$ because $\Pi\neq0,e_t$. Conversely, if $\rho^{2}=e_t$ then $\Pi=\tfrac12(e_t+\rho)$ satisfies $\Pi^{2}=\tfrac14(e_t+2\rho+\rho^{2})=\tfrac12(e_t+\rho)=\Pi$.

**Corollary (the norm is zero).** Every minimal idempotent has norm zero, and the map $\rho\mapsto\tfrac12(e_t+\rho)$ is a bijection from the roots of $e_t$ other than $\pm e_t$ onto the minimal idempotents.

**Proof.** A minimal idempotent has matrix trace $1$, so $\operatorname{Sc}\rho=0$. Write $\rho=a+ib$ with $a$ and $b$ real vectors; the root condition $\rho^{2}=e_t$ is $|b|^{2}-|a|^{2}=1$ and $a\cdot b=0$. Hence $\rho^{\natural}=-a-ib=-\rho$, and

$$
\Pi\Pi^{\natural}
=\frac14\bigl(e_t+\rho\bigr)\bigl(e_t-\rho\bigr)
=\frac14\bigl(e_t-\rho^{2}\bigr)=0 .
$$

The map $\rho\mapsto\tfrac12(e_t+\rho)$ is injective, since $\rho=2\Pi-e_t$, and it is surjective by the classification.

The two idempotents attached to one root are $\Pi_{+}=\tfrac12(e_t+\rho)$ and $\Pi_{-}=\tfrac12(e_t-\rho)$; they satisfy

$$
\Pi_{+}+\Pi_{-}=e_t,\qquad
\Pi_{+}\Pi_{-}=0,\qquad
\Pi_{\pm}^{2}=\Pi_{\pm},
$$

the relations of a pair of complementary projections. In the matrix model they are conjugate to $E_{11}$ and $E_{22}$.

**The two roots of a projection.** The element $\rho=2\Pi-e_t$ is a root of $e_t$ with zero scalar part, and $\Pi\mapsto\rho$ is a bijection onto the roots other than $\pm e_t$. Writing $\rho=a+ib$ with $a$ and $b$ real vectors, the root condition is $|b|^{2}-|a|^{2}=1$ and $a\cdot b=0$. The Hermitian idempotents are the case $a=0$, that is $\rho=iu$ with $u$ a real unit vector; there the pair $\{\Pi_{+},\Pi_{-}\}$ determines $u$ up to sign. The complex multiples of $\Pi_{\pm}$ are the idempotent stratum of the cone.

**Nontrivial idempotents are zero divisors.** The relations $\Pi_{+}\Pi_{-}=0$ exhibit the zero-divisor property directly, with both factors nonzero. The left annihilator of $\Pi_{+}$ is the left ideal $\mathbb{B}\Pi_{-}$, the second column in the matrix model; the left annihilator of $\Pi_{-}$ is $\mathbb{B}\Pi_{+}$, the first column.

## The Hermitian Idempotents and the Sphere

The minimal idempotents that are fixed by the dagger are the **Hermitian idempotents**: $\Pi^{*}=\Pi$. By the classification they are exactly those with $\rho=iu$ for a **real** unit vector $\vec u$:

$$
\Pi_{+}=\frac{1}{2}\bigl(e_t+i\vec u\bigr),
\qquad \vec u\in S^{2}.
$$

The computation of the dagger is

$$
\Pi_{+}^{*}=\frac12\bigl(e_t+(i\vec u)^{*}\bigr)
=\frac12\bigl(e_t+i\vec u\bigr)=\Pi_{+},
$$

because $(i\vec u)^{*}=i\vec u$ for a real vector: the quaternion conjugation negates the vector, and the coefficientwise conjugation negates the factor $i$, and the two signs cancel.

**Theorem (the sphere).** The map $\vec u\mapsto\tfrac12(e_t+i\vec u)$ is a diffeomorphism from $S^{2}$ onto the set of Hermitian minimal idempotents. The inverse is $\vec u=-i(2\Pi-e_t)$.

**Proof.** The map is smooth and injective, since $2\Pi-e_t=i\vec u$ recovers $\vec u$. It is surjective by the classification and the reality of $\vec u$, and its inverse is the restriction of the affine map $\Pi\mapsto-i(2\Pi-e_t)$, which is smooth. A smooth bijection with a smooth inverse is a diffeomorphism.

The Hermitian idempotents are the **pure states** of the algebra: rank-one projections, of trace one, positive semidefinite, with $\Pi^{2}=\Pi=\Pi^{*}$. The matrix image is

$$
\mathsf M_2(\Pi_{+})=\frac12\bigl(I_2+\vec u\cdot\boldsymbol\sigma\bigr),
$$

the density matrix of a spin state with Bloch vector $\vec u$. The Bloch sphere of the two-level system is therefore the set of Hermitian minimal idempotents of the biquaternion algebra; the physical interpretation is that of *The Informational Sector: States, Observables and Probability*, and the mathematics uses only the algebra.

The same sphere is the **celestial sphere**. A future-pointing null element of the anti-Hermitian half is $\tilde Q_-=ia\,e_t+\vec b$ with $a=\lvert\vec b\rvert>0$. Its matrix image is $iA$ with $A=aI_2-\vec b\cdot\boldsymbol\sigma$, of rank one and trace $2a$, so $-i\mathsf M_2(\tilde Q_-)/(2a)=A/(2a)$ is a Hermitian minimal idempotent, and

$$
\frac{-i\,\mathsf M_2(\tilde Q_-)}{2a}
=\frac{A}{2a}
=\frac12\Bigl(I_2-\frac{\vec b}{a}\cdot\boldsymbol\sigma\Bigr)
=\mathsf M_2\Bigl(\frac12\bigl(e_t+i\vec u\bigr)\Bigr),
\qquad \vec u=-\frac{\vec b}{a}.
$$

The null direction is the point $\vec u$ of the sphere, and the scale $a$ is forgotten: the celestial sphere of null directions is the set of Hermitian idempotents. The two signs of $\vec u$ correspond to the two idempotents $\Pi_{\pm}$, that is, to the two antipodal points $\pm\vec u$ of the celestial sphere. The projective statement, with the Möbius action, is in *Biquaternion Lorentzian and Conformal Geometry*.

**The conjugations.** For $\vec u$ real,

$$
\Pi_{+}^{\natural}=\Pi_{-},\qquad
\overline{\Pi_{+}}=\Pi_{-},\qquad
\Pi_{+}^{*}=\Pi_{+}.
$$

The quaternion conjugation and the coefficientwise conjugation both exchange the two idempotents of the pair; the Hermitian conjugation fixes each. On the Hermitian idempotents the two real structures $\natural$ and $\overline{\phantom{Q}}$ agree, and the dagger is the involution that selects them.

## The Peirce Decomposition

An idempotent splits the algebra into four summands. Let $\Pi$ be a minimal idempotent and $\Pi'=e_t-\Pi$ its complement. The **Peirce decomposition** is

$$
\mathbb{B}
=\Pi\mathbb{B}\Pi\ \oplus\ \Pi\mathbb{B}\Pi'\ \oplus\ \Pi'\mathbb{B}\Pi\ \oplus\ \Pi'\mathbb{B}\Pi',
$$

and each summand is a complex line. The multiplication table, with a basis $\Pi$, $N$, $\bar N$, $\Pi'$ adapted to the four summands, is

| $\cdot$ | $\Pi$ | $N$ | $\bar N$ | $\Pi'$ |
|---|---|---|---|---|
| $\Pi$ | $\Pi$ | $N$ | $0$ | $0$ |
| $N$ | $0$ | $0$ | $-\Pi$ | $N$ |
| $\bar N$ | $\bar N$ | $-\Pi'$ | $0$ | $0$ |
| $\Pi'$ | $0$ | $0$ | $\bar N$ | $\Pi'$ |

The table is the multiplication table of $M_2(\mathbb{C})$ in the basis $\Pi=E_{11}$, $\Pi'=E_{22}$, $N=-iE_{12}$, $\bar N=-iE_{21}$, the basis in which the matrix images of the algebra elements are written. The two off-diagonal summands are the nilpotent directions:

$$
N^{2}=0,\qquad \bar N^{2}=0,\qquad N\bar N=-\Pi,\qquad \bar N N=-\Pi'.
$$

**Proposition (the Peirce nilpotents).** The two off-diagonal summands are spanned by nilpotents, and every nilpotent of the stratum $Q_t=0$ is a nonzero element of one of them, for a suitable minimal idempotent.

**Proof.** The products $N^{2}=0$ and $\bar N^{2}=0$ are read from the table. Conversely, a nilpotent $N$ with $N^{2}=0$ and $N\neq0$ has rank one and trace zero in the matrix model; it is therefore conjugate to $E_{12}$, and the conjugating element carries $E_{11}$ to a minimal idempotent $\Pi$ for which $N\in\Pi\mathbb{B}\Pi'$.

The decomposition depends on the idempotent, and the group acts transitively on the idempotents, so all the Peirce decompositions are conjugate. The two complex lines $\Pi\mathbb{B}\Pi$ and $\Pi'\mathbb{B}\Pi'$ are the two projections; the two off-diagonal lines are the two nilpotent directions; the quaternion conjugation acts on each by $-1$, and for a Hermitian pair the coefficientwise conjugation exchanges them.

## The Boundary of the Polar Word

The polar word has no value on the cone, but it has a boundary behaviour, and the boundary behaviour produces exactly the two strata.

**Theorem (the boundary limits).** Let $\vec u_{\mathrm b}$ and $\vec u_{\mathrm r}$ be unit vectors, $\zeta$ a unit complex number and $R>0$, and let

$$
\tilde Q(\psi)=R\,e^{-\frac{\psi}{2}}\,\zeta\,e^{i\frac{\psi}{2}\vec u_{\mathrm b}}\,\tilde u_{\mathrm r},
\qquad \psi>0 .
$$

Then $\tilde Q(\psi)$ is invertible for every $\psi$, and

$$
\tilde Q(\psi)\longrightarrow
\frac{R\zeta}{2}\bigl(e_t+i\vec u_{\mathrm b}\bigr)\tilde u_{\mathrm r}
\qquad(\psi\to\infty),
$$

a nonzero null element of rank one. It is a complex multiple of a minimal idempotent when $\tilde u_{\mathrm r}$ does not anticommute with $\vec u_{\mathrm b}$, and it is a nilpotent exactly when $\tilde u_{\mathrm r}$ anticommutes with $\vec u_{\mathrm b}$.

**Proof.** The closed form of the boost gives

$$
e^{-\frac{\psi}{2}}e^{i\frac{\psi}{2}\vec u_{\mathrm b}}
=\frac{1+e^{-\psi}}{2}e_t+\frac{1-e^{-\psi}}{2}\,i\vec u_{\mathrm b}
\longrightarrow \frac12\bigl(e_t+i\vec u_{\mathrm b}\bigr).
$$

The norm of the limit is zero by the corollary of the classification, and its matrix image has rank one because the first factor has rank one and $\tilde u_{\mathrm r}$ is invertible. Write $\tilde u_{\mathrm r}=a\,e_t+b\,\vec u_{\mathrm b}+\tilde u_{\perp}$ with $a,b\in\mathbb{R}$ and $\tilde u_{\perp}$ a real vector orthogonal to $\vec u_{\mathrm b}$. Then $\operatorname{tr}\mathsf M_2(\tilde u_{\mathrm r})=2a$ and $\operatorname{tr}\mathsf M_2(\vec u_{\mathrm b}\tilde u_{\mathrm r})=-2b$, so

$$
\operatorname{tr}\mathsf M_2\bigl(\tilde Q(\infty)\bigr)
=R\zeta\,(a-ib).
$$

A rank-one matrix $L$ satisfies $L^{2}=(\operatorname{tr}L)L$ by Cayley–Hamilton. Hence, if $a-ib\neq0$, the limit is $(\operatorname{tr}L)\Pi$ with $\Pi=L/\operatorname{tr}L$ a minimal idempotent; if $a-ib=0$, the trace vanishes and $L^{2}=0$. Now $a-ib=0$ with real $a,b$ means $a=b=0$, that is, $\tilde u_{\mathrm r}=\tilde u_{\perp}$ orthogonal to $\vec u_{\mathrm b}$, that is, $\tilde u_{\mathrm r}$ anticommutes with $\vec u_{\mathrm b}$.

**Corollary (every boundary point is a limit).** Every nonzero element of the null cone is the limit of a family $\tilde Q(\psi)$ of the theorem, and the limit is reached with the scale collapsing as $e^{-\psi/2}$ while the boost diverges.

**Proof.** If $\tilde Q=2Q_t\Pi$ is in the idempotent stratum, let $\Pi_+=\Pi\Pi^{*}/\operatorname{tr}(\Pi\Pi^{*})$ be the Hermitian projection onto the range of $\Pi$; it is $\tfrac12(e_t+i\vec u)$ with $\vec u$ real. Choose $w\in SU(2)$ with $\Pi_+w=\lambda\Pi$ and $\lambda>0$: in a unitary basis, which preserves $SU(2)$, where $\Pi_+=\operatorname{diag}(1,0)$ and $\Pi=\begin{pmatrix}1&p\\0&0\end{pmatrix}$, the matrix $w=\lambda\begin{pmatrix}1&p\\-\bar p&1\end{pmatrix}$ with $\lambda=(1+\lvert p\rvert^{2})^{-1/2}$ is unitary of determinant one and has the required first row. Take $\vec u_{\mathrm b}=\vec u$, $\tilde u_{\mathrm r}=w$ and $R\zeta=2Q_t/\lambda$, flipping the signs of $\zeta$ and $w$ if necessary to place $\zeta$ in the branch; the limit is $2Q_t\Pi=\tilde Q$. If $\tilde Q=N$ is nilpotent, write $N=a(e_1+ie_2)$ with $e_1,e_2$ orthonormal and $e_3=e_1\times e_2$; take $\vec u_{\mathrm b}=e_3$, $\tilde u_{\mathrm r}=e_1$, $R\zeta=2a$, with the same sign adjustment.

The theorem is the precise sense in which the idempotents are the **boundary values** of the polar word: the scale has to vanish and the rapidity has to diverge, at the same rate, and the direction of the divergence, together with the rotor, selects the stratum. The boundary of the domain and the set of minimal idempotents are not the same set — the nilpotents are also on the boundary — but the idempotent stratum is the part reached when the rotor has a component in the plane spanned by $e_t$ and the boost axis, and the nilpotent stratum is reached when the rotor is orthogonal to both $e_t$ and the boost axis.

**The rate.** The word of the theorem has norm

$$
\langle\tilde Q(\psi)\rangle_{\natural}=R^{2}e^{-\psi}\zeta^{2},
$$

so the distance to the cone is exponential in the rapidity, and the modulus is $Re^{-\psi/2}$. The boundary is approached along the exponential coordinate line of the boost, with the scale line compensating: this is the coordinate picture of the statement that the boost is the non-compact factor that drives the word to the boundary, and that the scale is the factor that keeps the element finite.

## The Idempotents and the Exponential

The idempotents are not in the image of the exponential, because every value of the exponential is invertible and an idempotent is not. They are in its closure, in the following precise sense.

**Proposition (the exponential limit).** For a real unit vector $\vec u$,

$$
\Pi_{+}=\frac12\bigl(e_t+i\vec u\bigr)
=\lim_{\psi\to\infty}\frac{e^{i\frac{\psi}{2}\vec u}}{2\cosh\frac{\psi}{2}}
=\lim_{\psi\to\infty}e^{-\frac{\psi}{2}}e^{i\frac{\psi}{2}\vec u}.
$$

**Proof.** The closed form of the boost gives

$$
\frac{e^{i\frac{\psi}{2}\vec u}}{2\cosh\frac{\psi}{2}}
=\frac12\Bigl(e_t+i\tanh\frac{\psi}{2}\,\vec u\Bigr)
\longrightarrow\frac12\bigl(e_t+i\vec u\bigr).
$$



The idempotent is therefore the **direction** of an infinite boost, with the scale removed. It is the limit of the polar word with $r=e^{-\psi/2}$, $\zeta=1$, $\tilde u_{\mathrm r}=e_t$; the phase multiplies it by a complex scalar, and the rotor moves it by the unitary action.

The nilpotent stratum has its own exponential description. For $N$ with $N^{2}=0$,

$$
e^{tN}=e_t+tN
$$

for every complex $t$, a unipotent line. The line is invertible for every finite $t$ and tends to infinity with $t$; it never reaches the nilpotent $N$ itself, and it does not reach an idempotent. The two strata are therefore reached only at infinity: the idempotent by the divergence of the boost, and the nilpotent as the rescaled limit of the unipotent line, $\tilde Q=\lim_{t\to\infty}(e^{tN}-e_t)/t$.

The idempotent has no logarithm: a logarithm $\tilde L$ with $e^{\tilde L}=\Pi$ would make $\Pi$ invertible. It has no polar decomposition either, since its norm vanishes. What it has is a **normalised word**: the limit of the polar words with the scale collapsing. This is the sense in which the polar decomposition extends to the boundary as a *boundary value*, not as a value.

## The Action on the Idempotents

Let $\tilde Q$ be invertible. The sandwich of a Hermitian minimal idempotent is

$$
\Theta_{\tilde Q}(\Pi)=\tilde Q\,\Pi\,\tilde Q^{*}.
$$

It is Hermitian and positive semidefinite, of rank one, because $\Pi$ is Hermitian of rank one and the congruence preserves rank and inertia. It is therefore a **positive multiple of a Hermitian minimal idempotent**:

$$
\Theta_{\tilde Q}(\Pi)=\lambda\,\Pi_{\tilde Q},\qquad
\lambda=\operatorname{tr}\mathsf M_2\bigl(\tilde Q\Pi\tilde Q^{*}\bigr)>0,
\qquad \Pi_{\tilde Q}=\Pi_{\tilde Q}^{*}=\Pi_{\tilde Q}^{2}.
$$

The scalar $\lambda$ is the **unnormalised Born weight** of the projection $\Pi$ in the state $\tilde Q^{*}\tilde Q/\operatorname{tr}(\tilde Q\tilde Q^{*})$: the probability is $\lambda/\operatorname{tr}(\tilde Q\tilde Q^{*})$. The order $\tilde Q^{*}\tilde Q$ is the one compatible with the sandwich: $\operatorname{tr}(\tilde Q^{*}\tilde Q\Pi)=\operatorname{tr}(\tilde Q\Pi\tilde Q^{*})=\lambda$, while $\tilde Q\tilde Q^{*}$ would put the factors in the other order and give a different number for a non-Hermitian $\tilde Q$. In the geometric reading it is the scale of the image on the null direction. The projective class of $\Pi_{\tilde Q}$ is the image of the projective class of $\Pi$, so the group acts on the sphere of Hermitian idempotents.

**Theorem (the projective action).** The map $\Pi\mapsto[\Pi_{\tilde Q}]$ descends to an action of $\mathbb{B}^{\times}$ on the sphere of Hermitian minimal idempotents. The kernel is the centre $\mathbb{C}^{\times}$; the unitary subgroup acts by rotations, and the full group acts by the Möbius transformations of $\mathbb{C}P^{1}\cong S^{2}$.

**Proof.** The sandwich is multiplicative, $\Theta_{\tilde Q\tilde Q_1}=\Theta_{\tilde Q}\circ\Theta_{\tilde Q_1}$, and a central scalar $c$ multiplies $\Theta$ by $\lvert c\rvert^{2}$, so the whole centre lies in the kernel projectively. A unitary element gives $\Pi_{\tilde Q}=\tilde U\Pi\tilde U^{*}$, a conjugation, which is the rotation of the Bloch sphere by the image of $\tilde U$ in $SO(3)$. A general element is the product of a unitary and a Hermitian positive factor; the Hermitian positive factor gives the Möbius transformation of the conformal action, read on the celestial sphere in *Biquaternion Lorentzian and Conformal Geometry*.

The **stabiliser** of a single idempotent is larger than the kernel of the action on the algebra: the central circle acts trivially projectively, and the stabiliser has real dimension six in $\mathbb{B}^{\times}$ — four in the projective group — and it is the parabolic subgroup that fixes a null direction. The orbit is the sphere, of real dimension two, and the quotient of the group by the stabiliser is the sphere. This is the group-theoretic form of the boundary dictionary: the idempotents are a homogeneous space, and the polar word is the coordinate system in which its limiting directions are read.

**The Hermitian idempotents as pure states.** In the informational reading, a Hermitian minimal idempotent is a pure state, the sandwich is the update by a general element, and the positive scalar $\lambda$, normalised by $\operatorname{tr}(\tilde Q\tilde Q^{*})$, is the Born weight. The two idempotents of a pair are the two outcomes of a yes–no measurement, and the Peirce decomposition is the algebra of the two outcomes. The mathematical statements above are independent of the reading; the reading is recorded because it is the one the algebra serves.

## Worked Example

### The Idempotents of the Axis $\vec e_z$

Take $\vec u=\vec e_z$. The two idempotents are

$$
\Pi_{+}=\frac12\bigl(e_t+i\vec e_z\bigr),
\qquad
\Pi_{-}=\frac12\bigl(e_t-i\vec e_z\bigr).
$$

Their norm is zero:

$$
\langle\Pi_{+}\rangle_{\natural}
=\frac14\bigl(e_t+i\vec e_z\bigr)\bigl(e_t-i\vec e_z\bigr)
=\frac14\bigl(e_t+\vec e_z^{2}\bigr)
=\frac14\bigl(e_t-e_t\bigr)=0,
$$

and their square is themselves:

$$
\Pi_{+}^{2}
=\frac14\bigl(e_t+2i\vec e_z+i^{2}\vec e_z^{2}\bigr)
=\frac14\bigl(e_t+2i\vec e_z+e_t\bigr)
=\Pi_{+}.
$$

The two are Hermitian, complementary and orthogonal: $\Pi_{+}^{*}=\Pi_{+}$, $\Pi_{-}^{*}=\Pi_{-}$, $\Pi_{+}+\Pi_{-}=e_t$, $\Pi_{+}\Pi_{-}=0$. The matrix images are the diagonal projections

$$
\mathsf M_2(\Pi_{+})=\begin{pmatrix}1&0\\0&0\end{pmatrix}=E_{11},
\qquad
\mathsf M_2(\Pi_{-})=\begin{pmatrix}0&0\\0&1\end{pmatrix}=E_{22},
$$

of trace one and determinant zero.

### The Peirce Basis

With $\Pi=\Pi_{+}$ and $\Pi'=\Pi_{-}$, the two off-diagonal directions are

$$
N=\Pi\,\vec e_x\,\Pi'=\frac12\bigl(\vec e_x+i\vec e_y\bigr),
\qquad
\bar N=\Pi'\,\vec e_x\,\Pi=\frac12\bigl(\vec e_x-i\vec e_y\bigr).
$$

The first identity is computed directly:

$$
(e_t+i\vec e_z)\vec e_x(e_t-i\vec e_z)
=2\bigl(\vec e_x+i\vec e_y\bigr),
$$

using $\vec e_z\vec e_x=\vec e_y$ and $\vec e_x\vec e_z=-\vec e_y$. The nilpotence is also direct:

$$
N^{2}=\frac14\bigl(\vec e_x^{2}+i\vec e_x\vec e_y+i\vec e_y\vec e_x+i^{2}\vec e_y^{2}\bigr)
=\frac14\bigl(-e_t+i\vec e_z-i\vec e_z+e_t\bigr)=0.
$$

So $N$ is a nilpotent of the second stratum, and it is not a complex multiple of an idempotent: a multiple $c\Pi$ has square $c^{2}\Pi=c(c\Pi)\neq0$ for $c\neq0$.

### The Boundary Path

The polar path of the theorem, with $\vec u_{\mathrm b}=\vec e_z$, $\tilde u_{\mathrm r}=e_t$, $\zeta=1$ and $R=1$, is

$$
\tilde Q(\psi)=e^{-\frac{\psi}{2}}e^{i\frac{\psi}{2}\vec e_z}
=\frac{1+e^{-\psi}}{2}e_t+\frac{1-e^{-\psi}}{2}i\vec e_z .
$$

At $\psi=0$ it is $e_t$; at $\psi=1$ it is $0.6839\,e_t+0.3161\,i\vec e_z$; as $\psi\to\infty$ it tends to $\Pi_{+}$. Its norm is $e^{-\psi}$, so the path approaches the cone exponentially. The rotor $e_t$ commutes with $\vec e_z$, and the limit is the idempotent stratum.

With $\tilde u_{\mathrm r}=\vec e_x$, which anticommutes with $\vec e_z$, the same path gives

$$
\tilde Q(\psi)\longrightarrow\frac12\bigl(e_t+i\vec e_z\bigr)\vec e_x
=\frac12\bigl(\vec e_x+i\vec e_y\bigr)=N,
$$

the nilpotent of the Peirce basis. The two limits are the two strata of the cone, reached from the same boost line by two rotor orientations.

### The Two Strata in One Table

| element | scalar part | norm | square | stratum |
|---|---|---|---|---|
| $\Pi_{+}=\tfrac12(e_t+i\vec e_z)$ | $\tfrac12$ | $0$ | $\Pi_{+}$ | idempotent |
| $\Pi_{-}=\tfrac12(e_t-i\vec e_z)$ | $\tfrac12$ | $0$ | $\Pi_{-}$ | idempotent |
| $N=\tfrac12(\vec e_x+i\vec e_y)$ | $0$ | $0$ | $0$ | nilpotent |
| $\bar N=\tfrac12(\vec e_x-i\vec e_y)$ | $0$ | $0$ | $0$ | nilpotent |
| $2\Pi_{+}=e_t+i\vec e_z$ | $1$ | $0$ | $2(2\Pi_{+})$ | idempotent |

The table exhibits the boundary dictionary: the scalar part is nonzero exactly on the idempotent stratum, where the square is a nonzero multiple of the element, $\tilde Q^{2}=2Q_t\tilde Q$; on the nilpotent stratum the scalar part and the square both vanish. The nilpotents are the boundary of the boundary, the stratum where even the scalar part has collapsed.

## Summary

The boundary of the polar decomposition is the null cone, the set of nonzero zero divisors, of real dimension six. It splits into two strata. The **idempotent stratum** is the set of nonzero complex multiples of minimal idempotents, where the scalar part is nonzero: every such element is $2Q_t\Pi$ with $\Pi^{2}=\Pi$. The **nilpotent stratum** is the set of pure isotropic elements, where the scalar part vanishes and the square is zero. The scalar part is the invariant that separates them.

The minimal idempotents are exactly $\tfrac12(e_t+\rho)$ with $\rho^{2}=e_t$ and $\rho\neq\pm e_t$; all of them have norm zero, and all are zero divisors. The Hermitian ones are exactly $\tfrac12(e_t+i\vec u)$ with $\vec u$ a real unit vector, and they form a sphere: the Bloch sphere of the pure states and the celestial sphere of the null directions. For a Hermitian pair, the quaternion and coefficientwise conjugations exchange the two idempotents, and the dagger fixes each; for a general pair the quaternion conjugation exchanges them and the coefficientwise conjugation need not.

Each idempotent induces a Peirce decomposition into four complex lines, with the multiplication table of $M_2(\mathbb{C})$; the two off-diagonal lines are nilpotent, and every nilpotent of the cone lies in one of them for a suitable idempotent. The polar word reaches the boundary only with the rapidity divergent and the scale collapsing at the rate $e^{-\psi/2}$: the limit is $\tfrac{R\zeta}{2}(e_t+i\vec u_{\mathrm b})\tilde u_{\mathrm r}$, an idempotent multiple when the rotor does not anticommute with the boost axis and a nilpotent when it does. Every nonzero null element arises as such a limit. The idempotents are not in the image of the exponential and have no polar word, but they are its boundary values, and the sandwich of an invertible element sends the Hermitian ones to positive multiples of Hermitian idempotents, giving the projective action of the group on the sphere.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathcal N=\{\langle\tilde Q\rangle_{\natural}=0\}$ | the null cone, the boundary of the polar domain |
| $\Pi$, $\Pi'=e_t-\Pi$ | a minimal idempotent and its complement |
| $\Pi_{\tilde Q}$ | the normalised image of $\Pi$ under the sandwich, $\Theta_{\tilde Q}(\Pi)=\lambda\Pi_{\tilde Q}$ |
| $\rho=2\Pi-e_t$ | the root of $e_t$ attached to $\Pi$ |
| $\Pi_{\pm}=\tfrac12(e_t\pm i\vec u)$ | the two Hermitian idempotents of a real unit vector $\vec u$ |
| $N$, $\bar N$ | the two Peirce nilpotents, $N^{2}=\bar N^{2}=0$ |
| $\vec u_{\mathrm b}$, $\vec u_{\mathrm r}$ | the axes of the boost and of the rotor |
| $\psi$, $\theta$ | the rapidity and the angle of the word |
| $R$, $\zeta$ | the limiting scale and phase of the boundary path |
| $2Q_t$ | the trace of the boundary element, the scalar part doubled |
| $\lambda$ | the positive scalar of the sandwich of a Hermitian idempotent |
| $[\Pi]$ | the projective class of an idempotent, a point of the sphere |

## Further Reading

- [Modulus–Unit Polar Decomposition of Biquaternions](modulus-unit-polar-decomposition-of-biquaternions.html), for the four factors, the modulus–unit writing and the theorem of existence and uniqueness on the complement of the null cone.
- [Exponential Polar Decomposition of Biquaternions](exponential-polar-decomposition-of-biquaternions.html), for the four exponentials, the rapidity and the angle, and the two logarithms at the boundary.
- [Norm and Invertibility in the General Quaternionic Algebra](norm-and-invertibility-in-the-general-quaternionic-algebra.html), for the norm, the zero divisors and the rank-one criterion.
- [Hermitian and Skew-Hermitian Elements](hermitian-and-skew-hermitian-elements.html), for the split $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ and the two real forms.
- [The Unitary Group of the Biquaternion Algebra](the-unitary-group-of-the-biquaternion-algebra.html), for the unitary subgroup and its action by conjugation.
- [Biquaternion Lorentzian and Conformal Geometry](biquaternion-lorentzian-and-conformal-geometry.html), for the celestial sphere, the null directions and the Möbius action.
- [The Informational Sector: States, Observables and Probability](../articles_physics/the-informational-sector-states-observables-and-probability.html), for the pure states, the Born weight and the density-matrix reading.
- [The Polar Decomposition and Remarkable Subspaces](the-polar-decomposition-and-remarkable-subspaces.html), for the domain read on the six subspaces.
- [The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions](the-cartan-hermitian-pairing-of-the-polar-decomposition-of-biquaternions.html), for the positive cone and the unitary factor whose limits are the two strata.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the root convention and the matrix model.
