# __Introduction to the Spin-Half Bispinors Spaces__

## Introduction

**This entry reads the second of the three carriers in detail: the spinor plane, the two subspaces that close it, and the two-component object that a fermion carries at each event.** The mathematics is one article and its two companions, and its answer is longer than the spin-zero answer for a structural reason. The carrier of spin zero needs one closure and has one. The carrier of spin one half needs two, and it has two: the plane is the carrier, the minimal left ideal is its first closure, and the algebra split by a pair of idempotents is the second. A field with values in the first closure is a Weyl spinor; a field with values in the second is a Dirac spinor. Both closings are the same algebraic step repeated, and the entry keeps them apart because physics uses both.

**The first claim is that the carrier is a complex line, of real dimension two.** For a unit real axis $\vec u$ the element $\tilde\Pi_+(\vec u)=\tfrac12(e_t+i\vec u)$ is idempotent, its norm vanishes, and the plane $\mathbb{C}\tilde\Pi_+(\vec u)$ is two real dimensional and one complex dimensional. Left multiplication acts on it by the phase $e^{-i\theta/2}$, the weights are $\pm\tfrac12$, the spin is $\tfrac12$, the identity $2s+1=\dim_\mathbb{R}$ reads $2=2$, and a full turn acts as $-\mathrm{id}$. All five statements are verified below to machine precision.

**The second claim is that the plane is a carrier for one circle and not for the group.** Left multiplication by the axis of the plane preserves it; left multiplication by a transverse axis does not, and the image of $\tilde\Pi_+$ lands at distance $\sqrt2/2$ from the plane. This is the one carrier of the three whose invariance fails, and it is why the spin-half case has two closures where the other two have one.

**The third claim is that the first closure is a minimal left ideal, of real dimension four.** The subspace $\mathbb{B}\tilde\Pi_+(\vec u)$ adds the transverse direction and nothing else, is closed under left multiplication by the whole algebra, has no smaller invariant left subspace, and is null: the norm vanishes on all of it. A field valued in it is a two-component spinor, and the algebra acts on it irreducibly.

**The fourth claim is that the second closure is the algebra split by the pair of idempotents.** The two ideals $S_+$ and $S_-$ meet only at zero, each is null, and $\mathbb{B}=S_+\oplus S_-$. A field valued in both is a four-component spinor. The norm on that space is not a norm on either summand: it is the pairing $N(X_++X_-)=2B(X_+,X_-)$, so the invariant length of a bispinor is the pairing of its two chiral halves and of nothing else.

**The fifth claim is that the norm measures mixedness, and that the nullity of the carrier is purity.** For a state $S_{\vec r}=\tfrac12(e_t+i\vec r)$ the norm, the failure of idempotence and the departure from the Bloch sphere are one quantity:

$$
N(S_{\vec r})=\tfrac14\bigl(1-\lvert\vec r\rvert^{2}\bigr),\qquad S_{\vec r}^{2}=S_{\vec r}-N(S_{\vec r})\,e_t .
$$

Verified exactly. A state is a projector precisely when its norm vanishes, so the plane consists of pure states and the vanishing norm is not a defect of the carrier but its definition. The spin-zero carrier was null-free because a complex number is not a state; the spin-half carrier is null because a pure state is a projector.

**The sixth claim is that the two ideals are the two spinor chiralities.** Right multiplication by $-i\vec e_z$ acts as $-1$ on $S_+(\vec e_z)$ and as $+1$ on $S_-(\vec e_z)$, verified to $0$, so the two ideals are the two eigenspaces of the chirality operator when the axis is the frame's third direction. The coefficient conjugation, which sends $i$ to $-i$ and leaves the invertibles alone, is an algebra automorphism and exchanges the two ideals. And because each ideal is null on its own, a field of one chirality has no invariant length: a mass term has to pair the two.

**The first objection is that a null carrier cannot be a carrier of anything physical.** It can, and the nullity is the point. The plane is null because a pure state is a projector, and a projector has zero norm in this algebra for the same reason that $\tfrac12(1+\sigma_z)$ has determinant zero in the Pauli algebra. The norm of the algebra is not a Hilbert norm; it is the determinant, and the determinant of a rank-one projector is zero. What the entry keeps apart is the algebraic norm $N$, which vanishes on the carrier, and the Hermitian form $\langle X,X\rangle_{*}=\sum_\mu\lvert X_\mu\rvert^{2}$, which is positive on the whole algebra and which normalises a state.

**The second objection is that a carrier of real dimension two cannot hold a spinor, which has four real components.** The objection is right about the spinor and wrong about the carrier. A spinor is the closure, not the carrier. The carrier is the minimal subspace the action moves; the closure is the space a field takes values in; the two are different objects and the entry names them differently throughout. For spin zero the two happened to differ by a factor of two in dimension; here they differ by a factor of two as well, from two to four, and the second closure takes four to eight.

**The third objection is that the axis is a coordinate and the article builds physics on a coordinate.** The axis is a coordinate in the sense that it can be rotated, and the entry states exactly that and refuses to make it a datum. What survives the rotation is the structure: every axis gives a plane, an ideal, and a pair; no axis is preferred; and a statement proved at one axis holds at every axis because the group moves one axis to another and carries the whole family with it. The frame enters once, when a value or a chirality is named, and the entry marks that place.

