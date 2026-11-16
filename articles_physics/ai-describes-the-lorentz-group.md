# __AI describes the Lorentz Group__

## Introduction

This article states the Lorentz group the way a course in relativity states it, and only then asks why the biquaternion algebra should have anything to do with it. The order matters. The group is not a construction of the biquaternion framework and it is not discovered there; it is a group of linear maps of four-dimensional spacetime, defined by one equation, classified by its own theorems, and measured in experiments that were done before the algebra was applied to it. What the algebra supplies is a second description of the same object, and the second description is worth having only because it turns several of the standard theorems into a single multiplicative fact.

So the article has two halves. The first half is the standard account, with no biquaternions in it: the interval and the equation that preserves it, the four components of the group and the subgroup of physical observers, the six parameters and the two families, the failure of boosts to compose, the Lie algebra and its invariants, the complexification and the two labels, the double cover, the representations, and the orbits that carry mass and spin. The second half asks a narrow question — what would an algebra have to satisfy for its own multiplicative structure to reproduce every one of those statements — and answers it, showing what the biquaternion algebra does, what it explains rather than restates, and what it does not add.

## Part One: The Group as Relativity Defines It

### The interval and the one equation

Spacetime is $\mathbb{R}^4$ with the Minkowski form. Write a point as $x^\mu=(x^0,\mathbf{x})$ with $x^0=ct$, and set

$$
\eta=\operatorname{diag}(1,-1,-1,-1),\qquad
s^2(x)=x^{\mathsf T}\eta\,x=(x^0)^2-\lvert\mathbf{x}\rvert^2 .
$$

The form is not positive definite. Its zero set is the light cone through the origin, and the sign of $s^2$ sorts the other events into those a signal can reach and those it cannot. This sorting is the whole of the causal structure of flat spacetime, and it is carried by one quadratic form.

**The Lorentz group is the set of linear maps that preserve that form.** Concretely,

$$
\Lambda\in\mathrm{O}(1,3)
\iff
\Lambda^{\mathsf T}\eta\,\Lambda=\eta .
$$

Nothing else is imposed. The equation says that $s^2(\Lambda x)=s^2(x)$ for every $x$, so the group is exactly the linear maps that leave every interval alone, and hence leave the light cone, the causal order and the speed of light alone. It is the largest such group, because a quadratic form is determined by its values: a linear map preserving all intervals satisfies the equation by polarisation.

**It has six parameters.** Counting is immediate. $\Lambda$ has sixteen entries and the matrix equation is a symmetric $4\times4$ condition, which is ten independent equations, so $6=16-10$ parameters remain. The same six appear from the infinitesimal form. Write $\Lambda=I+\omega$ and keep first order:

$$
\omega^{\mathsf T}\eta+\eta\,\omega=0
\iff
\omega_{\mu\nu}=-\omega_{\nu\mu},\qquad \omega_{\mu\nu}=\eta_{\mu\rho}\,\omega^{\rho}{}_{\nu}.
$$

An antisymmetric $4\times4$ array has $\binom{4}{2}=6$ independent entries. Pair them by the plane they generate: three pairs with one time and one space index, and three pairs with two space indices. The first three are the boosts, the second three are the rotations. The six parameters are not six independent kinds of thing; they are six planes, and there are six planes because there are four dimensions.

**The group is not connected.** Taking determinants of $\Lambda^{\mathsf T}\eta\Lambda=\eta$ gives $\det\Lambda=\pm1$. The $(0,0)$ entry satisfies

$$
\bigl(\Lambda^{0}{}_{0}\bigr)^2=1+\sum_{i}\bigl(\Lambda^{i}{}_{0}\bigr)^2\ \ge 1,
$$

so $\Lambda^{0}{}_{0}$ is never zero and cannot change sign along a continuous path. The two signs of the determinant and the two signs of $\Lambda^{0}{}_{0}$ therefore cut the group into four pieces, and no path joins two of them. Each piece is named by two bits, proper or improper and orthochronous or not, and the discrete maps

$$
\mathsf P=\operatorname{diag}(1,-1,-1,-1),\qquad
\mathsf T=\operatorname{diag}(-1,1,1,1),\qquad
\mathsf{PT}=-\eta
$$

lie in three of the four, so each piece is a coset of the piece containing the identity.

**Only one piece is the group of observers.** The identity component, written $\mathrm{SO}^{+}(1,3)$ and called the proper orthochronous Lorentz group, is the set of $\Lambda$ with $\det\Lambda=+1$ and $\Lambda^{0}{}_{0}\ge1$. It is the piece that carries a physical frame into another physical frame continuously, without reversing time or orientation. The other three are reached from it by composing with $\mathsf P$, $\mathsf T$ or $\mathsf{PT}$, and those maps are symmetries of the theory rather than changes of frame: no continuous motion of an observer turns a right-handed frame into a left-handed one, or a future-pointing clock into a past-pointing one. Two of the four pieces are groups and two are not.

