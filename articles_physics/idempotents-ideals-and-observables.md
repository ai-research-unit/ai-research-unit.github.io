# __Idempotents, Ideals and Observables__

## Introduction

**This entry reads the third section of the mathematical category: the roots of $+1$ and of $0$, the idempotents, the nilpotents, the minimal left ideals and the Peirce decomposition.** Seven mathematics articles establish those objects.

**The section is where the algebra stops being a space and becomes a collection of subspaces with a product.** Everything before it describes one element; everything in this section describes a cut of the whole algebra by one element. The cut is made by an idempotent, and the pieces it produces are the pieces a measurement has.

**Two equations govern the section and they are the same equation with a different constant.**

$$
\tilde\Pi^{2}=\tilde\Pi,\qquad \tilde\Upsilon^{2}=0 .
$$

The first says an element is unchanged by being applied twice; the second says it is annihilated by being applied to itself. In matrix language the first is a projector and the second is a step down. Everything in this entry is a consequence of one of the two.

**The single idea is that a measurement is a cut of the algebra and not an operator on a state.** An idempotent splits the algebra into two ideals, the ideals are the two chiralities, the Peirce corners are the four blocks of the reading, and the nilpotents are what completes the cut into a basis. The entry states the mathematics of that cut and then reads it.

## The Source Table

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| the roots of zero, the reduction, the null cone, the nilpotents, the criterion, the nilpotent cone, index two, the conjugations, the matrix model | [The Square Roots of Zero and the Nilpotents of the Biquaternion Algebra](../articles_maths/the-square-roots-of-zero-and-the-nilpotents-of-the-biquaternion-algebra.html) |
| the roots of one, the trivial and non-trivial roots, the roots of minus one, the idempotents and their classification, the halving map, the families, the idempotents in the six subspaces | [The Square Roots of One and the Idempotents of the Biquaternion Algebra](../articles_maths/the-square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html) |
| the idempotents at an axis, the two ideals, minimality, the decomposition of the algebra, the lattice of left ideals, simplicity, the sphere of axes | [The Minimal Left Ideals of the Biquaternion Algebra](../articles_maths/the-minimal-left-ideals-of-the-biquaternion-algebra.html) |
| the Peirce decompositions, the biquaternion case, the corner rule, the two indices, the mixed components, the grading | [Peirce Decompositions of the Biquaternion Algebra](../articles_maths/the-peirce-decomposition-of-the-biquaternion-algebra.html) |
| the definition of a Peirce basis, its existence, its coordinates, the gauge, the dimensions | [The Peirce Basis of a Peirce Decomposition of the Biquaternion Algebra](../articles_maths/the-peirce-basis-of-the-biquaternion-algebra.html) |
| the companion corner, the two nilpotents at an axis, the multiplication table of the four corners, the Peirce coordinates, the Peirce functional | [The Companion Nilpotents of the Biquaternion Algebra](../articles_maths/the-companion-nilpotents-of-the-biquaternion-algebra.html) |
| the Peirce data of a root, the factorization theorem, its proof and uniqueness, the Peirce-diagonal reading, what is intrinsic and what is a choice | [The Special Decomposition of a Biquaternion under a Peirce Basis](../articles_maths/the-special-decomposition-of-a-biquaternion-under-a-peirce-basis.html) |

**The rows are the entry's order.** The two equations come first, then the ideals they cut, then the four-corner reading, then the basis that completes the reading, then the theorem that puts an arbitrary element into that basis.

## The Results in Brief

### The Roots of One and the Idempotents

**An idempotent is an element of square equal to itself.**

$$
\tilde\Pi^{2}=\tilde\Pi .
$$

The two trivial idempotents are $0$ and $e_t$. Two idempotents are **orthogonal** when their two products vanish, and a family is **complete** when in addition its members sum to $e_t$. An idempotent is **primitive** when it is not a sum of two nonzero orthogonal idempotents.

**Every root of $+1$ carries a complete orthogonal pair, and the root is their difference.**

$$
\tilde\Pi_{\pm}(\tilde Z)=\tfrac12\bigl(e_t\pm\tilde Z\bigr),\qquad \tilde\Pi_++\tilde\Pi_-=e_t,\qquad \tilde\Pi_+-\tilde\Pi_-=\tilde Z,\qquad \tilde\Pi_+\tilde\Pi_-=\tilde\Pi_-\tilde\Pi_+=0 .
$$