**The letters.** The algebra is $\mathbb{B}$, real of dimension eight, units $e_t,\vec e_x,\vec e_y,\vec e_z$, with $e_t$ the identity and $\vec e_k^{2}=-e_t$; the central imaginary is $i$; an element is $\tilde Q=Q_te_t+\vec Q$ with complex coefficients. The star ${}^{*}$ is the Hermitian conjugation, the bar $\bar{\cdot}$ the coefficient conjugation, and ${}^{\natural}$ the natural conjugation. The norm is $N(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$ and $B$ is its polar form. A unit real axis is $\vec u$, with $\vec u_2,\vec u_3$ an oriented orthonormal pair completing it; the idempotents are $\tilde\Pi_\pm(\vec u)=\tfrac12(e_t\pm i\vec u)$; the plane is $\Sigma(\vec u)=\mathbb{C}\tilde\Pi_+(\vec u)$; the ideals are $S_\pm(\vec u)=\mathbb{B}\tilde\Pi_\pm(\vec u)$; the action is left multiplication, $L_X(Y)=XY$. The sectors are $\mathbb{B}_\Psi=\{X^{*}=X\}$ and $\mathbb{B}_\Phi=\{X^{*}=-X\}$, and the four sectors of the two predicates are written $\Sigma_{ij}$. A rotor is $\tilde u=\cos\tfrac\theta2e_t+\sin\tfrac\theta2\vec u$, and the spectrum of an element is the pair $\lambda_{\pm}=Q_t\pm iB$ with $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$.

**Boundaries.** The plane, the two closures, the infinity of the family and the corners are *Introduction to the Spin-Half Bispinors Spaces*; the nullity of the idempotent, of the plane and of the ideals, the isotropic dimension and the pairing are *The Spin-Half Bispinors and N Norm Regularity*; the spectrum $\{0,\lambda\}$, the degenerate plane inside the ideal and the square-zero elements are *The Spin-Half Bispinors and Spectral Regularity*; the list of three carriers and the four closure rules are *From the Spin to the Carriers and the Closures*; the idempotents, the minimality and the splitting are *The Minimal Left Ideals of the Biquaternion Algebra*; the parametrisation of the family is *The Peirce Basis of the Biquaternion Algebra*; the one-sided action as a representation is *The One-Sided Action and the Spin Representation*. The physics is read from *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, *The Dirac Equation in Biquaternionic Form*, *Chiral Fermions in the Biquaternion Framework*, *States, Observables and the Born Weight*, *Chirality and the Weyl Spinors*, *The Celestial Sphere of the Null Cone* and *Two Spin-Half Particles*. No dynamics, no mass value and no quantum postulate appear below.

## The Source Table

| mathematical content | source article |
| --- | --- |
| the idempotent, the plane, the action and the half angle, the failure of invariance, the two closures, the family and the corners | [Introduction to the Spin-Half Bispinors Spaces](../articles_maths/the-spin-half-bispinor-spaces.html) |
| the nullity of the idempotent, of the plane and of the ideals, the isotropic dimension, the pairing $N=2B$ and its nondegeneracy | [The Spin-Half Bispinors and N Norm Regularity](../articles_maths/the-spin-half-bispinor-spaces-and-n-norm-regularity.html) |
| the square $B^{2}=-\lambda^{2}/4$ on the plane, the spectrum $\{0,\lambda\}$, the degenerate plane of the ideal and the square-zero elements | [The Spin-Half Bispinors and Spectral Regularity](../articles_maths/the-spin-half-bispinor-spaces-and-spectral-regularity.html) |
| the list of three carriers, the criterion of the weight string and the four closure rules | [From the Spin to the Carriers and the Closures](../articles_maths/the-carriers-the-representation-the-spin-and-the-closure.html) |
| the idempotents, the minimality of the left ideals and the splitting of the algebra | [The Minimal Left Ideals of the Biquaternion Algebra](../articles_maths/the-minimal-left-ideals-of-the-biquaternion-algebra.html) |
| the Peirce basis and the parametrisation of the family by the axis | [The Peirce Basis of the Biquaternion Algebra](../articles_maths/the-peirce-basis-of-the-biquaternion-algebra.html) |
| left multiplication as a representation and the two-sided operator as its tensor square | [The One-Sided Action and the Spin Representation](../articles_maths/the-one-sided-action-and-the-spin-representation.html) |
| the two predicates and the four sectors | [Relations between the N Norm and Spectral Regularity and Degeneracy](../articles_maths/relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html) |

**The four rows that own the carrier.** The first three state the plane, the two predicates and the degenerate locus. The last four supply the context: the place of the carrier in the list of three, the minimality that makes the first closure canonical, the basis that parametrises the family, and the operator theory that turns left multiplication into a representation.

## The Results in Brief

**The carrier.** The plane $\Sigma(\vec u)=\mathbb{C}\tilde\Pi_+(\vec u)$, of real dimension $2$ and complex dimension one, with the idempotent of the axis as its generator.

**The first closure.** The minimal left ideal $S_+(\vec u)=\mathbb{B}\tilde\Pi_+(\vec u)$, of real dimension $4$ and complex dimension two, spanned over $\mathbb{C}$ by $\tilde\Pi_+$ and $\vec u_2\tilde\Pi_+$.

**The second closure.** The bispinor space $\mathbb{B}=S_+(\vec u)\oplus S_-(\vec u)$, of real dimension $8$, which as a set is the algebra and as a decomposition is the algebra together with the pair of idempotents.

**The action.** Left multiplication at every element: $\varrho(X)=L_X$, with $L_X(Y)=XY$. It preserves each ideal and does not preserve the plane.

**The half angle.** $\vec u\tilde\Pi_+=-i\tilde\Pi_+$ and $\tilde u\tilde\Pi_+=e^{-i\theta/2}\tilde\Pi_+$, so the rotor multiplies the plane by a phase and the phase is half the rotation angle.

**The two numbers.** The weights are $\pm\tfrac12$, the spin is $\tfrac12$, $2s+1=2$ is the dimension of the carrier, and a full turn acts as $-\mathrm{id}$, which is $(-1)^{2s}$.

**The norm.** $N(\lambda\tilde\Pi_+)=0$ for every $\lambda$; the norm vanishes on the plane and on each ideal, so no element of a single chirality is norm-regular.

**The spectrum.** $B^{2}(\lambda\tilde\Pi_+)=-\lambda^{2}/4$, so the plane is spectrally regular off the origin, with $\operatorname{spec}(\lambda\tilde\Pi_+)=\{0,\lambda\}$ and $\operatorname{spec}(\tilde\Pi_+)=\{0,1\}$.

**The sector.** The plane away from the origin is $\Sigma_{01}$: null and spectrally regular. It is the only carrier in that sector.

**Inside the ideal.** Every element has $\operatorname{spec}(Y)=\{0,2Q_t(Y)\}$; the degenerate elements are those with $Q_t=0$, they form the real plane $\mathbb{C}(\vec u_2-i\vec u_3)$, and they are exactly the elements with $Y^{2}=0$.

**The isotropic dimension.** Each ideal is a maximal totally isotropic subspace: the norm and the polar form vanish on it, and its real dimension is half of eight.

**The pairing.** $N(X_++X_-)=2B(X_+,X_-)$, and the restriction of $B$ to $S_+\times S_-$ is nondegenerate: the invariant length of a bispinor is the duality pairing of its two halves.

**The two spinor chiralities.** Under the coefficient conjugation the two ideals are exchanged, $\bar\Pi_+=\Pi_-$, and the bar is an automorphism; under right multiplication by $-i\vec e_z$ they are the two eigenspaces, $-1$ and $+1$.

**The mixedness.** $N\bigl(\tfrac12(e_t+i\vec r)\bigr)=\tfrac14(1-\lvert\vec r\rvert^{2})$ and $S^{2}=S-N(S)e_t$: the norm is the failure of a state to be pure, and it vanishes exactly on the idempotents.

**The family.** One plane, two ideals and one pair per axis; the axes form the unit sphere and the pairs the real projective plane, so the family is infinite and no member is canonical.

**The mass.** A mass term needs both ideals, because a term built from one vanishes identically; the mass is the coefficient of the pairing, not a property of either half.

## The Plane

**The idempotent.** For a unit real axis $\vec u$,

$$
\tilde\Pi_+(\vec u)=\tfrac12\bigl(e_t+i\vec u\bigr),
\qquad
\tilde\Pi_+^{2}=\tilde\Pi_+ .
$$

The square is a one-line computation: $(e_t+i\vec u)^{2}=e_t+2i\vec u-\vec u^{2}=2e_t+2i\vec u$, since $\vec u^{2}=-\lvert\vec u\rvert^{2}e_t=-e_t$, and half of that is the element again. The idempotent is not a matrix, not a column and not a choice of basis: it is one element of the algebra, named by one unit vector.

**The complement.** The companion element is

$$
\tilde\Pi_-(\vec u)=\tfrac12\bigl(e_t-i\vec u\bigr)=e_t-\tilde\Pi_+(\vec u),
\qquad
\tilde\Pi_+\tilde\Pi_-=0 .
$$

The product vanishes because the crossed terms cancel and the remaining square is $(e_t+i\vec u)(e_t-i\vec u)=e_t-\vec u^{2}=e_t-e_t=0$, and the product in quarters is $e_t-i\vec u+i\vec u+i^{2}\vec u^{2}=e_t+\vec u^{2}=e_t-e_t=0$. The pair is a Peirce basis: two idempotents, summing to the identity, with vanishing product. The algebra is the sum of the four corners they cut out.

**The plane.** The carrier is the complex line through the idempotent, taken as a real plane:

$$
\Sigma(\vec u)=\mathbb{C}\tilde\Pi_+(\vec u)=\mathbb{R}\bigl\{\tilde\Pi_+,\;i\tilde\Pi_+\bigr\},
\qquad
\dim_\mathbb{R}\Sigma=2,\quad \dim_\mathbb{C}\Sigma=1 .
$$

The two real dimensions are the idempotent and the idempotent multiplied by the central imaginary. Multiplication by $i$ stays inside, so the plane is a complex line; but multiplication by $i$ is central, so it is not an extra structure the plane has to be given.

**The action.** Left multiplication by the whole algebra,

$$
\varrho(X)=L_X,\qquad L_X(Y)=XY .
$$

The action is one-sided. This is the difference that matters and it is worth naming precisely: on the centre and on the vector part the algebra acted by conjugation, two factors, one on each side; here it acts by one factor on one side. A one-sided action is what a module is, and the spin-half carrier is the first carrier in the sequence that is a module rather than a subspace the adjoint action preserves.

**The half angle.** Two identities carry the whole spin content, and both follow from the defining property of the axis rather than from a computation with arrays:

$$
\vec u\,\tilde\Pi_+(\vec u)=\tfrac12\bigl(\vec u+i\vec u^{2}\bigr)=\tfrac12\bigl(\vec u-ie_t\bigr)=-i\,\tilde\Pi_+(\vec u),
\qquad
\tilde\Pi_+(\vec u)\,\vec u=-i\,\tilde\Pi_+(\vec u).
$$

The axis multiplies the idempotent by $-i$ from either side. Now let $\tilde u=\cos\tfrac\theta2e_t+\sin\tfrac\theta2\vec u$ be the rotor of angle $\theta$ about the same axis. Its action on the plane is

$$
\tilde u\,\tilde\Pi_+=\Bigl(\cos\tfrac\theta2-i\sin\tfrac\theta2\Bigr)\tilde\Pi_+=e^{-i\theta/2}\,\tilde\Pi_+ .
$$

The rotor multiplies the plane by a phase, and the phase is half the angle. Nothing was inserted to produce the half: it is the identity $\vec u\tilde\Pi_+=-i\tilde\Pi_+$ read once. A rotation of the axis by $\theta$ turns the plane by $\theta/2$, and the map from rotations to phases on the plane is two-to-one.

**The weights.** The generator of rotations about $\vec u$ is $A(\vec u)=\tfrac12\vec u$, and by the identity above it acts on the plane as the complex scalar $-\tfrac i2$. The plane is a complex line, so the operator has one complex eigenvalue, and on the two real dimensions the eigenvalues are that scalar and its conjugate:

$$
\operatorname{spec}\bigl(A(\vec u)\bigr)\big|_{\Sigma}=\{-\tfrac i2,+\tfrac i2\},
\qquad\text{weights}\quad\{+\tfrac12,-\tfrac12\}.
$$

The spin is the largest weight, $s=\tfrac12$, and the count $2s+1=2$ is the real dimension of the carrier. The three carriers of the algebra are exactly the three solutions of this count: $1$, $2$ and $3$ real dimensions give $s=0,\tfrac12,1$.

**The full turn.** At $\theta=2\pi$ the phase is $e^{-i\pi}=-1$, so the operator of a full turn is $-\mathrm{id}$ on the plane while it is $+\mathrm{id}$ on every four-vector. The coefficient is $(-1)^{2s}=-1$. This is the algebraic origin of the statement that a spinor needs two full turns to return to itself, and it is a statement about the action, not about a picture: the operator of $2\pi$ is minus the identity on the carrier and plus the identity on the vector sector, and those are two different operators of the same algebra.

**Verification.** With the axis $\vec e_z$ the residuals are: $\lVert\tilde\Pi_+^{2}-\tilde\Pi_+\rVert=0$; $\lVert\tilde\Pi_++\tilde\Pi_--e_t\rVert=0$; $\lVert\tilde\Pi_+\tilde\Pi_-\rVert=0$; the rank of $\{\tilde\Pi_+,i\tilde\Pi_+\}$ is $2$; $\lVert\vec u\tilde\Pi_++i\tilde\Pi_+\rVert=0$; the rotor identity holds to $0$ at $\theta=0.9$; and a full turn gives $\lVert\tilde u\tilde\Pi_++\tilde\Pi_+\rVert=8.7\times10^{-17}$. The last number is round-off, not a residual.

**What the plane is not.** The plane is not an ideal. It is a complex line inside the ideal, closed under multiplication by the axis and by every rotor about the axis, and not closed under multiplication by the rest of the algebra. The distinction between the line and the ideal is the distinction between the carrier and the first closure, and the next two sections are about that difference.

## Why the Plane Is Not a Carrier for the Group

**The failure.** Take $\vec u_2$ a unit axis orthogonal to $\vec u$. Then

$$
\vec u_2\,\tilde\Pi_+(\vec u)=\tfrac12\bigl(\vec u_2+i\vec u_2\vec u\bigr)=\tfrac12\bigl(\vec u_2-i\vec u_3\bigr),
$$

using $\vec u_2\vec u=-\vec u_3$ for the oriented triple. The result has a component along $\vec u_3$, which is not a complex multiple of $\tilde\Pi_+$ and not even in the span of $\tilde\Pi_+$ and $\vec u_2\tilde\Pi_+$ — the second statement needs the next section, the first is immediate. The distance from the image to the plane is

$$
\operatorname{dist}\bigl(\vec u_2\tilde\Pi_+,\Sigma(\vec u)\bigr)=\tfrac{\sqrt2}{2},
$$

computed as the residual of the best complex multiple: the image has a component $\tfrac12\vec u_2$ that no multiple of $\tfrac12(e_t+i\vec u)$ can reproduce, since a multiple of the idempotent has equal scalar and axis parts.

**The interpretation.** Left multiplication by a transverse axis moves the plane out of itself. The plane is therefore invariant under the circle of rotations about its own axis and under nothing else. Read strictly, it is a carrier for that circle, and the statement that it is the carrier of spin $\tfrac12$ is a statement about the weights of that circle, not about invariance under the group.

**Why this is the one failure.** The centre is fixed by the adjoint action at every element, so it is invariant under the whole group and under more. The vector part is preserved by the adjoint action at every unit element, so it too is invariant. Only the plane fails, and it fails for a structural reason: it is built from an idempotent, an idempotent names an axis, and the group moves axes. A carrier built from a choice cannot be invariant under the group that undoes the choice.

**The repair.** The repair is to close the plane under the action: to take the smallest subspace that contains it and is preserved by left multiplication at every element. That subspace is the spinor space of the next section, and its dimension is four rather than two. The repair is forced, it is unique, and it costs the minimality of the plane: the closed object is no longer a line.

**The physics of the failure.** A preparation direction is not Lorentz invariant. If the plane is a state of a definite spin direction, then a boost tilts that direction, and the tilted state is not in the original plane. This is exactly what the informational sector reports in its own language: a boost is a Hermitian unit element, it acts on the state slice by the two-sided operator, and it carries a state off the slice. The algebraic statement and the physical statement are the same statement: the object that a rotation about one axis preserves, a boost about another axis destroys.

## The First Closure: The Spinor Space

**The subspace.** The smallest real subspace that contains the plane and is preserved by left multiplication at every element of the algebra is

$$
S_+(\vec u)=\mathbb{B}\,\tilde\Pi_+(\vec u)=\mathbb{C}\bigl\{\tilde\Pi_+,\;\vec u_2\tilde\Pi_+\bigr\},
\qquad
\dim_\mathbb{R}S_+=4,\quad \dim_\mathbb{C}S_+=2 .
$$

**Why those two vectors span it.** Expand a general element in the orthonormal quadruple $e_t,\vec u,\vec u_2,\vec u_3$: $\tilde Q=Q_te_t+Q_1\vec u+Q_2\vec u_2+Q_3\vec u_3$. On the right every unit meets $\tilde\Pi_+$, and the four products are fixed by the multiplication of the pure units:

$$
e_t\tilde\Pi_+=\tilde\Pi_+,\qquad
\vec u\tilde\Pi_+=-i\tilde\Pi_+,\qquad
\vec u_2\tilde\Pi_+=\tfrac12\bigl(\vec u_2-i\vec u_3\bigr),\qquad
\vec u_3\tilde\Pi_+=\tfrac12\bigl(\vec u_3+i\vec u_2\bigr).
$$

The first two are multiples of the idempotent; the last two are $\vec u_2\tilde\Pi_+$ and $i\vec u_2\tilde\Pi_+$ respectively, since $i\vec u_2\tilde\Pi_+=\tfrac12(i\vec u_2+\vec u_3)$ — the same element. So the image of the whole algebra is the complex span of two vectors, and the complex dimension is two.

**What the closure adds.** Not the complex structure: the plane was already a complex line and multiplication by $i$ acted inside it. The closure adds the transverse direction $\vec u_2$, which is two real dimensions on top of the two of the plane. The natural guess is that a spinor space is a complex line taken twice or a plane given an imaginary unit; both guesses are wrong, and the statement is worth the care because everything downstream depends on it.

**Closure.** For $Y\in S_+$ and any $X$, the product $XY$ lies in $S_+$ because $Y=Z\tilde\Pi_+$ gives $XY=(XZ)\tilde\Pi_+$. The verification is a residual of $1.1\times10^{-15}$ on random pairs. The map $X\mapsto X\tilde\Pi_+$ is a projection of the algebra onto the ideal, $\bigl(X\tilde\Pi_+\bigr)\tilde\Pi_+=X\tilde\Pi_+$ to $0$: the idempotent projects, and the projection is the algebra's own operation and not an added rule.

**Minimality.** No nonzero left subspace of $S_+$ is preserved by the whole algebra. The argument is a dimension count with one input from the structure theory: the algebra is isomorphic to the full algebra of two-by-two complex matrices, its nonzero left ideals are the column ideals, and a column ideal has complex dimension two. A nonzero $Y\in S_+$ generates the left ideal $\mathbb{B}Y$, which is contained in $S_+$ because $S_+$ is a left ideal and contains $Y$; being nonzero it has complex dimension two; and $S_+$ also has complex dimension two, so the two coincide. Hence every nonzero element of the ideal generates the whole ideal, which is the definition of minimality.

**Nullity.** The norm is multiplicative and the idempotent has norm zero, so for every $X$

$$
N\bigl(X\tilde\Pi_+(\vec u)\bigr)=N(X)\,N\bigl(\tilde\Pi_+(\vec u)\bigr)=0 .
$$

The computation on the idempotent itself is the cancellation that names the case: the coordinates are $Q_t=\tfrac12$ and $Q_k=\tfrac i2u_k$, so the four squares are $\tfrac14$ and three copies of $-\tfrac14u_k^{2}$, and the unit length of the axis makes them sum to zero.

**Total isotropy and maximality.** The polar form vanishes on $S_+\times S_+$ because all three terms of $\tfrac12\bigl(N(X+Y)-N(X)-N(Y)\bigr)$ vanish when $X$ and $Y$ are both in $S_+$. So the ideal is totally isotropic. It is also maximal: an isotropic subspace of a nondegenerate form of complex dimension four has complex dimension at most two, by $W\subseteq W^{\perp}$ and $\dim W^{\perp}=4-\dim W$, and $S_+$ attains the bound. The plane, by contrast, is isotropic of complex dimension one and is not maximal.

**The interpretation.** A field with values in $S_+$ is a two-component spinor in the only sense that matters: two complex numbers, acted on irreducibly by the algebra, with the group of unit elements acting by left multiplication. The algebra cannot see a difference between this ideal and any other, because it has one simple module; the axis chooses the realisation and not the module.

**Why the closure is canonical and the plane is not.** The plane is a choice; the ideal is what the choice generates once the whole algebra is allowed to act. So the carrier is a choice and the closure is a consequence. That inversion is the content of the phrase *the plane is the carrier and the ideal is its closure*: the object physics calls a spinor is the consequence, not the choice.

## The Second Closure: The Bispinor Space

**The splitting.** The complementary idempotent gives a second ideal of the same dimension, and the two are complementary:

$$
X=X\tilde\Pi_++X\tilde\Pi_-,\qquad
S_+(\vec u)\cap S_-(\vec u)=\{0\},\qquad
\mathbb{B}=S_+(\vec u)\oplus S_-(\vec u).
$$

The directness is one line. If $X$ lies in both, then $X=X\tilde\Pi_+$ and $X=X\tilde\Pi_-$, so $X=X\tilde\Pi_+\tilde\Pi_-=0$ using the vanishing product of the idempotents. The sum is the whole algebra because $\tilde\Pi_++\tilde\Pi_-=e_t$ and every element splits as $X=X\tilde\Pi_++X\tilde\Pi_-$. The rank of eight basis vectors taken four from each ideal is eight, verified; the intersection is zero, verified.

**As a set it is the algebra; as a decomposition it is not.** Each bispinor space is $\mathbb{B}$, so as sets the family has one member. What varies from axis to axis is the splitting, and the two ideals are genuine proper subspaces that move with the axis. A bispinor space is therefore not a subspace of the algebra; it is the algebra together with a Peirce pair. The phrase that keeps this straight is that the object is the algebra *read through* the pair, and the entry uses that read throughout.

**The family.** The pair is unchanged when the axis is reversed, $\tilde\Pi_+(-\vec u)=\tilde\Pi_-(\vec u)$, so the unordered pair is indexed by the real projective plane and the ordered pair by the sphere. A rotation by $\pi$ about a transverse axis sends $\vec u$ to $-\vec u$ and exchanges the two idempotents; no element of the algebra sends one ideal to the other by left multiplication, since left multiplication preserves every ideal.

**The corners.** The four Peirce corners $\tilde\Pi_\epsilon\mathbb{B}\tilde\Pi_\delta$ have real dimension two each, and the two ideals are their grouping two by two: $S_+=\tilde\Pi_+\mathbb{B}\tilde\Pi_++\tilde\Pi_+\mathbb{B}\tilde\Pi_-$, and the same for $S_-$. Four corners of two and two ideals of four: the counts agree and the kinds do not, and the entry follows the source in refusing to identify them.

**The two steps are different in kind.** The first step repairs an invariance: the plane was not preserved by the group, the ideal is. The second step completes a pair: the ideal was one of two, and the algebra is their sum. The first is forced by the requirement that the carrier be a module for the group. The second is forced by nothing; it is the statement that a four-component object is available and that physics uses it.

**The physics of the two steps.** The first closure is the Weyl spinor: a field of two complex components that carries one chirality and one irreducible action. The second is the Dirac spinor: a field of four complex components that carries both chiralities and on which the mass operator can act. The dimension count of the physicist, two and four, is the complex dimension of the ideal and of the algebra. The algebra does not need the Dirac field; it contains it.

## The Two Numbers: the Norm and the Spectrum

**Two predicates, two failures.** An element carries two independent scalar invariants. The norm $N=Q_t^{2}+\lvert\vec Q\rvert^{2}$ is multiplicative and vanishes on the elements without an inverse; the square of the vector part $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ controls whether the two eigenvalues $Q_t\pm iB$ coincide. An element is norm-regular when $N\neq0$ and spectrally regular when $B^{2}\neq0$. On the carrier the first fails everywhere and the second fails only at the origin.

**The norm on the plane is zero.** By multiplicativity, $N(\lambda\tilde\Pi_+)=\lambda^{2}N(\tilde\Pi_+)=0$ for every complex $\lambda$; the residual over one hundred random values is $7.0\times10^{-16}$ and is round-off. The statement excludes nothing: every element of the plane, including every nonzero one, is norm-degenerate. The plane meets the null cone in its entirety.

**The norm is mixedness.** Let the axis be replaced by an arbitrary real vector $\vec r$ and put $S_{\vec r}=\tfrac12(e_t+i\vec r)$. This is the general element of the real three-dimensional ball of Hermitian elements of unit trace, which is the state slice of the informational sector. Its norm and its failure to be idempotent are the same quantity:

$$
N(S_{\vec r})=\tfrac14\bigl(1-\lvert\vec r\rvert^{2}\bigr),
\qquad
S_{\vec r}^{2}=S_{\vec r}-N(S_{\vec r})\,e_t .
$$

The first display is exact for every real $\vec r$ — residual $0$ over one hundred random draws, of length up to $1.2$ and hence beyond the sphere as well. The second follows from the quadratic relation $S^{2}-2Q_tS+N e_t=0$ with $Q_t=\tfrac12$. So the norm vanishes exactly on the sphere $\lvert\vec r\rvert=1$, which is exactly the set of idempotents, and it grows as the state moves inward. On the sphere it is zero; at the centre of the ball, where $S=\tfrac12e_t$, it is $\tfrac14$; and the identity $S^{2}=S-N$ says that a state is a projector exactly when its norm vanishes.

**The scope of the identity.** This is a statement about the Hermitian slice and not about the algebra. A general element is not of the form $S_{\vec r}$, its $Q_t$ is complex, and the norm is not a real measure of anything. The identity holds where the state slice is, and the entry restricts it there deliberately: the identification of the norm with a departure from purity uses the Hermiticity of the state, and it would be a mistake to carry it to a general element.

**The spectrum on the plane.** The square of the vector part is

$$
B^{2}\bigl(\lambda\tilde\Pi_+(\vec u)\bigr)
=\sum_k\Bigl(\tfrac i2\lambda u_k\Bigr)^{2}
=-\tfrac14\lambda^{2},
$$

because the three squares of the components of a unit vector sum to one. Residual $0$ over one hundred random $\lambda$. The factor $-\tfrac14$ is invertible, so the plane meets the degenerate cone only at $\lambda=0$: the plane is spectrally regular at every nonzero point, while its norm vanishes at every point. Its spectrum is

$$
\operatorname{spec}\bigl(\lambda\tilde\Pi_+(\vec u)\bigr)=\{0,\lambda\},
\qquad
\operatorname{spec}\bigl(\tilde\Pi_+(\vec u)\bigr)=\{0,1\},
$$

verified at $\lambda=0.7+0.2i$ and at the idempotent.

**The scaled idempotent.** The spectrum $\{0,\lambda\}$ has a second statement, shorter and stronger: every nonzero element of the plane satisfies

$$
X^{2}=\lambda X\qquad\text{for } X=\lambda\tilde\Pi_+(\vec u),
$$

residual $0$ over one hundred draws. So the plane is the set of rescaled idempotents: every element of the carrier is a nonzero complex multiple of a projector. The idempotent is the case $\lambda=1$, and the scale $\lambda$ is the amplitude. This is the sharpest statement of what the carrier is: not a set of projectors, but the projective line of one projector, which is the same set up to the scale that carries the amplitude.

**Inside the ideal.** Every element of $S_+$ has vanishing norm, so its two eigenvalues have vanishing product and one of them is zero:

$$
N(Y)=0,\qquad \operatorname{spec}\bigl(Y\bigr)=\{0,\,2Q_t(Y)\},
\qquad B^{2}(Y)=-Q_t(Y)^{2}.
$$

The last identity is the content: on the ideal the square of the vector part is minus the square of the scalar part, residual $4.6\times10^{-16}$ over one hundred random elements. So the spectral predicate on the ideal reads $Q_t\neq0$, and the degenerate elements are the ones with vanishing scalar coordinate. In the complex basis $\tilde\Pi_+,\vec u_2\tilde\Pi_+$ the scalar coordinate is the first coefficient, since $Q_t(\vec u_2\tilde\Pi_+)=0$, so the degenerate locus is

$$
S_+(\vec u)\cap\mathcal S=\mathbb{C}\bigl(\vec u_2-i\vec u_3\bigr),
\qquad \dim_\mathbb{R}=2,
$$

a real plane inside the ideal. Its generator is the element $\vec u_2-i\vec u_3$, which lies in $S_+$ — it is twice $\vec u_2\tilde\Pi_+$ — and which satisfies

$$
(\vec u_2-i\vec u_3)^{2}=0,
$$

residual $0$. The identity is not an accident of the generator: on a null ideal the quadratic relation reduces to $Y^{2}=2Q_t(Y)Y$, so $Y^{2}=0$ exactly when $Q_t(Y)=0$. The square-zero elements and the spectrally degenerate elements are the same set, and both are the plane $\mathbb{C}(\vec u_2-i\vec u_3)$.

**Two planes, not one.** The degenerate plane is not the carrier. The carrier is $\mathbb{C}\tilde\Pi_+$, spanned by an idempotent with $Q_t=\tfrac12$; the degenerate plane is $\mathbb{C}(\vec u_2-i\vec u_3)$, spanned by a square-zero element with $Q_t=0$. They meet only at the origin, and they move together with the axis without ever coinciding. A reader who conflates them loses the whole distinction between the carrier and its exceptional locus.

**The exceptional point.** The degenerate plane deserves the name used for it in the family: it is where the two eigenvalues coalesce, $0$ and $0$, where the element stops being a rescaled projector and becomes nilpotent, and where the two predicates fail together. In a one-parameter family crossing it, the spectrum closes and reopens, and the element at the crossing has no eigenvector to speak of — the algebraic statement of the coalescence is $Y^{2}=0$ with $Y\neq0$, which is exactly the statement that the spectrum has one value and the element is not a multiple of the identity.

**The residual table.**

| statement | residual |
| --- | --- |
| $N(\lambda\tilde\Pi_+)=0$ | $7.0\times10^{-16}$ |
| $N(S_{\vec r})=\tfrac14(1-\lvert\vec r\rvert^{2})$ | $0$ |
| $S_{\vec r}^{2}=S_{\vec r}-N(S_{\vec r})e_t$ | $0$ |
| $B^{2}(\lambda\tilde\Pi_+)=-\lambda^{2}/4$ | $0$ |
| $\operatorname{spec}(\lambda\tilde\Pi_+)=\{0,\lambda\}$ | exact |
| $X^{2}=\lambda X$ on the plane | $0$ |
| $B^{2}(Y)=-Q_t(Y)^{2}$ on $S_+$ | $4.6\times10^{-16}$ |
| $(\vec u_2-i\vec u_3)^{2}=0$ | $0$ |

## The Two Ideals and the Two Chiralities

**Two operators, two splits.** Two different maps separate the algebra into two halves of complex dimension two, and the entry keeps them apart because physics uses the words for both.

The first is the coefficient conjugation: the map that sends $i$ to $-i$ and leaves the four units alone. It is an algebra automorphism, since the structure constants of the algebra are real, and it acts on the idempotents by

$$
\overline{\tilde\Pi_+(\vec u)}=\tilde\Pi_-(\vec u),
\qquad
\overline{X\tilde\Pi_+(\vec u)}=\bar X\,\tilde\Pi_-(\vec u)\in S_-(\vec u),
$$

residuals $0$ and $0$ over one hundred draws. So the bar exchanges the two ideals and exchanges the two halves of every element. The star does not do this, and cannot: it is an antiautomorphism, so it turns a left multiple into a right multiple, and it fixes both idempotents rather than exchanging them, $\tilde\Pi_\pm^{*}=\tilde\Pi_\pm$ to $0$. The star preserves the set of idempotents and reverses the side; the bar exchanges the two ideals and keeps the side. A statement that requires crossing from one ideal to the other is a statement about the bar.

The second is right multiplication by the axis. Since $\tilde\Pi_\pm(\vec u)\vec u=\mp i\tilde\Pi_\pm(\vec u)$, every element of an ideal is an eigenvector of the operator

$$
\gamma(\vec u)=-iR_{\vec u},\qquad
\gamma(\vec u)\bigl|_{S_+}=-\mathrm{id},\qquad
\gamma(\vec u)\bigl|_{S_-}=+\mathrm{id}.
$$

The residuals are $0$ at the axis $\vec e_z$ and $1.1\times10^{-15}$ and $7.1\times10^{-16}$ at two tilted axes, so the identity holds axis by axis and is not an artefact of a frame. The two ideals are exactly the two eigenspaces of $\gamma(\vec u)$, and the splitting by the ideals is exactly the splitting by the chirality.

**The relation between the two splits.** At the axis $\vec e_z$ the operator $\gamma$ is the one the corpus calls the chirality operator, and its eigenspaces are the two values. So the two ideals *are* the two chiralities at that axis, and at any other axis they are the two chiralities of that axis. What varies is the name and not the object: the axis of the operator is the axis of the ideals, and the value is a frame-dependent label for a member of a family that the algebra already carries.

**The projections.** The maps $X\mapsto X\tilde\Pi_\pm$ are projections onto the two ideals. They are idempotent as maps, $\bigl(X\tilde\Pi_\pm\bigr)\tilde\Pi_\pm=X\tilde\Pi_\pm$ to $0$, and they annihilate each other's images, since $\tilde\Pi_+\tilde\Pi_-=0$. The sum of the two projections is the identity map on the algebra. In the physicist's notation these are the chiral projections $\psi\mapsto\psi P_\pm$, and the only difference from the textbook is that the projectors are elements of the algebra and the multiplication is the algebra's own.

**The correction that has to be stated.** The two ideals are not the two sectors. The star splits the algebra into the anti-Hermitian and Hermitian halves, and that split is a different pair of subspaces: an element of one sector is not a sum of parts of one sector, and the star does not preserve either ideal. Chirality is not the material-informational split, and the two decompositions share no part. The corpus states this as a standing correction and the entry repeats it because the temptation to read the two halves of a spinor as matter and information is strong and wrong.

**The interpretation.** A chiral field takes values in one ideal. The algebra acts on it irreducibly, the group of unit elements acts by left multiplication, and no operation inside the algebra moves it to the other ideal except the bar, which is not a symmetry of the action but a change of the coefficient field. In physical language, a left-handed field and a right-handed field are two fields and not two components of one, until something couples them.

**One-sidedness and the double cover.** The action on each ideal is faithful, because $-e_t$ acts as $-\mathrm{id}$ and $e_t$ acts as $+\mathrm{id}$: the two elements of the centre that the adjoint action cannot distinguish are distinguished here. So the carrier is a genuine module for the double cover and not for the Lorentz group. The two-sided operator on the vector sector has the kernel $\{\pm e_t\}$ and descends; the one-sided action on the ideal has the trivial kernel and does not. That difference is the whole content of the word *spinor*.

## The Mass as the Pairing

**The statement.** Let $X=X_++X_-$ be the splitting of an element along the two ideals. Then

$$
N(X)=2B(X_+,X_-),
$$

because the norm is quadratic, the cross term is twice the polar form, and the two pure terms vanish since each ideal is null. The residual over one hundred random pairs is $8.9\times10^{-16}$.

**What it says.** The invariant length of a bispinor is not a length of either half. It is the pairing of the two halves; it vanishes when either half vanishes, and it is nonzero exactly when the two halves pair nontrivially. The pairing is nondegenerate: if a fixed $X_+$ pairs to zero with every element of $S_-$, then it is zero, because $B(X_+,Y)=B(X_+,Y_-)$ for every $Y$ and $B$ is nondegenerate on the algebra. One hundred random trials found no counterexample; the proof is the argument of the source article.

**The interpretation: a single chirality has no invariant length.** Put $X_-=0$. Then $N(X)=0$ whatever $X_+$ is, and the statement is uniform: no element of one ideal is norm-regular. This is the algebraic fact behind every statement in the corpus about a mass term being odd in the value. A term built from one ideal alone cannot produce a nonzero invariant, because the invariant is the pairing and one factor is missing.

**The interpretation: the mass is the pairing.** In the Dirac pair of the archive the two equations are

$$
\tilde\nabla_\Phi\tilde\Xi_R=k_m\tilde\Xi_L,
\qquad
\bigl(\tilde\nabla_\Phi\bigr)^{\natural}\tilde\Xi_L=k_m\tilde\Xi_R,
$$

and the mass coefficient $k_m=mc/\hbar$ is the constant that relates the two components. The entry's statement and the equation's statement are the same statement in two notations: the operator acts inside one ideal, since it is an element and an element is a left multiplier, and the mass is the only term that ties the two ideals together. At $k_m=0$ the pair decouples into two independent equations, one for each chirality, and each is consistent on its own because the operator preserves the ideal. That is why a massless fermion can be described by a two-component field and a massive one cannot.

**The mass number is diagonal in the value.** The mass enters as the central scalar $k_m$, and a central scalar holds both slots, so it cannot move a value. In the projectors of the chirality operator,

$$
P_+(k_m\mathrm I)P_-=0\quad\text{for every }k_m .
$$

The norm says that a mass pairs the two closures; this says that the pairing does not move the value.

**The interpretation: gauge invariance of a mass.** A mass term that pairs the two ideals ties their two charges together, and the archive's selection rule is the statement of that tie: a bare Dirac mass is gauge invariant if and only if the two chiral charges are equal, and a chiral fermion is massless in the unbroken phase. The pairing is the algebraic reason the tie exists, and the entry reports the rule as the archive's and claims only the pairing for itself.

**The interpretation: why the pairing is symmetric.** The polar form $B$ is symmetric, so $B(X_+,X_-)=B(X_-,X_+)$ and the exchange of the two names changes nothing. There is no sign to track, and no antisymmetric structure enters the mass. The fermionic minus sign belongs to the action of a full turn and to the exchange of two particles, not to this pairing; the entry states that separation because the two are easy to conflate.

**Why the mass is not a fifth force and not a scalar.** The mass coefficient is central, so it commutes with everything and multiplies both ideals by the same number. It is a number and not an element of a sector: it does not sit in $\mathbb{B}_\Psi$, it does not sit in $\mathbb{B}_\Phi$, and no gauge field couples to it. The algebra gives the shape of the pairing and gives no value: $k_m$ is a parameter, and the entry states that as a boundary rather than as a gap.

## The Sector Question

**The four sectors.** The two predicates give four sectors: $\Sigma_{11}$ for norm-regular and spectrally regular, $\Sigma_{10}$ for norm-regular and spectrally degenerate, $\Sigma_{01}$ for norm-degenerate and spectrally regular, and $\Sigma_{00}$ for both degenerate. The carriers of the algebra sit one per sector and the fourth is empty, and the spin-half entry is where that bookkeeping becomes interesting because its carrier and its closures sit in different places.

**Where the plane sits.** The plane away from the origin is null and spectrally regular, so it lies in $\Sigma_{01}$, and it is the only carrier in that sector: the centre is in $\Sigma_{10}$, the vector part in $\Sigma_{11}$, and the plane in $\Sigma_{01}$. The three carriers cover three sectors, one each.

**Where the ideal sits.** Every element of an ideal is null, so the ideal lies in the union of $\Sigma_{01}$ and $\Sigma_{00}$ and nowhere else. A scan of one hundred random elements of $S_+$ found every one of them in $\Sigma_{01}$ and none elsewhere; the elements in $\Sigma_{00}$ are the degenerate plane, which is a set of measure zero inside the ideal. So the ideal is null throughout, spectrally regular almost everywhere, and degenerate exactly on the plane $\mathbb{C}(\vec u_2-i\vec u_3)$.

**The one place where the closure reaches the empty sector.** No carrier meets $\Sigma_{00}$ away from the origin: the centre is regular in the norm, the vector part is regular in both, and the plane is regular in the spectrum. The *closure* of the plane does meet it, on the degenerate plane of the ideal. That is the sharpest statement of the sector bookkeeping for spin one half: the carrier is the regular null plane, and the exceptional set is one closure away.

**Where the bispinor space sits.** The bispinor space is the whole algebra, so it meets all four sectors. The pairing gives it the sector $\Sigma_{11}$ on a generic element, since $N=2B(X_+,X_-)\neq0$ and $B^{2}\neq0$ for a generic pair; the degenerate elements are the complex cone $B^{2}=0$, of real dimension six, and the null elements are the union of the two ideals together with the further set where the pairing vanishes.

**The physics of the placement.** Within one chirality the norm says nothing at all and the spectrum says everything: the invariant length of a single Weyl field vanishes identically, while the spectrum $\{0,2Q_t\}$ distinguishes the generic element from the exceptional one. Within the bispinor the norm says everything: the mass is the pairing and the invariant length is nonzero exactly when the two halves pair. The sector bookkeeping is the formal shadow of that difference, and it is why the entry treats the two closures as two different physical objects and not as two sizes of the same object.

## The Plane Read as a State

**The idempotent is a projector and a state.** In the algebra an idempotent is a projection; in the informational sector the element $\tfrac12(e_t+i\vec r)$ with $\lvert\vec r\rvert\le1$ is a state, Hermitian, of unit trace. The two descriptions meet at the sphere: a state is a projector exactly when $\lvert\vec r\rvert=1$, and that is exactly where its norm vanishes. So the plane is a state, and the rest of the ball is not.

**The family of carriers is the sphere.** One axis gives one idempotent and one plane. All axes give all pure states: the set of axes is the unit sphere, the set of idempotents is the unit sphere, and the set of planes is the sphere as well, since a plane determines its axis. The two-to-one correspondence axis-to-pair is the antipodal identification: $\vec u$ and $-\vec u$ give the same pair of idempotents in the opposite order. So the family of carriers of spin one half is the Bloch sphere, and the projective plane of the pairs is the sphere with antipodes identified, which is the sphere of unoriented axes.

**The measurement is the Peirce basis.** The two idempotents of the axis satisfy

$$
\tilde\Pi_++\tilde\Pi_-=e_t,
\qquad
\tilde\Pi_+\tilde\Pi_-=0 .
$$

Read physically, the first is completeness: the two outcomes are exhaustive and their weights sum to one. The second is exclusivity: the two outcomes never both occur. A complete exclusive pair of outcomes is exactly what a two-outcome measurement is, so the Peirce basis of an axis *is* a Stern–Gerlach analyser along that axis, and the algebra supplies the analyser and the algebra supplies the arithmetic of the outcomes in the same two elements.

**The Born weight.** Let the analyser be $\tilde\Pi_\pm(\vec u)$ and the state $\tfrac12(e_t+i\vec r)$. The normalised pairing of the state with each outcome is

$$
p_\pm=\frac{\langle\tilde\Pi_\pm(\vec u),\tfrac12(e_t+i\vec r)\rangle_{*}}{\langle\tfrac12(e_t+i\vec r),e_t\rangle_{*}}
=\tfrac12\bigl(1\pm\vec u\cdot\vec r\bigr),
$$

which is the standard formula for a spin-$\tfrac12$ measurement along $\vec u$ of a state polarised along $\vec r$, and the two weights sum to one by the completeness of the pair. The formula is the archive's and is quoted, not derived here; what the entry adds is its place: the probability is the pairing of the state with an *element of the carrier's own basis*, and the carrier's axis is the analyser's axis.

**Amplitude and scale.** The plane is the projective line of one projector together with a complex scale, and the scale is the amplitude. A nonzero element of the plane is $\lambda\tilde\Pi_+$, with $\lambda$ a complex number; the state is the idempotent, and the square root of the state is the element. The complex scale is the phase of the field, and the phase is what the action multiplies by $e^{-i\theta/2}$. So the carrier holds the two things a spinor holds: a direction, which is the axis, and a phase, which is the scale.

**The field and the state.** The distinction that the entry keeps throughout is that the field is the element and the state is its image. The informational sector writes the image as $\tilde X\tilde X^{*}$ up to a positive factor, and records as an open question whether the phase of $\tilde X$ is physical. The carrier sits on the field side of that question: left multiplication acts on $\tilde X$ and not on $\tilde X\tilde X^{*}$, the mass pairs $\tilde X$ and not the image, and the double cover is visible on $\tilde X$ and invisible on the image. So the carrier of spin one half is a carrier of fields, and the state space is a separate object that the field maps onto.

**Why the algebra's norm is not the probability.** The algebraic norm vanishes on the pure states and is not positive anywhere; the Hermitian form $\langle X,X\rangle_{*}=\sum_\mu\lvert X_\mu\rvert^{2}$ is positive definite and supplies the normalisation. Two different objects, two different jobs. The entry uses $N$ for the multiplicativity, the nullity and the pairing, and the Hermitian form for the weights, and it never substitutes one for the other.

**The light cone.** The degenerate plane of the ideal has a physical name too. Its generator is the complex null vector $\vec u_2-i\vec u_3$, whose square vanishes, and the archive's celestial sphere is exactly the set of such directions up to scale: a massless element is a direction together with a phase, the direction a point of the sphere and the phase the little-group circle over it. Within one chirality the degenerate plane is the complex line over one such point. So the exceptional locus of the ideal is the spinor of a null direction, and the axis of the plane chooses which point of the chiral sphere it is.

**What the sphere does not carry.** The sphere of directions carries no scale and no dynamics: the norm that would give the scale vanishes on all of it, and a weight is a representation datum and not an equation. The same boundary applies here and the entry repeats it: the algebra gives the carrier, the weights, the pairing and the sectors, and gives no frequency and no momentum except through the elements that represent them.

## The Interpretations

1. **A spinor is the square root of a state.** The carrier is the projective line of a projector, so an element of the carrier is the amplitude of a pure state and the state is the projector it generates. The scale is the amplitude and the phase of the scale is the phase of the field. This is a reading of the algebra and not an added postulate: it is what $S^{2}=\lambda S$ and $\tilde X\tilde X^{*}$ say.

2. **The nullity of the carrier is purity, not pathology.** The norm vanishes on the plane because a projector has rank one in the two-dimensional representation, and the determinant of a rank-one matrix is zero. For a general state the same norm is $\tfrac14(1-\lvert\vec r\rvert^{2})$, so it measures the departure from purity. A carrier that lives entirely in the null cone is the exact image of the statement that its elements are pure.

3. **The half angle is the fermion sign.** The rotor acts as $e^{-i\theta/2}$ and a full turn as $-\mathrm{id}$. Nothing about this is a convention of sign: the factor of two is the map from the group of rotations to the phases on the carrier, and the minus sign at $2\pi$ is its kernel. Every statement about the double cover of the Lorentz group in the corpus is this one line read on a different carrier.

4. **The two ideals are the two spinor chiralities.** The eigenspaces of $-iR_{\vec u}$ are the two minimal left ideals of the axis, verified to $10^{-15}$ at three axes. A field valued in one ideal is a Weyl field; the projection $\psi\mapsto\psi\tilde\Pi_\pm$ is the chiral projection; and the fact that the operator is a right multiplication while the action is a left multiplication is why chirality and the action commute.

5. **Mass is the pairing of the two spinor chiralities.** The norm on the bispinor is $2B(X_+,X_-)$ and on a single ideal it is zero. So a mass term has to pair the two, and the archive's Dirac pair with the coefficient $k_m$ between the two components is that pairing written as an equation. A massless field can be one ideal; a massive field cannot.

6. **A mass term ties two charges.** A pairing of the two ideals ties their two charges together, which is the archive's selection rule: a bare Dirac mass needs equal charges and a chiral fermion is massless in the unbroken phase. The entry reads the rule as the shape of the pairing and not as a separate postulate.

7. **The axis is a frame and not a datum.** No element of the algebra singles out an axis, so no ideal, no chirality and no pair is canonical. A result proved at one axis holds at all of them, and the entry writes the axis as a parameter for exactly that reason. Where a name such as *left* or *third direction* appears, a frame has been declared and the entry declares it.

8. **The plane fails where the centre and the vector part do not.** The one carrier that is not invariant under the whole group is the one built from a choice. Read physically: a definite spin direction is preserved by rotations about itself and destroyed by a boost, which is the statement that a state is not a Lorentz invariant object but a frame-dependent one.

9. **The exceptional locus is the null spinor.** Inside one chirality the degenerate elements form the plane over $\vec u_2-i\vec u_3$, they are exactly the square-zero elements, and they are the direction datum of a massless element in the archive's celestial sphere. The carrier never meets them; the closure does.

10. **The sectors say which invariant is informative.** On the plane the norm is uniformly zero and the spectrum separates; on the bispinor the spectrum can degenerate and the norm separates. Which of the two scalars carries information is a property of the carrier and not of the element, and that is why the entry computes both everywhere.

11. **The two closures are two physical objects.** Two complex components are a Weyl field; four are a Dirac field. The algebra contains both, and the difference between them is not a size but a pair: the first is an ideal and the second is the algebra read through a Peirce basis. A theory that uses one ideal per chirality and a theory that uses the whole algebra are two theories of the same algebra, and the mass decides which one is available.

12. **What is not claimed.** No spin-statistics theorem: the minus sign of a full turn is established, and the antisymmetry of a two-particle state under exchange is a separate statement the corpus makes in its own article and does not derive here. No mass value: $k_m$ is a parameter. No derivation of the Born rule: the weight is quoted from the informational sector. No identification of chirality with the material-informational split: the entry states the correction. No claim that the infinity of the family is a problem: it is the statement that the algebra has no preferred frame.

## The Limits

**No dynamics.** Left multiplication by an element is not an equation of motion. The entry describes the carrier, the closures and the invariants; the operator that acts on a field, its square and its solutions belong to the Dirac articles. A reader who wants the propagator will not find it here, and the entry says so rather than sketching one.

**No mass value.** The pairing has the shape of a mass term and no number. The coefficient $k_m=mc/\hbar$ is a parameter, the algebra gives no equation that would fix it, and the mass spectrum of the framework is not a result of the carrier theory.

**No proof of minimality from first principles.** The minimality of the ideal is proved from the structure of the algebra as a full matrix algebra, which is an established result of the corpus and not re-derived here. The dimension count does the work and the matrix-algebra input is cited.

**No general element theory.** Everything stated about states is stated on the Hermitian slice: $Q_t$ real, $\vec r$ real, unit trace. A general element has complex coefficients, its norm is complex, and the identity $S^{2}=S-N$ has no interpretation as a departure from purity. The entry restricts the reading and marks the restriction.

**No identification of the two values with the two ideals outside a frame.** The ideals are the eigenspaces of the chirality operator at the axis of the operator, which is exact and frame-independent as a statement about a family. Which member is called left requires a frame, and the entry declares the frame when it uses the name.

**No quantum postulate.** The entries of the informational sector supply the weights and the state space, and the entry quotes them. Nothing here postulates a Hilbert space, a collapse or a probability rule.

**No claim about the shape of the family beyond its indexing.** Axes give planes, pairs and ideals; the sphere indexes the axes, the projective plane indexes the pairs, and the entry stops there. Whether the family should be read as a bundle with a connection is a question the corpus does not settle and this entry does not open.

## Summary

The carrier of spin one half is the plane $\Sigma(\vec u)=\mathbb{C}\tilde\Pi_+(\vec u)$, of real dimension two, generated by the idempotent of a unit real axis and acted on by left multiplication. The action is one-sided, the weights are $\pm\tfrac12$, $2s+1=2$ counts the real dimensions of the carrier, and a full turn acts as $-\mathrm{id}$.

The plane is invariant under the rotations about its own axis and under no others: a transverse axis sends the idempotent to $\tfrac12(\vec u_2-i\vec u_3)$, at distance $\sqrt2/2$ from the plane. The repair is the first closure, the minimal left ideal $S_+=\mathbb{B}\tilde\Pi_+$ of real dimension four, spanned by $\tilde\Pi_+$ and $\vec u_2\tilde\Pi_+$, closed under the whole algebra, with no smaller invariant left subspace, and totally isotropic and maximal. The completion is the second closure, $\mathbb{B}=S_+\oplus S_-$, which as a set is the algebra and as a decomposition is the algebra with a Peirce pair.

The norm vanishes on the plane and on each ideal; on the state slice it is $\tfrac14(1-\lvert\vec r\rvert^{2})$, which is the departure from purity, so the nullity of the carrier is the purity of its elements and $S^{2}=S-N e_t$ states it in one line. The spectrum separates instead: $B^{2}=-\lambda^{2}/4$ on the plane, $\operatorname{spec}(\lambda\tilde\Pi_+)=\{0,\lambda\}$, and every element of the plane is a rescaled projector. So the plane away from the origin is $\Sigma_{01}$ and it is the only carrier in that sector.

Inside one ideal every element is null, $\operatorname{spec}(Y)=\{0,2Q_t(Y)\}$, and the degenerate elements are the square-zero ones: they form the real plane $\mathbb{C}(\vec u_2-i\vec u_3)$, the exceptional locus of the closure and the spinor of a null direction.

The two ideals are the two spinor chiralities: they are the eigenspaces of $-iR_{\vec u}$, and the coefficient conjugation exchanges them and is an automorphism. On the bispinor space the norm becomes the pairing, $N(X_++X_-)=2B(X_+,X_-)$, nondegenerate: the invariant length of a spinor of one chirality is zero, and the mass is the pairing of the two. The carrier is one pure state and its amplitude; the family over all axes is the Bloch sphere; the Peirce pair is a complete exclusive two-outcome analyser; and the weight $\tfrac12(1\pm\vec u\cdot\vec r)$ is the pairing of the state with the analyser's own basis.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}$ | the biquaternion algebra, real, of dimension $8$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the units, $e_t$ the identity, $\vec e_k^{2}=-e_t$ |
| $\vec u$ | a unit real axis, the parameter of the family |
| $\vec u_2,\vec u_3$ | an oriented orthonormal pair completing the axis |
| $\theta$ | the rotation angle, twice the rotor angle |
| $\tilde\Pi_\pm(\vec u)=\tfrac12(e_t\pm i\vec u)$ | the two idempotents of the axis, a Peirce basis |
| $\Sigma(\vec u)=\mathbb{C}\tilde\Pi_+(\vec u)$ | the carrier, $\dim_\mathbb{R}=2$ |
| $S_\pm(\vec u)=\mathbb{B}\tilde\Pi_\pm(\vec u)$ | the first closure, $\dim_\mathbb{R}=4$ |
| $S_+\oplus S_-=\mathbb{B}$ | the second closure, the bispinor space, $\dim_\mathbb{R}=8$ |
| $L_X$, $R_X$ | left and right multiplication by $X$ |
| $\varrho$ | the representation $X\mapsto L_X$ on the carrier |
| $N$, $B$ | the norm $Q_t^{2}+\lvert\vec Q\rvert^{2}$ and its polar form |
| $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the square of the vector part, the spectral discriminant |
| $\Sigma_{ij}$ | the sector of norm-regularity $i$ and spectral regularity $j$ |
| $\gamma(\vec u)=-iR_{\vec u}$ | the chirality operator of the axis |
| $\bar{\cdot}$, ${}^{*}$ | coefficient conjugation (automorphism) and Hermitian conjugation (antiautomorphism) |
| $S_{\vec r}=\tfrac12(e_t+i\vec r)$ | a state of the informational sector, $\lvert\vec r\rvert\le1$ |
| $k_m=mc/\hbar$ | the mass coefficient of the Dirac pair |
| $\mathcal N$, $\mathcal S$ | the null cone and the spectral-degenerate cone |

## Further Reading

- [Introduction to the Spin-Half Bispinors Spaces](../articles_maths/the-spin-half-bispinor-spaces.html), for the plane, the two closures, the family and the corners.
- [The Spin-Half Bispinors and N Norm Regularity](../articles_maths/the-spin-half-bispinor-spaces-and-n-norm-regularity.html), for the nullity of the idempotent, the plane and the ideals, the isotropic dimension and the pairing.
- [The Spin-Half Bispinors and Spectral Regularity](../articles_maths/the-spin-half-bispinor-spaces-and-spectral-regularity.html), for the spectrum $\{0,\lambda\}$ and the degenerate plane of the ideal.
- [The Minimal Left Ideals of the Biquaternion Algebra](../articles_maths/the-minimal-left-ideals-of-the-biquaternion-algebra.html), for the idempotents, the minimality and the splitting.
- [The Peirce Basis of the Biquaternion Algebra](../articles_maths/the-peirce-basis-of-the-biquaternion-algebra.html), for the basis that parametrises the family.
- [The One-Sided Action and the Spin Representation](../articles_maths/the-one-sided-action-and-the-spin-representation.html), for the representation and its tensor square.
- [Introduction to the Spin-Zero Centre Subspace](the-spin-zero-centre-subspace.html), for the carrier whose action is trivial, whose spectrum degenerates and whose norm separates.
- [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html), for the module, the double cover and the one-sided action.
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), for the chiral pair in which the mass relates the two components.
- [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html), for the value decomposition, the mass selection rule and the correction that chirality is not the sector split.
- [States, Observables and the Born Weight](states-observables-and-the-born-weight.html), for the state slice, the Bloch ball and the Born weight.
- [Chirality and the Weyl Spinors](exercise-chirality-and-the-weyl-spinors.html), for the two-component equations of the massless limit.
- [The Celestial Sphere of the Null Cone — Null Directions, Chirality and the Phase](the-celestial-sphere-of-the-null-cone-null-directions-chirality-and-the-phase.html), for a massless element as a direction together with a phase.
- [Two Spin-Half Particles in Biquaternionic Form](two-spin-half-particles-in-biquaternionic-form.html), for the composite system and the exchange operator.
- [The Eigenspinor: the Lorentz Rotor as a Function of Proper Time](the-eigenspinor-the-lorentz-rotor-as-a-function-of-proper-time.html), for the rotor that acts on the carrier and the plane.

**The next entry.** *Introduction to the Spin-One Anti-Hermitian Subspace* takes the third carrier, the three-dimensional vector part, and completes the sequence that the centre began and the bispinor continued.