### The two families, and the number that is not an angle

**A rotation is a Lorentz transformation that fixes the time axis.** It acts on $\mathbf{x}$ by an orthogonal matrix, so it has three parameters and is written with an axis $\hat{\mathbf n}$ and an angle $\theta$,

$$
R(\hat{\mathbf n},\theta)=\exp\bigl(-\theta\,\hat{\mathbf n}\cdot\mathbf{J}\bigr),
$$

and every rotation is periodic, $R(\hat{\mathbf n},\theta+2\pi)=R(\hat{\mathbf n},\theta)$.

**A boost is a Lorentz transformation that fixes a plane through the time axis and acts on the remaining two directions by a hyperbolic rotation.** With $\boldsymbol\beta=\beta\hat{\mathbf n}$ and $\gamma=(1-\beta^2)^{-1/2}$,

$$
\Lambda_{\mathrm b}(\hat{\mathbf n},w)=
\begin{pmatrix}
\gamma & -\gamma\boldsymbol\beta^{\mathsf T}\\
-\gamma\boldsymbol\beta & I+(\gamma-1)\,\hat{\mathbf n}\hat{\mathbf n}^{\mathsf T}
\end{pmatrix},
\qquad
\beta=\tanh w,\quad \gamma=\cosh w .
$$

The parameter $w$ is the **rapidity**, and it is the additive parameter of the family, because the addition theorem of the hyperbolic tangent,

$$
\frac{\tanh w_1+\tanh w_2}{1+\tanh w_1\tanh w_2}=\tanh(w_1+w_2),
$$

is the velocity addition law written in the parameter that linearises it. Two collinear boosts of rapidities $w_1$ and $w_2$ compose to one of rapidity $w_1+w_2$.

**The two families differ in the character of their parameter, and that is the whole difference.** The five groups that contain the two families, and what each of them leaves invariant, are collected in [The Rotations, the Boosts and the Groups](the-rotations-the-boosts-and-the-groups.html). A rotation has a periodic parameter; a boost has a non-periodic one. So the rotation set is compact and the boost set is unbounded, and a boost never returns to the identity while a rotation always does. The group is non-compact, and this is the same statement as: velocities are bounded below the speed of light and rapidities are not bounded at all.

**The half-angle is a number the standard account meets and does not explain.** For a boost of rapidity $w$,

$$
\cosh\tfrac{w}{2}=\sqrt{\tfrac{\gamma+1}{2}},\qquad
\sinh\tfrac{w}{2}=\sqrt{\tfrac{\gamma-1}{2}} .
$$

At $\beta=0.6$ the numbers are $\gamma=1.25$, $w=0.693147$, $\cosh\tfrac w2=1.060660$. The half-angle is used because $\cosh w$ and $\sinh w$ factor through it, and the standard account has no further reason for it. Part Two supplies one.

### Boosts do not close

The six parameters do not form six independent directions of a group that is a product. Rotations compose to rotations and form a subgroup. Boosts do not.

Take two boosts with perpendicular directions, of rapidities $a$ and $b$. Their product is a Lorentz transformation, so it lies in the group, but it is not a boost: it is a boost followed by a rotation about the axis perpendicular to both. The rotation is the **Wigner rotation**. For $a=0.7$ and $b=0.9$ the product splits as

$$
\Lambda_{\mathrm b}(\hat{\mathbf y},0.9)\,\Lambda_{\mathrm b}(\hat{\mathbf x},0.7)
=\Lambda_{\mathrm b}(\hat{\mathbf u},w)\,\Lambda_{\mathrm{rot}}(\hat{\mathbf z},\theta),
\qquad
\cosh w=\cosh a\cosh b,\quad \beta=0.831224,
$$

and the angle obeys the closed form

$$
\tan\theta=\frac{\sinh a\,\sinh b}{\cosh a+\cosh b},
$$

which gives $\theta=0.281950$ here, matching the numerical split to nine digits. For small rapidities the angle is quadratic: at $\varepsilon=0.2,\,0.1,\,0.05,\,0.025$ the ratio $\theta/\varepsilon^2$ reads $0.4967$, $0.4992$, $0.4998$, $0.4999$, so $\theta=\tfrac12\varepsilon^2+O(\varepsilon^4)$.

**The reason is a commutator.** In the Lie algebra the bracket of two boost generators is a rotation generator,

$$
[K_i,K_j]=-\epsilon_{ijk}J_k ,
$$