**The halving map is a bijection between the roots of $+1$ and the idempotents.** Every idempotent is the image of exactly one root, so the two vocabularies are one vocabulary.

**The idempotents fall into three families.**

| family | form | Hermitian | parameters |
| --- | --- | --- | --- |
| the trivial pair | $0$, $e_t$ | yes | none |
| the Hermitian non-trivial ones | $\tfrac12\bigl(e_t\pm i\vec u\bigr)$, $\vec u$ a real unit vector | yes | $S^{2}$ |
| the non-Hermitian ones | $\tfrac12\bigl(e_t+\vec\zeta+i\vec\zeta'\bigr)$ | no | four real |

**The standard pair is the one at an axis.** At $\vec u=\vec e_z$ the two idempotents are the diagonal matrix units, orthogonal, complete and primitive.

### The Roots of Zero and the Nilpotents

**A nilpotent is an element of vanishing square, and it is necessarily pure and isotropic.**

$$
\tilde\Upsilon^{2}=0\iff Q_t=0\ \text{and}\ (\vec Q,\vec Q)=0 .
$$

**The index is two and there is no other.** A vanishing cube already forces a vanishing square, so the powers of a nilpotent stop at the second.

**The nilpotents are a real four-dimensional cone in the vector subspace.**

$$
\tilde\Upsilon=r\bigl(\vec u_p+i\vec u_{p'}\bigr),\qquad r>0,\qquad \vec u_p\cdot\vec u_p=\vec u_{p'}\cdot\vec u_{p'}=1,\qquad \vec u_p\cdot\vec u_{p'}=0 .
$$

**The two real parts of a nilpotent are orthogonal and of equal length.** That is the whole content of the complex isotropy condition $(\vec Q,\vec Q)=0$, written in real coordinates.

**Every nilpotent is a zero divisor, and the star and the quaternion conjugation preserve nilpotency.**

### The Minimal Left Ideals

**An idempotent generates a left ideal.**

$$
S_{\pm}(\vec u)=\mathbb{B}\,\tilde\Pi_{\pm}(\vec u),\qquad S_{+}=\operatorname{span}_{\mathbb{C}}\bigl\{\tilde\Pi_+,\ \vec\Upsilon_{-+}\bigr\},\qquad S_{-}=\operatorname{span}_{\mathbb{C}}\bigl\{\tilde\Pi_-,\ \vec\Upsilon_{+-}\bigr\} .
$$

**Each is four real dimensions, two complex, and minimal.** It has no left subideal other than $0$ and itself, and every one of its nonzero elements generates it.

**The algebra is the direct sum of the two.**

$$
\mathbb{B}=S_{+}\oplus S_{-},\qquad 4+4=8\ \text{real},\qquad 2+2=4\ \text{complex} .
$$

**The two ideals are isomorphic as left modules and distinct as subspaces.** Right multiplication by the companion nilpotent carries one to the other.

**The lattice of left ideals is the lattice of subspaces of $\mathbb{C}^{2}$:** $0$, a projective line of minimal ideals, and $\mathbb{B}$. The algebra is simple, so its only two-sided ideals are $0$ and $\mathbb{B}$.

**All minimal left ideals have one type.** The unit real quaternions act transitively on the axes, so the axis is a parameter of the family and not a datum of the algebra.

### The Peirce Decomposition

**A complete orthogonal pair cuts the algebra into four corners.**

$$
\mathbb{B}_{st}=\tilde\Pi_s\mathbb{B}\tilde\Pi_t,\qquad \mathbb{B}=\mathbb{B}_{++}\oplus\mathbb{B}_{+-}\oplus\mathbb{B}_{-+}\oplus\mathbb{B}_{--} .
$$

**Each corner is a complex line**, and the diagonal ones carry canonical vectors, the two idempotents.

**The product follows the corner rule.**

$$
\mathbb{B}_{st}\mathbb{B}_{uv}\subseteq\delta_{tu}\mathbb{B}_{sv} .
$$

The right index of the first factor must equal the left index of the second. The mixed corners are square-zero and the diagonal ones are the two idempotent lines.

**The four lines are graded by parity.** With $A_0=\mathbb{B}_{++}\oplus\mathbb{B}_{--}$ and $A_1=\mathbb{B}_{+-}\oplus\mathbb{B}_{-+}$,

$$
A_0A_0\subseteq A_0,\qquad A_0A_1\subseteq A_1,\qquad A_1A_0\subseteq A_1,\qquad A_1A_1\subseteq A_0 ,
$$

and $A_0$ is the commutative algebra $\mathbb{C}\times\mathbb{C}$ with unit $e_t$.

**The decomposition gives the lines and nothing else.** It gives no element of a mixed line, no basis, no gauge and no spinor.

### The Peirce Basis

**One point in each mixed line completes the cut to a basis.**

$$
\mathcal{B}(\vec u)=\bigl(\tilde\Pi_+,\ \vec\Upsilon_{-+},\ \vec\Upsilon_{+-},\ \tilde\Pi_-\bigr),\qquad \vec\Upsilon_{-+}=\tfrac12\bigl(i\vec a+\vec b\bigr),\qquad \vec\Upsilon_{+-}=\tfrac12\bigl(i\vec a-\vec b\bigr) ,
$$

with $\vec a,\vec b$ unit real vectors completing $\vec u$ to a right-handed orthonormal triple.

**The four relations.**

$$
\vec\Upsilon_{-+}^{2}=\vec\Upsilon_{+-}^{2}=0,\qquad \vec\Upsilon_{-+}\vec\Upsilon_{+-}=\tilde\Pi_-,\qquad \vec\Upsilon_{+-}\vec\Upsilon_{-+}=\tilde\Pi_+ .
$$

**The whole basis has vanishing norm.** All four elements are rank-one in the matrix model, the norm is the determinant, so the Peirce basis lies entirely on the isotropic cone.

**The bases of one family form a torsor under a one-parameter complex gauge.**

$$
\vec\Upsilon'_{+-}=t^{-1}\vec\Upsilon_{+-},\qquad \vec\Upsilon'_{-+}=t\,\vec\Upsilon_{-+},\qquad t\in\mathbb{C}^{\times} ,
$$

two real parameters, and no basis of the family is distinguished.

### The Peirce Coordinates and the Functional

**Every element has a unique Peirce expansion.** At the axis $\vec e_z$,

$$
\tilde Q=\bigl(Q_t-iQ_z\bigr)\tilde\Pi_++\bigl(-iQ_x+Q_y\bigr)\vec\Upsilon_{-+}+\bigl(-iQ_x-Q_y\bigr)\vec\Upsilon_{+-}+\bigl(Q_t+iQ_z\bigr)\tilde\Pi_- .
$$

**The diagonal corners see the scalar part and the axial component; the mixed corners see the two transverse components.**

**The Peirce functional is the diagonal coefficient.**

$$
\tilde\Pi_+\tilde Q\tilde\Pi_+=\lambda(\tilde Q)\,\tilde\Pi_+,\qquad \lambda(\tilde Q)=Q_t-iQ_z .
$$

**It is complex-linear and it is not multiplicative.**

$$
\lambda(\vec e_x\vec e_y)=\lambda(\vec e_z)=-i,\qquad \lambda(\vec e_x)\lambda(\vec e_y)=0 .
$$

The failure is forced: a multiplicative functional onto $\mathbb{C}$ would have a nontrivial two-sided ideal as its kernel, and the algebra is simple.

**The product inside a corner ideal is governed by the functional alone.**

$$
a\tilde\Pi\cdot b\tilde\Pi=\lambda(b)\,a\tilde\Pi,\qquad [a\tilde\Pi,b\tilde\Pi]=\bigl(\lambda(b)a-\lambda(a)b\bigr)\tilde\Pi .
$$

### The Special Decomposition

**Every element factorises relative to any root, with two intrinsic numbers.**

$$
\boxed{\;\tilde Q=\tilde U\,\bigl(r e_t+s\tilde Z\bigr)\,\tilde V^{*},\qquad \tilde U,\tilde V\in\mathrm{U}(\mathbb{B}),\qquad r\ge s\ge0\;}
$$

**The middle factor is diagonal in the Peirce basis of the root,** with coefficients $r+s$ and $r-s$, which are the two singular values of $\tilde Q$.

**The numbers are intrinsic and the presentation is a choice.** For $r>s>0$ the two unitaries are unique up to the simultaneous right multiplication by $e^{i\theta_+}\tilde\Pi_++e^{i\theta_-}\tilde\Pi_-$; for $r=s>0$ the freedom is larger. The root, the Peirce basis and its gauge are all presentation.

## The Interpretations

### I.3.a — An Idempotent Is a Question Already Answered

**Read:** $\tilde\Pi^{2}=\tilde\Pi$ says that applying the thing to itself returns the thing. That is the algebraic shape of a settled answer: a proposition that, once affirmed, is affirmed again by the same affirmation.

**In the matrix image the reading is exact.** An idempotent is a rank-one projection, so it is a pure state and a projector of that state at once. The two roles are not analogous; they are the same element seen from the two sides of the module.

**The three faces of minimality are one face.** A rank-one matrix, a minimal left ideal, and a Peirce decomposition with four lines of dimension one are three descriptions of the same cut. A reader who needs one of them can use whichever is convenient, and the entry does not choose between them.

**The boundary.** The equation $\tilde\Pi^{2}=\tilde\Pi$ is relative to the plain product. With another of the four general products the same equation has a different solution set, and its idempotents are other objects. The entry uses the plain product throughout and says so where it matters.

### I.3.b — A Two-Outcome Measurement Is a Root of $+1$

**Read:** a Hermitian root of $+1$ is an observable with two eigenvalues, $+1$ and $-1$, and its halving map gives the two outcome states.

$$
\tilde Z\tilde\Pi_+=\tilde\Pi_+\tilde Z=\tilde\Pi_+,\qquad \tilde Z\tilde\Pi_-=\tilde\Pi_-\tilde Z=-\tilde\Pi_-,\qquad \tilde Z=\tilde\Pi_+-\tilde\Pi_- .
$$

**The observable, its two eigenvalues and its two outcomes are one object.** The root is the observable, the pair is the two outcomes, the difference of the pair is the root again. The halving map is a bijection, so nothing is lost in either direction: a measurement and its possible results determine one another.

**The family of non-trivial Hermitian roots is one observable for each point of $S^{2}$.** The eigenvalues never change; only the eigenbasis does. The axis of the measurement is a line, so the observable is an oriented axis, and the antipodal point is the same pair of projectors with the two outcomes exchanged.

**The boundary.** Not every observable is a root of $+1$. A general Hermitian element $h_te_t+i\vec h$ has eigenvalues $h_t\pm\lvert\vec h\rvert$ and is a root only when $h_t^2+\lvert\vec h\rvert^2=1$ and $h_t\vec h=0$. The section supplies the two-outcome observables and not the general ones; the general spectrum is the subject of the next entry.

### I.3.c — Only the Hermitian Idempotents Are States

**Read:** the state reading is confined to one of the three families, and the confinement is exact.

**The Hermitian non-trivial idempotents are the pure states.** They are the Bloch sphere: $\tfrac12(e_t+i\vec u)$ over the real unit vectors, normalised by $2\operatorname{Sc}\tilde\Pi=1$ and lying on the boundary of the positive cone. The mixed states are the interior of the ball and are not idempotent at all.

**The non-Hermitian idempotents are not states and lie in no remarkable subspace.** They are a four-real-parameter family with no orthogonality and no positivity, and their only role is that they classify the non-pure zero divisors: every non-pure zero divisor is a complex multiple of one of them.

**The consequence is a clean division of labour.** Hermitian idempotents are states; nilpotents are modes; non-Hermitian idempotents are neither, and they are the bookkeeping object that makes the zero-divisor set two families instead of one.

**The boundary.** The identification of idempotents with states uses the star, so it is a statement about the informational sector and not about the algebra. An idempotent read without the star is only a cut.

### I.3.d — Purity Is Being on the Cone

**Read:** a pure state has vanishing norm, and it is a zero divisor. That is one fact in three vocabularies.

**The computation is one line.** For $\tilde\Pi=\tfrac12(e_t+i\vec u)$ with $\vec u$ a real unit vector, the vector part is $\tfrac12i\vec u$, and since $(\vec u,\vec u)=\lvert\vec u\rvert^{2}=1$ for a real unit vector,

$$
B^2=\bigl(\tfrac12i\vec u,\tfrac12i\vec u\bigr)=\tfrac14i^{2}(\vec u,\vec u)=-\tfrac14,\qquad N(\tilde\Pi)=\tfrac14-\tfrac14=0 .
$$

So the pure states sit exactly on the $N$-cone, and the mixed states are the interior where $N>0$.

**The four words then coincide.** A pure state, a zero-entropy state, a zero-divisor state and a perfectly resolvable state are four names for one element. The von Neumann entropy is a monotone function of $\operatorname{Sc}(\tilde\Pi^{2}-\tilde\Pi)$, which vanishes exactly on the idempotents, and the Fisher information with respect to the Bloch radius diverges there.

**The same is true of the nilpotents, one level down.** A nilpotent is on the cone too, and it is the extreme case: a pure state is on the cone but is not nilpotent, while a nilpotent is on the cone and is annihilated by its own product.

**The boundary.** Being on the cone is necessary for purity and not sufficient for statehood. Nilpotents and non-Hermitian idempotents are on the cone as well. Purity is the conjunction of three conditions: idempotent, Hermitian, rank one.

### I.3.e — The Two Ideals Are the Two Chiralities

**Read:** a minimal left ideal is one chirality, and the pair of them is the algebra.

$$
\mathbb{B}=S_+\oplus S_-,\qquad S_{\pm}=\mathbb{B}\tilde\Pi_\pm .
$$

**Each ideal is closed under left multiplication and irreducible under it.** That is what makes it a carrier: an element acting on it cannot produce a smaller invariant subspace. In the matrix model the two ideals are the two columns, so the carrier is literally the space of spinors of one handedness.

**The two ideals are isomorphic and distinct.** A nonzero map of simple modules is an isomorphism, and right multiplication by the companion nilpotent provides one. So the two chiralities carry the same representation and are not the same subspace. This is why a chirality is a position in the algebra and not a label on a spinor.

**The algebra is simple, so there is no two-sided carrier.** Its only two-sided ideals are $0$ and $\mathbb{B}$, and $\mathbb{B}$ is reducible. Hence every carrier of the multiplication is a minimal left ideal, and the algebra is the sum of its carriers and is never one of them.

**The boundary.** The reading names the carrier and not what travels in it. A field, a particle and a mode are all things a carrier may hold; the algebra supplies the carrier and no dynamics, and the entry that puts a field in it must add the field equation.

### I.3.f — The Axis Is a Parameter and Not a Datum

**Read:** the minimal ideal depends on an axis, all axes give the same type, and the algebra does not choose one.

**The unit real quaternions act transitively on the axes,** carrying $\tfrac12(e_t+i\vec u)$ to $\tfrac12(e_t+i\vec u')$ and one ideal to the other. So the family of minimal ideals is one orbit, and the axis is a parameter with no algebraic privilege.

**The lattice explains why there are finitely many kinds.** The left ideals of the algebra are $0$, the minimal ones, and the algebra; the minimal ones form a projective line. There is no left ideal strictly between a minimal one and the whole algebra, which is the statement that the carrier cannot be refined.

**The physical reading is that a quantisation axis is a choice of frame and not a property of the system.** A spin direction is picked by the measurement, and every choice gives the same carrier type. A result that changes when the axis changes is a result about the frame.

**The boundary.** The transitivity is the transitivity of the *unit real* quaternions, so it is a statement about rotations of the axis and not about all units. And the axis does affect the weight string of a generator, which is a statement about the matrix in a basis and not about the ideal.

### I.3.g — The Peirce Corners Are the Four Blocks of a Reading

**Read:** cutting by one idempotent splits the algebra into two sides, and cutting by the pair splits it into four blocks: two diagonal and two mixed.

| corner | what it holds | the matrix image |
| --- | --- | --- |
| $\mathbb{B}_{++}$ | the part that is $\tilde\Pi_+$ on both sides | the upper-left entry |
| $\mathbb{B}_{--}$ | the part that is $\tilde\Pi_-$ on both sides | the lower-right entry |
| $\mathbb{B}_{+-}$ | the part that is $\tilde\Pi_+$ on the left and $\tilde\Pi_-$ on the right | the upper-right entry |
| $\mathbb{B}_{-+}$ | the part that is $\tilde\Pi_-$ on the left and $\tilde\Pi_+$ on the right | the lower-left entry |

**The two indices are the two answers.** The left index says which side the element is on when it acts; the right index says which side it is on when it is acted upon. An element of a diagonal corner has the same answer twice; an element of a mixed corner has two different answers.

**The corner rule is the arithmetic of that.** A product is non-zero only when the right index of the first factor matches the left index of the second, which is the statement that the two answers must agree before the two elements can be composed. In the matrix image it is the rule that a row index must meet a column index.

**The physical reading is the population-and-coherence split.** The diagonal corners are the populations and the mixed corners the coherences. Multiplying two coherences gives a population; multiplying a population by a coherence gives a coherence; multiplying two populations of different index gives zero. That is the arithmetic of interference, and the algebra imposes it with no extra input.

**The boundary.** The four corners are four complex lines of the algebra and not four numbers of a particular state. The names population and coherence belong to the reading of one element in one basis, and a change of root mixes them.

### I.3.h — The Corner Algebra Is Degenerate, and That Is Why a Chirality Has No Invertible

**Read:** inside one ideal the product collapses to a scalar.

$$
a\tilde\Pi\cdot b\tilde\Pi=\lambda(b)\,a\tilde\Pi,\qquad \lambda(\tilde Q)=Q_t-iQ_z .
$$

**So the ideal is not a subalgebra and has no invertible element of its own.** The unit of the algebra does not lie in either ideal; the closest thing is the idempotent, which is invertible only for the elements already in the ideal's own corner. Composing two elements of one chirality does not produce a third element of that chirality in any general way: it produces a multiple of the first, with the multiple fixed by the second.

**The functional $\lambda$ is the trace-like object of the cut and it is not multiplicative.** $\lambda(\vec e_x\vec e_y)=-i$ while $\lambda(\vec e_x)\lambda(\vec e_y)=0$. The failure is not an accident of the choice of axis: a multiplicative functional onto $\mathbb{C}$ would have a nontrivial two-sided ideal as its kernel, and the algebra has none.

**The physical reading is that a chirality carries no multiplicative charge.** A one-dimensional representation of the algebra would be the algebraic form of an additive label that multiplies when two objects compose. There is none, so no such label exists on a chirality; the algebra's simplicity forbids it. Whatever additive quantum numbers the physics carries are therefore not representations of this algebra on a line.

**The boundary.** $\lambda$ is complex-linear and it is a legitimate linear functional; only multiplicativity fails. A computation may use it freely as a linear map, and must not use it as a homomorphism. The trace of the matrix image is the same kind of object, and it fails in the same way.

### I.3.i — The Gauge of a Peirce Basis Is the Phase of the State Vector

**Read:** completing the cut to a basis needs one point in each mixed line, and the choice is free up to a complex parameter.

$$
\vec\Upsilon'_{+-}=t^{-1}\vec\Upsilon_{+-},\qquad \vec\Upsilon'_{-+}=t\,\vec\Upsilon_{-+},\qquad t\in\mathbb{C}^{\times} .
$$

**Two real parameters, of which one is a phase and one is a scale.** The modulus of $t$ rescales the two nilpotent directions reciprocally; the argument rotates them. The product normalisation $\vec\Upsilon_{+-}\vec\Upsilon_{-+}=\tilde\Pi_+$ fixes the product of the two scalings and leaves their ratio free.

**The physical reading is the ray freedom.** A state vector is defined up to a complex multiple, and here the multiple has a home: it is the freedom of the basis used to present the cut. The phase is unobservable because the basis is a choice, and the scale is unobservable because the normalisation is a convention.

**The bases form a torsor, so no basis is distinguished.** The set of bases of one family is a principal homogeneous space for $\mathbb{C}^{\times}$: the action is free and transitive, so there is no canonical point.

**The boundary.** This is one complex parameter and not the whole unitary freedom of the algebra. The larger freedom, in the special decomposition, is the pair of unitaries, and the two must not be confused: the gauge here moves the basis of a fixed cut, and the unitaries there move the element.

### I.3.j — The Nilpotent Is a Mode With No Rest Frame, and a Null Momentum Is Not a Nilpotent

**Read:** a nilpotent is pure and isotropic, so it has no scalar part and no length. It cannot be a frame, a scale or a mass.

**The two real parts are orthogonal and of equal length.** That is the whole geometry: a nilpotent is a pair of real vectors of the same length at right angles, $\tilde\Upsilon=r(\vec u_p+i\vec u_{p'})$. Such a pair has no invariant direction singled out, and the isotropic condition is exactly the statement that no rest frame can be erected on it.

**The physical reading is the massless mode.** A nilpotent squares to zero, so it is annihilated by its own action; it cannot mediate a mass, because a mass is a bijection between the two chiralities and a nilpotent is a one-way map. The mode is the object that a mass term is not.

**The null four-momentum is on the cone and is not a nilpotent.** A material element $\tilde R_\Phi=ir'_te_t+\vec r$ has $N=-(r'_t)^2+\lvert\vec r\rvert^2$, so the null momenta have vanishing norm and are zero divisors. A nilpotent needs $Q_t=0$ as well, that is $r'_t=0$, and then nullness forces $\vec r=0$: the only nilpotent of the material sector is zero. Every non-zero null momentum therefore lies in the zero-divisor set and outside the nilpotent cone, and a computation that identifies the two sets is wrong.

**The nilpotent cone is not the light cone.** The nilpotent cone is four real dimensions inside the vector subspace; the light cone of the material sector is three real dimensions inside a different slice. They meet on the pure material elements with vanishing scalar part, and that intersection is the only place where the two readings coincide.

**The boundary.** The mode reading gives the nilpotent no dynamics. It says that a square-zero element is a one-way step; it does not say what steps, and the differential, the supercharge and the lattice of rungs are the subject of the entry on the modules and of the archive article that treats them.

### I.3.k — The Peirce Basis Is Lightlike Throughout

**Read:** all four elements of a Peirce basis have vanishing norm.

$$
N(\tilde\Pi_+)=N(\tilde\Pi_-)=N(\vec\Upsilon_{-+})=N(\vec\Upsilon_{+-})=0 .
$$

**The reason is that each is rank one in the matrix image,** and the norm is the determinant. So the basis of a measurement is a basis of the null cone: four lightlike vectors that together span the algebra.

**This is why the corner rule is so rigid.** A basis of definite-length vectors could not have the property that two of its members multiply to a third. Here every member is null, the products are either zero or another null member, and the whole multiplication table stays on the cone.

**The physical reading is that the states of a measurement basis are all extremal.** A pure state is on the boundary of the positive cone, and a basis of pure states is a basis of the boundary. There is no "interior" element in the basis, and that is why a measurement basis cannot be reached by a small perturbation of its members without leaving orthogonality.

**The boundary.** The vanishing is the vanishing of the quaternionic norm and not of the Hermitian form. On the informational sector the Hermitian form is positive definite and the same elements have positive Hermitian norms. Two different normals, one statement about each.

### I.3.l — The Special Decomposition Is the Schmidt Form, and Its Two Numbers Are the Physics

**Read:** every element is a pair of unitaries acting on a diagonal middle factor, and the two diagonal numbers are intrinsic.

$$
\tilde Q=\tilde U\bigl(r e_t+s\tilde Z\bigr)\tilde V^{*},\qquad r+s=\sigma_1,\qquad r-s=\sigma_2 .
$$

**The two numbers do not depend on the root.** This is the theorem: $r$ and $s$ are the singular values, and every root gives the same pair. So the intrinsic data of the element is a pair of non-negative numbers with $r\ge s$, exactly as a two-level state has two eigenvalues and a matrix has two singular values.

**The root, the Peirce basis and its gauge are all presentation.** They do not enter the numbers, they enter only the way the middle factor is displayed. This is the cleanest statement in the category of what an element *is* and what is a choice of frame.

**The physical reading is a Schmidt decomposition.** A pair $(r,s)$ with $r\ge s\ge0$ is a pair of amplitudes; their ratio is a population ratio; their normalisation is a scale. The unitaries are the two changes of frame, and the root labels the basis in which the off-diagonal entries vanish.

**The uniqueness cases carry a warning.** For $r>s>0$ the two unitaries are unique only up to a simultaneous diagonal phase, and for $r=s>0$ the freedom is larger still, so a degenerate pair of singular values leaves the frame undetermined. An argument that reads a frame off an element with $r=s$ is reading a convention.

**The boundary.** The decomposition is a statement about one element and not about a state. It gives the singular values and no probability; turning $r/(r+s)$ into a probability needs the normalisation and the Born reading, which the next entries supply.

## The Limits

**The entry reads the cut and not the spectrum.** The spectral projectors of a general element, the eigenvalue pair and the semisimple–nilpotent split belong to the entry on the spectrum, which also reads the centraliser and the Jordan basis.

**The entry does not read what the ideals carry.** A module structure, a field, a representation of the Lorentz group on the carrier — each is a further datum, and the entry that supplies it must say so.

**Two readings are labelled and not proved.** The identification of the Hermitian idempotents with states and of the Hermitian roots with two-outcome observables uses the star and the Born pairing, and the pairing is a convention of the corpus. The non-Hermitian idempotents are given no physical name at all, and that is deliberate.

**The nilpotent is given no dynamics.** The mode reading is structural: it says what a square-zero element cannot be. The differential, the cohomology and the supercharge are interpretations of a further structure that this section does not contain.

## Summary

- Two equations govern the section: $\tilde\Pi^{2}=\tilde\Pi$ and $\tilde\Upsilon^{2}=0$.
- Every idempotent is one root of $+1$ halved, and the halving map is a bijection, so root and idempotent are one vocabulary.
- There are three families of idempotents: the trivial pair, the Hermitian ones over $S^{2}$, and a four-real-parameter non-Hermitian family.
- A nilpotent is pure and isotropic, of index two, and the nilpotents form a real four-dimensional cone.
- An idempotent generates a minimal left ideal of complex dimension two, and the algebra is the direct sum of the two ideals at an axis.
- The algebra is simple, so every carrier is a minimal left ideal and the algebra itself is never a carrier.
- The axis is a parameter, not a datum: all minimal left ideals have one type and the unit real quaternions are transitive on them.
- The Peirce corners are four complex lines obeying $\mathbb{B}_{st}\mathbb{B}_{uv}\subseteq\delta_{tu}\mathbb{B}_{sv}$, and they are graded by parity.
- The Peirce functional $\lambda(\tilde Q)=Q_t-iQ_z$ is linear and not multiplicative, and its failure is the simplicity of the algebra.
- The whole Peirce basis lies on the isotropic cone.
- A Peirce basis is fixed up to a one-parameter complex gauge, and the gauge is the ray freedom of the state vector.
- Every element factorises as $\tilde U(re_t+s\tilde Z)\tilde V^{*}$ with $r,s$ its singular values, independent of the root.
- The two-outcome observables are the Hermitian roots; the pure states are the Hermitian idempotents; the mixed states are neither.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde\Pi$ | an idempotent, $\tilde\Pi^{2}=\tilde\Pi$ |
| $\tilde\Upsilon$ | a nilpotent, $\tilde\Upsilon^{2}=0$ |
| $\tilde Z$ | a root of $+1$, $\tilde Z^{2}=e_t$ |
| $\tilde\Pi_\pm(\tilde Z)=\tfrac12(e_t\pm\tilde Z)$ | the idempotent pair of a root |
| $\vec u,\vec a,\vec b$ | real unit vectors, with $\vec u$ the axis and $\vec a,\vec b$ completing it |
| $\vec\Upsilon_{-+}=\tfrac12(i\vec a+\vec b)$, $\vec\Upsilon_{+-}=\tfrac12(i\vec a-\vec b)$ | the companion nilpotents |
| $S_{\pm}(\vec u)=\mathbb{B}\tilde\Pi_\pm(\vec u)$ | the minimal left ideals at the axis |
| $\mathbb{B}_{st}=\tilde\Pi_s\mathbb{B}\tilde\Pi_t$ | the four Peirce corners |
| $\mathcal{B}(\vec u)$ | the Peirce basis at the axis |
| $\lambda(\tilde Q)=Q_t-iQ_z$ | the Peirce functional |
| $A_0,A_1$ | the diagonal and mixed parts of the graded decomposition |
| $r\ge s\ge0$ | the two numbers of the special decomposition; $r+s$, $r-s$ are the singular values |

## Further Reading

**In the mathematics corpus.** The seven articles of the source table, and *The Lattice of Left Ideals* and *Simplicity* inside the third of them, which are used here in one paragraph each.

**In this category.** *The Modules: What the Algebra Acts On* takes the carrier that this entry constructs and asks what acts on it. *The Spectrum and the Two Modes* takes the idempotent pair of a general element, which this entry gives only for a root. *States, Observables and the Born Weight* reads the pairing that turns a pair of idempotents into a probability.

**The sources of this entry.** [The Biquaternion Vacuum as a Minimal Idempotent](the-biquaternion-vacuum-as-a-minimal-idempotent.html) reads one minimal idempotent as a one-mode vacuum. [The Vacuum and the Nilpotent Ladder](the-vacuum-and-the-nilpotent-ladder.html) is the long treatment of the nilpotent, with the ladder, the BRST complex and the excluded null momentum. [Decoherence as Idempotent Projection](decoherence-as-idempotent-projection.html) tests how far the projection reading of a channel can be pushed, and where it fails. The observable and state readings, with their boundaries, are stated here.