so the failure of $\{\mathbf K\}$ to close is exactly the statement that the boost directions do not span a subalgebra. The effect is second order for the same reason: it is the bracket, and the bracket is the leading correction to the product of two exponentials. Its measurable form is the Thomas precession, the rotation of a particle's rest frame at a rate fixed by this angle per unit proper time, worked out once in [Exercise: The Thomas Precession](exercise-the-thomas-precession.html).

### The algebra, and the invariant that is not a scalar

The six generators close on three bracket rows,

$$
[J_i,J_j]=\epsilon_{ijk}J_k,\qquad
[J_i,K_j]=\epsilon_{ijk}K_k,\qquad
[K_i,K_j]=-\epsilon_{ijk}J_k .
$$

In order, the rows say: the rotations are a subalgebra of dimension three; a rotation turned by a boost is a boost, so $\mathbf K$ transforms as a vector; and two boosts make a rotation, so $\mathbf K$ is not a subalgebra. The third row is the only asymmetry in the table, and everything in the previous section follows from it.

**There is one quadratic invariant, and it is the parity-even one.** The combination

$$
C_1=J^2-K^2
$$

commutes with all six generators. The other natural contraction,

$$
C_2^{\,\mathrm{ps}}=J\cdot K ,
$$

commutes with all six as well, being built from the bracket alone, so it is an invariant of the connected group. But it is a **pseudoscalar**: under parity $\mathbf J$ is axial and $\mathbf K$ is polar, so $J\cdot K\mapsto-J\cdot K$. It is an invariant of $\mathrm{SO}^{+}(1,3)$ and not of the full $\mathrm{O}(1,3)$, and it cannot be added to $C_1$ to make a second scalar invariant of the same kind.

This is the first sign that the real algebra is not the natural home for the two invariants. The second sign is the complexification.

### Complexification, and the two labels

Complexify the algebra. A short computation shows

$$
\mathfrak{so}(1,3)_{\mathbb{C}}\cong\mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C}),
$$

of complex dimension $6$, with the splitting elements

$$
\vec J_{\pm}=\tfrac12\bigl(\vec J\pm i\vec K\bigr),
\qquad
[J_{\pm}^{i},J_{\pm}^{j}]=\epsilon_{ijk}J_{\pm}^{k},
\qquad
[J_{+}^{i},J_{-}^{j}]=0 .
$$

Each triple closes as a complex $\mathfrak{su}(2)$ and the two triples commute. The step that produced them is not a rotation of the algebra but a change of complex basis, and it is what $C_2^{\,\mathrm{ps}}$ was refusing to be in the real algebra. In the complexified algebra the two invariants become the two Casimirs

$$
C_1=\tfrac12\bigl(\vec J^{\,2}-\vec K^{\,2}\bigr),\qquad
C_2=-\tfrac{i}{2}\{\vec J,\vec K\},
$$

with eigenvalues $m(m+1)+n(n+1)$ and $m(m+1)-n(n+1)$ on a carrier labelled by a pair of half-integers $(m,n)$, of dimension $(2m+1)(2n+1)$. So $(0,0)$ is the scalar, $(\tfrac12,0)$ and $(0,\tfrac12)$ are the two Weyl spinors, and $(\tfrac12,\tfrac12)$ is the four-vector. Parity exchanges the two labels, which is why a single Weyl spinor carries no mass term and a Dirac pair does.

**Three real forms, one complex algebra.** The slices that matter are $\mathfrak{so}(1,3)$, $\mathfrak{so}(4)$ and $\mathfrak{so}(2,2)$. They differ in the signature of their invariant form and in which of the two chiral triples is compact. Choosing among them is choosing the signature of spacetime, and that choice is made by physics — one time and three spaces — not by the algebra, which contains all three.

### The double cover, and where the half-angle comes from

$\mathrm{SO}^{+}(1,3)$ is not simply connected: a rotation by $2\pi$ is the identity in the group, but the path that performs it is not contractible. The universal cover is a group mapping onto it two-to-one,

$$
\mathrm{SL}(2,\mathbb{C})\longrightarrow \mathrm{SO}^{+}(1,3),
\qquad\text{kernel of order }2 .
$$

A representation of the covering group therefore need not be a representation of the group: the two elements over the identity may act as $+1$ and $-1$. Those are the spinor representations, and the sign is why a spinor returns to minus itself after one turn and to itself after two. The half-angle of the boost belongs to the same cover: the boost matrix is the square of an element of the covering group, and its parameter is half the rapidity for that reason.

**A representation of the group is then of two kinds, and only one of them is finite.** The finite-dimensional ones, labelled $(m,n)$, are not unitary. The argument is short. If a finite-dimensional representation of a connected semisimple group were unitary, its image would be a compact subgroup of $\mathrm{GL}_n(\mathbb{C})$ and the Lie algebra would map into a compact real form; the boosts, being non-compact, would have to act with purely imaginary eigenvalues, whereas they act with real ones. So no nontrivial finite-dimensional representation is unitary. The unitary ones are infinite-dimensional: the principal series and the complementary series, induced from a parabolic subgroup, with one discrete and one continuous parameter, computed in [The Principal Series and the Complementary Series](the-principal-series-and-the-complementary-series.html).

The division of labour that follows is the one physics uses. The finite carriers $(m,n)$ are the **fields**: the field strength in $(1,0)\oplus(0,1)$, the Dirac field in $(\tfrac12,0)\oplus(0,\tfrac12)$, the potential in $(\tfrac12,\tfrac12)$. The infinite carriers are the **states**. A field is a finite representation that happens not to be unitary; a state is a unitary representation that happens not to be finite.

### The orbits: mass and spin

Add the translations and the group is the Poincaré group, whose two Casimirs are

$$
P^2=P_\mu P^\mu,\qquad
W^2=W_\mu W^\mu,\qquad
W_\mu=\tfrac12\epsilon_{\mu\nu\rho\sigma}P^{\nu}M^{\rho\sigma}.
$$

$P^2$ takes three signs, and the sign is invariant, so momenta fall into three families, timelike, null and spacelike. On each orbit $W^2$ reduces to a label of the subgroup fixing a representative momentum, the **little group**. For a massive particle the representative is the rest frame, the little group is $\mathrm{SU}(2)$, and its weight is the spin, with $2s+1$ states per momentum; the case is set out in [The Little Group of a Massive Particle: $\mathrm{SU}(2)$](the-little-group-of-a-massive-particle-su2.html), and the orbit count in [Wigner's Classification: Two Casimirs, Three Orbits](wigers-classification-two-casimirs-three-orbits.html). For a massless particle the representative is a null momentum, the little group is $E(2)$, its $\mathrm{U}(1)$ part gives the helicity, and its two null translations act trivially on any state of finite helicity, so a massless particle has one helicity state per momentum and not a continuum: [The Little Group of a Null Momentum: $E(2)$](the-little-group-of-a-null-momentum-e2.html). For a spacelike momentum the little group is $\mathrm{SU}(1,1)$.

That is the standard account, and it is complete as it stands: two Casimirs, three orbits, two little groups of physical interest.

## Part Two: Why the Biquaternion Algebra Reproduces It

The question is now sharp. An algebra could reproduce the group by accident, by containing a matrix copy of it; every algebra of matrices does. The interesting question is whether the algebra's **own multiplication** — the product it has before any matrix is written — already contains the group, its action and its invariant, so that the standard theorems become statements about one product.

For the biquaternion algebra the answer is yes, and the reason is one identity.

### The one algebraic fact

Let $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ be the complexified quaternion algebra, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$ where $e_t$ is the identity and $\vec e_\eta^2=-e_t$. Write an element as $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ with complex coefficients. Let ${}^{\natural}$ be the quaternion conjugation, fixing the scalars and negating the vectors, and ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ its composition with complex conjugation. The **biquaternion norm** is

$$
N(\tilde Q)=\tilde Q\tilde Q^{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2 .
$$

As a complex algebra, $\mathbb{B}\cong M_2(\mathbb{C})$, of complex dimension $4$, and under that reading the norm is the determinant,

$$
\det\mathsf{M}_2(\tilde Q)=N(\tilde Q).
$$

This is the identity the whole correspondence rests on, and it has two consequences.

**The norm is multiplicative.** $N(\tilde Q_1\tilde Q_2)=N(\tilde Q_1)N(\tilde Q_2)$, by the determinant of a product, or directly from the product rule of ${}^{\natural}$. The form is complex-valued and vanishes on a cone; it is not an analytic norm.

**The unit-norm set is a group.** If $N(\tilde U)=N(\tilde V)=1$ then $N(\tilde U\tilde V)=1$; the inverse is $\tilde U^{\natural}$, of norm $1$; the identity $e_t$ has norm $1$. So

$$
G=\{\tilde U\in\mathbb{B} : N(\tilde U)=1\}
$$

is a group, inside the invertible elements, of complex dimension $3$ and real dimension $6$ — the same six as Part One, and for the same reason: one complex equation on four complex coordinates.

### The group of the algebra is the covering group of the group of spacetime

$N=1$ is $\det=1$, so $G=\mathrm{SL}(2,\mathbb{C})$. That is the covering group of the previous section, obtained without a matrix and without a choice of basis of $\mathbb{R}^4$.

| the standard object | the algebra's object |
|---|---|
| the covering group $\mathrm{SL}(2,\mathbb{C})$ | the elements of unit biquaternion norm |
| the condition $\det=1$ | the condition $N=1$ |
| the two-to-one cover | the sign $\pm e_t$ |
| real dimension $6$ | one complex equation on four complex coordinates |

**It is not a matrix trick.** The matrix model exists, is exact and is used as a dictionary, but it is a reading of the algebra, not the definition of the group. The group is defined by the algebra's own multiplicative form, and that form is the one its units already carry: $N(e_t)=1$ and $N(\vec e_\eta)=-1$, so the norm is the quadratic form of the base.

### The action is one product, and it preserves the interval for one reason

The algebra acts on itself. The four-vectors of Part One are the anti-Hermitian elements — imaginary scalar, real vector — and a unit element acts on them by the congruence

$$
\tilde X\longmapsto \tilde U\,\tilde X\,\tilde U^{*}.
$$

**The image is a four-vector.** $\bigl(\tilde U\tilde X\tilde U^{*}\bigr)^{*}=\tilde U\tilde X^{*}\tilde U^{*}=-\tilde U\tilde X\tilde U^{*}$, using that ${}^{*}$ is an involution. The sector is preserved by the conjugate on the right, which is the part a naive action on one side gets wrong.

**The interval is preserved, and this is the whole of the theorem.** The interval of $\tilde X$ is its norm: with $X_t=ix_0$ and real $\mathbf x$,

$$
N(\tilde X)=-x_0^2+\lvert\mathbf x\rvert^2 ,
$$

which is $s^2$ of signature $(3,1)$. Then

$$
N\bigl(\tilde U\tilde X\tilde U^{*}\bigr)
=N(\tilde U)\,N(\tilde X)\,N(\tilde U^{*})
=1\cdot N(\tilde X)\cdot 1
=N(\tilde X),
$$

using multiplicativity twice and $N(\tilde U^{*})=\overline{N(\tilde U)}=1$. In Part One the interval was preserved because the group was **defined** to preserve it. Here the group is defined by a form, and preservation is a consequence of one multiplicativity. That is the difference in kind between the two descriptions.

**The map is a homomorphism onto the proper orthochronous group.** Congruence by $\tilde U\tilde V$ is congruence by $\tilde V$ then by $\tilde U$, so the map preserves products. Its image lies in $\mathrm{O}(1,3)$ because the form is preserved, in the identity component because $G$ is connected, and it has the dimension of the group, so it is all of $\mathrm{SO}^{+}(1,3)$.

**The kernel is the sign, and the cover is now visible.** $\tilde U$ acts trivially exactly when $\tilde U=\pm e_t$, so

$$
G/\{\pm e_t\}\cong \mathrm{SO}^{+}(1,3),
$$

and the two-to-one cover of Part One is the sign of an element of the algebra. The half-angle is explained at the same moment. The boost element

$$
\tilde U_{\mathrm b}=\cosh\tfrac w2\,e_t+i\sinh\tfrac w2\,\hat{\mathbf n}
$$

has norm $\cosh^2\tfrac w2-\sinh^2\tfrac w2=1$, so it is a unit element, and its parameters are half the rapidity because the square root of a boost is a boost of half the rapidity. Part One had $\sqrt{(\gamma+1)/2}$ and no reason; here the same number has one.

**A boost, written out.** For $\tilde U_{\mathrm b}=\cosh\tfrac w2\,e_t+i\sinh\tfrac w2\,\vec e_x$ the congruence gives, on the coordinates $(x_0,x_1,x_2,x_3)$,

$$
\Lambda_{\mathrm b}=
\begin{pmatrix}
\cosh w & -\sinh w & 0 & 0\\
-\sinh w & \cosh w & 0 & 0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix},
$$

which is the boost of Part One with $\gamma=\cosh w$ and $\gamma\beta=\sinh w$. The rotation is the same construction with a real quaternion, $\tilde u=\cos\tfrac\theta2\,e_t+\sin\tfrac\theta2\,\hat{\mathbf n}$, of norm $\cos^2\tfrac\theta2+\sin^2\tfrac\theta2=1$, whose congruence is $R(\hat{\mathbf n},\theta)$ and which returns to minus itself at $\theta=2\pi$ — the cover, in a single sign.

### The six parameters as a product of two three-parameter sets

The group has six real dimensions and the two families have three each. In the algebra the split is the polar decomposition, and it is a theorem, not a parametrisation.

**Every unit element is Hermitian-positive times unitary.** For $\tilde U\in G$ set

$$
\tilde H=\bigl(\tilde U\tilde U^{*}\bigr)^{1/2},\qquad
\tilde K=\tilde H^{-1}\tilde U,\qquad
\tilde U=\tilde H\tilde K .
$$

$\tilde U\tilde U^{*}$ is Hermitian and positive, so $\tilde H$ is; and $\tilde K\tilde K^{*}=\tilde H^{-1}\tilde U\tilde U^{*}\tilde H^{-1}=e_t$, so $\tilde K$ is unitary. Both have norm $1$. A check on one hundred random elements returns the split every time.

**The two factors are the two families.** $\tilde H$ has real scalar part and imaginary vector part, so it is the boost, and its congruence is a pure boost fixing a plane through the time axis. $\tilde K$ is a real quaternion of unit norm, so it is the rotation, and its congruence fixes the time axis. The count $3+3$ is therefore the count of Part One: three numbers for the velocity of the frame, three for the orientation of its axes, no number shared.

**The order is a convention with a reason.** The orderings $\tilde H\tilde K$ and $\tilde K'\tilde H$ differ by a rotation, and the rotation that reconciles them is the conjugating factor. The corpus takes the boost first, the order in which the boost is the part that changes the observer's motion. Read as a parametrisation of the group, this is the global Cartan decomposition $\mathrm{SL}(2,\mathbb{C})=P\cdot K$; the exponential chart that reaches every element is in [The Exponential Map from Algebra to Group](the-exponential-map-from-algebra-to-group.html).

**The mixing that Part One found is here as a failure to commute.** The two factors do not commute, and the amount by which they fail is the Wigner rotation of Part One, because the product $\tilde K^{-1}\tilde H^{-1}\tilde K\tilde H$ is an element of $G$ whose congruence is that rotation.

### The commutator table is the same table

Take the generators as elements of the algebra, the three $\tfrac12\vec J$ being imaginary spatial units and the three $\tfrac12\vec K$ built from $i\vec e_\eta$. The brackets are those of the algebra's own multiplication, and they read

$$
[\vec J,\vec J]\subset\vec J,\qquad
[\vec K,\vec K]\subset\vec J,\qquad
[\vec J,\vec K]\subset\vec K .
$$

That is the table of Part One, and its third row is not an accident of a basis. It says that the traceless part of the algebra under the commutator **is** the Lorentz algebra, as a real Lie algebra of dimension six,

$$
\mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}}\cong\mathfrak{so}(1,3).
$$

The check is the invariant form: in the real basis $\{\sigma_x,\sigma_y,\sigma_z,i\sigma_x,i\sigma_y,i\sigma_z\}$ the structure constants give a form of signature $(3,3)$, with eigenvalues $\pm4$ and determinant $-4096$, which is the signature of $\mathfrak{so}(1,3)$. Note what the statement is not: the full algebra under the commutator is $\mathfrak{gl}(2,\mathbb{C})$ of real dimension $8$, and that is not a Lorentz algebra. The trace is the extra direction and must be removed.

**The two Casimirs are the two sums of the two triples.** The complexification of Part One is not an extra step here, because the algebra's scalar imaginary is already there. The triples $\vec J_{\pm}=\tfrac12(\vec J\pm i\vec K)$ commute, and the invariants are

$$
C_1=\tfrac12\bigl(\vec J^{\,2}-\vec K^{\,2}\bigr),\qquad
C_2=-\tfrac{i}{2}\{\vec J,\vec K\},
$$

with eigenvalues $m(m+1)+n(n+1)$ and $m(m+1)-n(n+1)$. The pseudoscalar obstruction of Part One has dissolved, and it dissolved because the algebra was complex from the start. This is the second thing the algebra explains rather than restates: the two chiral labels are the two commuting triples, and they are available without adjoining an $i$, because the $i$ is the one that already carries the minus sign of the interval.

### The elements classified by their own spectrum

An element of $G$ has two eigenvalues, the roots of the characteristic equation of its $2\times2$ image, so they are fixed by its trace and its determinant. Inside $G$ the determinant is $1$, so the pair is $\{\lambda,\lambda^{-1}\}$ and the trace alone decides:

$$
\tau=\operatorname{tr}\mathsf{M}_2(\tilde U)=2Q_t .
$$

Comparing $\tau$ with $\pm2$ gives the four classical kinds of transformation, which are the four kinds of frame:

| $\tau$ | kind | the standard name | what it does |
|---|---|---|---|
| real, $\lvert\tau\rvert<2$ | elliptic | rotation conjugate | a turn about an axis |
| real, $\lvert\tau\rvert>2$ | hyperbolic | boost conjugate | a change of motion |
| $\pm2$ | parabolic | unipotent, null rotation | one Jordan block |
| not real | loxodromic | screw | a turn and a boost about one axis |

The classification is by conjugacy, because a conjugacy class of $\mathrm{SL}(2,\mathbb{C})$ is its eigenvalue pair, and the four boxes are the four positions of $\{\lambda,\lambda^{-1}\}$. Part One classified the group by two discrete signs plus a spectrum; here the signs are carried by the norm and its $\pm$ ambiguity, and the spectrum carries the rest.

**The spectrum does not determine the element.** It fixes $Q_t$ and $B^2=Q_x^2+Q_y^2+Q_z^2$, the scalar part and the modulus, and neither the axes nor the two angles. There is an exact one-parameter family of frames with one spectrum, which is what [The Spectrum Does Not Determine the Frame](the-spectrum-does-not-determine-the-frame.html) shows with a worked case. Part One has the same fact in another dress: six parameters are needed, the eigenvalues supply two complex numbers, and the rest is a continuous freedom plus a discrete choice.

## What the Second Description Buys

**One product.** The group is a set of elements, the action is one multiplication on each side, the invariant is the form the algebra already had, the generators are elements, and the two factors of a frame are one Hermitian and one real element of the same algebra. No matrix, no column, no ideal and no projector is needed. The matrix model is exact and is used as a dictionary; it is not the definition.

**The half-angle has a reason.** A boost is the square root of a boost, and the root's parameter is half the rapidity. In Part One the half-angle was a computational convenience.

**The cover is a sign.** The two-to-one cover, the spinor's return to minus itself after one turn, and the non-contractibility of the $2\pi$ rotation are all the same $\pm e_t$.

**The complexification is already there.** The scalar imaginary that splits $\mathfrak{so}(1,3)_{\mathbb{C}}$ into two chiral triples is the algebra's own $i$, and it is the same $i$ that carries the minus sign of the interval once time is written as $ict$. One symbol does both jobs, and it is the subject of [The Local Complex Structure and the Speed of Light](the-local-complex-structure-and-the-speed-of-light.html).

**The algebra carries the field, not only the group.** Once a frame is a curve $\tilde U(\tau)$ in $G$, its derivative is an element of the algebra and the equation of motion of the frame is a linear equation in the algebra. The eigenspinor of [The Eigenspinor: The Lorentz Rotor as a Function of Proper Time](the-eigenspinor-the-lorentz-rotor-as-a-function-of-proper-time.html), the field strength of [The Field Strength as the Sum of Two Self-Dual Halves](the-field-strength-as-the-sum-of-two-self-dual-halves.html), and the polar decomposition of an arbitrary element are statements of this kind, and none of them has a natural home in a description of the group alone.

## What the Second Description Does Not Buy

**No new group.** What is obtained is the standard $\mathrm{SO}^{+}(1,3)$ acting on the standard four-vectors. The algebra supplies a description in which every piece is an element and one operation; it does not supply a different group, and no experiment distinguishes the descriptions, because they are the same group on the same space.

**No new prediction, by itself.** The correspondences above are identities, and an identity cannot be confirmed or refuted. What can be refuted is a proposal built on them, and the corpus says separately what would count as a signature.

**No translations.** The Poincaré group is a semidirect product, with an additive translation part and a multiplicative rotor part, and the dimension count forbids a faithful embedding of the ten-parameter group into the six-dimensional one. The frame carries the homogeneous part; the translation sits beside it.

**No choice of signature.** The complex algebra contains all three real forms, so the algebra cannot decide which one spacetime takes. The Lorentzian slice is chosen because the interval has one time and three spaces, and it is read off the material sector, not derived from the algebra.

## Summary

The Lorentz group is the set of linear maps of $\mathbb{R}^4$ preserving the Minkowski form, $\Lambda^{\mathsf T}\eta\Lambda=\eta$. Sixteen entries less ten independent conditions leaves six parameters, and the same six appear infinitesimally as the independent entries of an antisymmetric $\omega_{\mu\nu}$: three planes with one time and one space index, three with two space indices. The determinant is $\pm1$ and $\Lambda^{0}{}_{0}$ never vanishes, so the group has four components, and the identity component is the proper orthochronous group, the one a physical frame moves in.

The six parameters are three rotations and three boosts. A rotation has a periodic parameter; a boost has an additive one, the rapidity, with $\beta=\tanh w$ and $\gamma=\cosh w$. Rotations close and boosts do not. Two perpendicular boosts compose to a boost times a rotation, the Wigner rotation, with $\tan\theta=\sinh a\sinh b/(\cosh a+\cosh b)$, second order in the rapidities because $[K_i,K_j]$ is a rotation generator.

The real algebra has one scalar quadratic invariant, $J^2-K^2$, and one pseudoscalar contraction, $J\cdot K$. Complexified, it splits into two commuting $\mathfrak{sl}(2,\mathbb{C})$'s, and the invariants become the two Casimirs with eigenvalues $m(m+1)\pm n(n+1)$ on the label $(m,n)$. Parity exchanges the labels; the finite representations are all non-unitary; the unitary ones are infinite-dimensional. On momenta, the two Poincaré Casimirs give three orbits and the little groups give mass and spin.

The biquaternion algebra reproduces every one of those statements from one identity: its norm is the determinant of its $2\times2$ image, and the norm is multiplicative. The unit-norm elements are therefore a group, equal to $\mathrm{SL}(2,\mathbb{C})$, which is the covering group of the first half. A unit element acts on a four-vector by the congruence $\tilde X\mapsto\tilde U\tilde X\tilde U^{*}$; the sector is preserved because ${}^{*}$ is an involution, and the interval is preserved because the norm is multiplicative. The kernel is $\{\pm e_t\}$, so the cover is a sign, and the half-angle of a boost is the parameter of the square root of its transformation.

Every unit element is a Hermitian positive factor times a unitary one, a boost times a rotation, and $3+3=6$ is the polar decomposition. The commutator table of the algebra is the table of the first half, its third row being the statement that the traceless part under the bracket is the real Lorentz algebra of dimension six. The complexification needs no step, because the scalar imaginary is the algebra's own, and the two chiral labels are the two commuting triples. The elements are classified by their trace, and the four kinds are the four conjugacy classes.

The second description buys a single product, a reason for the half-angle, a sign for the double cover, and an algebra in which the field as well as the group can be written. It buys no new group, no new prediction, no translations and no signature.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\eta$ | $\operatorname{diag}(1,-1,-1,-1)$, the Minkowski form |
| $\Lambda$ | a Lorentz transformation, $\Lambda^{\mathsf T}\eta\Lambda=\eta$ |
| $\mathrm{SO}^{+}(1,3)$ | the proper orthochronous component, the identity component |
| $\mathbf J,\mathbf K$ | the rotation and boost generators |
| $w$ | rapidity, with $\beta=\tanh w$ and $\gamma=\cosh w$ |
| $C_1,C_2$ | the two Casimirs of the complexified algebra |
| $(m,n)$ | representation labels, of dimension $(2m+1)(2n+1)$ |
| $P^2,W^2$ | the Poincaré Casimirs, mass and spin |
| $\mathbb{B}$ | the biquaternion algebra, $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_t,\vec e_\eta$ | its units, $e_t$ the identity and $\vec e_\eta^2=-e_t$ |
| $N(\tilde Q)$ | the biquaternion norm, $\tilde Q\tilde Q^{\natural}=Q_t^2+B^2$ |
| ${}^{\natural}$, ${}^{*}$ | quaternion and Hermitian conjugation |
| $G$ | the set $N=1$, the group of unit-norm elements |
| $\tilde H,\tilde K$ | the Hermitian positive and the unitary factors |
| $\tau$ | $\operatorname{tr}\mathsf{M}_2(\tilde U)=2Q_t$, the classifier |

## Further Reading

- S. Weinberg, *The Quantum Theory of Fields*, vol. 1, chapters 2 and 5, for the group, its algebra, Wigner's classification and the little groups.
- E. Wigner, "On unitary representations of the inhomogeneous Lorentz group", *Ann. of Math.* 40 (1939), for the orbits and the little groups at their source.
- V. Bargmann, "Irreducible unitary representations of the Lorentz group", *Ann. of Math.* 48 (1947), for the principal and complementary series.
- A. O. Barut and R. Raczka, *Theory of Group Representations and Applications*, for the complexification, the real forms and the $(m,n)$ calculus.
- J. D. Jackson, *Classical Electrodynamics*, §11.7, for the Thomas precession and the composition of non-collinear boosts.
- C. Møller, *The Theory of Relativity*, for the four components of the group and the discrete symmetries.
- [The Isomorphisms and Their Dimensions](the-isomorphisms-and-their-dimensions.html), for the three isomorphism statements and their dimensions.
- [The Group of Unit-Norm Biquaternions](the-group-of-unit-norm-biquaternions.html), for the group as a set.
- [A Frame Is a Boost Times a Rotation: The Cartan Word](a-frame-is-a-boost-times-a-rotation-the-cartan-word.html), for the polar decomposition and its order.
- [The Six Generators and Their Commutators](the-six-generators-and-their-commutators.html), for the bracket table and the invariant form.
- [The Two Commuting Complex Triples](the-two-commuting-complex-triples.html), for the splitting and its caveats.
- [The Two Casimirs of the Lorentz Algebra](the-two-casimirs-of-the-lorentz-algebra.html), for the normalisation and the eigenvalues.
- [The Two-Sheeted Cover and the Topology of Boosts in Biquaternionic Form](the-two-sheeted-cover-and-the-topology-of-boosts-in-biquaternionic-form.html), for the cover as an algebraic sign.
- [The Four Kinds of Frame Transformation](the-four-kinds-of-frame-transformation.html), for the conjugacy classes and their fixed sets.
