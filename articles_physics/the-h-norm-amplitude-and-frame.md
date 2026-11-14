# __The H Norm: Amplitude and Frame__

## Introduction

**This entry reads the eighth section of the mathematical category: the polar decomposition of a biquaternion, and what its two factors are.**

**The question is what remains of an element when everything that can be moved is moved.** Multiplication on the left by one unitary and on the right by another is the largest motion of the algebra that a measure can be asked to ignore. Three of the four measures ignore a part of it. One ignores all of it, and that one is the Hermitian norm.

**The rule is one line.**

$$
\boxed{\;\tilde Q=\tilde Q_H\,\tilde Q_0,\qquad
\tilde Q_H=\bigl(\tilde Q\tilde Q^{*}\bigr)^{1/2}\ge0,\qquad
\tilde Q_0=\tilde Q_H^{+}\tilde Q\;}
$$

**The first factor is the amplitude and the second is the frame.** The amplitude is Hermitian positive semidefinite and lies in the informational sector. The frame is a partial isometry, and off the zero-divisor cone it is a $*$-unitary element. Both are functions of $\tilde Q$ alone, the pair is defined on the whole algebra including $0$, and it is unique once the two ideals of $\tilde Q$ are imposed.

**The single idea is that the H-norm *is* the amplitude, and the amplitude is exactly what the frame cannot change.** The Hermitian norm passes to $\tilde Q_H$ unchanged, and every $*$-unitary multiplication on either side leaves it alone. No other measure of the four does this. The plain and the quaternionic forms are not positive, so neither can be carried by a positive factor at all. The quaternionic form is multiplicative, and multiplicativity makes it change by the norms of the two unitaries instead of staying fixed. The Krein form is indefinite, and its isometry group is the indefinite unitary group, not the compact one.

**The second idea is that this is a theorem and not a convention.** The positive definite forms on the algebra invariant under both-sided $*$-unitary multiplication form a one-dimensional family. The bimodule is irreducible, so Schur's lemma leaves one form up to a scale, and $H$ is that form. The amplitude of the polar decomposition is therefore not one choice among many: it is the coordinate of the double coset that the largest compact group cannot move.

**The word *frame* is used twice in the corpus and the two uses must be kept apart.** A **change of frame** is a left multiplication $\tilde Q\mapsto\tilde U\tilde Q$ by a $*$-unitary element: it is the observer's passive move, and it rotates the amplitude by conjugation. The **frame of an element** is the second polar factor $\tilde Q_0$: it is the element's own orientation, and it is what the amplitude does not contain. A left multiplication changes the first and, in a definite sense, leaves the second fixed up to the same rotation. This entry uses *the frame* for $\tilde Q_0$ and *a change of frame* for the left action, and it states which is meant whenever the distinction matters.

**The H-pair is not the N-word.** The two-factor decomposition is defined everywhere and its second factor is a partial isometry. The four-factor word $r\exp(i\theta)\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ exists only off the null cone, where the second factor is $*$-unitary and the amplitude is positive definite. The refinement is the subject of the next entry. Here the general pair is the object, and the four factors are quoted only where a result needs them.

**The strongest objection is that the H-norm is the Euclidean norm on $\mathbb{C}^{4}$ and therefore carries no physics.** The objection is correct about the formula and wrong about the consequence. The norm is Euclidean, and that is exactly why it is the amplitude: a probability amplitude is an element of a Hilbert space, its norm is the square root of a sum of squared moduli, and the group that preserves that norm is the unitary group and nothing larger. The physical content of $H$ is not the mass. It is the size of the state, and the reason the polar decomposition exists on the whole algebra rather than on the units.

**A second objection is that a decomposition that forgets the phase and the rotation cannot be physical, because those are the interesting parts.** The answer is that the two factors are not ranked. The amplitude answers what the element is and the frame answers how it is turned, and a theory needs both. What the decomposition proves is that the two questions have separate answers, and that the answer to the first is a positive element of the informational sector while the answer to the second is an element of the compact group.

## The Source Table

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| the two-factor decomposition, the Moore–Penrose inverse, the isometry factor, uniqueness by the four conditions, the invariants of the positive factor, the continuity of one factor and the discontinuity of the other, the six worked elements | [The Polar Decomposition of a Biquaternion](../articles_maths/the-polar-decomposition-of-a-biquaternion.html) |
| the positive cone, the uniqueness of the square root in the cone, the Cartan involution of the group of units | [Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint](../articles_maths/positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.html) |
| the two ideals of an element and the two orthogonal projections that generate them | [The Peirce Decomposition of the Biquaternion Algebra](../articles_maths/the-peirce-decomposition-of-the-biquaternion-algebra.html) |
| the minimal Hermitian idempotents, their normal form and their traces | [Hermitian Idempotents and the Peirce Decomposition](../articles_maths/hermitian-idempotents-and-the-peirce-decomposition.html) |
| the two spectral values of a Hermitian element and the criterion of positivity | [The Spectrum](../articles_maths/the-spectrum.html) |
| the four forms and the four algebraic norms, the Gram matrices and the definiteness of each | [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](../articles_maths/the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html) |
| the topological norm as the square root of the Hermitian norm and its uniqueness | [The Euclidean Topology of the Biquaternion Algebra](../articles_maths/the-euclidean-topology-of-the-biquaternion-algebra.html) |
| the restriction of the polar factors to the six remarkable subspaces | [The Polar Decomposition and Remarkable Subspaces](../articles_maths/the-polar-decomposition-and-remarkable-subspaces.html) |
| the positive definite refinement and its four factors, on the complement of the cone | [The Polar Decomposition of an N-Regular Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html) |
| the closed forms on the two sectors of the cone, where the second factor is rank one | [The Polar Decomposition of an N-Degenerate Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-degenerate-biquaternion.html) |

## The Results in Brief

- Every element has the pair $\tilde Q=\tilde Q_H\tilde Q_0$, with $\tilde Q_H$ Hermitian positive semidefinite and $\tilde Q_0$ a partial isometry; the pair is unique and exists at $0$.
- The amplitude is the closed element $\tilde Q_H=a e_t+i\vec W/(2a)$, with $2a^{2}=\langle\tilde Q\rangle_{*}+\lvert\langle\tilde Q\rangle_{\natural}\rvert$; it is the unique square root of $\tilde Q\tilde Q^{*}$ in the cone.
- The amplitude carries the whole H-norm and the modulus of the whole N-norm: $H(\tilde Q_H)=H(\tilde Q)$ and $N(\tilde Q_H)=\lvert N(\tilde Q)\rvert$, the second being real and non-negative.
- The frame carries the two ideals: $\tilde Q_0\tilde Q_0^{*}=\tilde\Pi_{\mathrm f}(\tilde Q)$ and $\tilde Q_0^{*}\tilde Q_0=\tilde\Pi_{\mathrm i}(\tilde Q)$.
- The H-norm is invariant under both-sided $*$-unitary multiplication, and the group of elements that leave it invariant is exactly the $*$-unitary group; $H$ is the only positive definite form with this property, up to a scale.
- Off the cone the frame has $H(\tilde Q_0)=1$; on the cone it has $H(\tilde Q_0)=\tfrac12$; in general $H(\tilde Q_0)$ is half the rank of the frame.
- The amplitude is continuous everywhere and the frame is discontinuous on the null cone and at the origin; no choice of Moore–Penrose inverse removes the jump.
- The amplitude is scale times boost and the frame is central phase times rotor, so the four-factor word splits $2+2$ between the two polar factors.
- Written through the rapidity, $H(\tilde Q)=\lvert N(\tilde Q)\rvert\cosh\Xi$ and the normalised state has Bloch vector of length $\tanh\Xi$.
- The H-norm is not multiplicative and not submultiplicative: $H(\tilde Q_1\tilde Q_2)\le2H(\tilde Q_1)H(\tilde Q_2)$, and the constant $2$ is attained.
- The H-norm is the only one of the four that adds across the two sectors, because the sectors are orthogonal for it and for no other.

## The Pair

**The decomposition is an ordered product, positive factor first.**

$$
\tilde Q=\tilde Q_H\tilde Q_0,\qquad
\tilde Q_H=\bigl(\tilde Q\tilde Q^{*}\bigr)^{1/2},\qquad
\tilde Q_0=\tilde Q_H^{+}\tilde Q .
$$

**The order is the opposite of the matrix polar decomposition and the difference is not cosmetic.** For a matrix the standard writing is $A=UP$ with $U$ an isometry on the left and $P$ positive on the right. The algebra's canonical pair puts the positive factor on the left, because the Hermitian square $\tilde Q\tilde Q^{*}$ is the invariant that the algebra supplies and it is a right-multiplication invariant. The factor that a right multiplication by a $*$-unitary cannot touch is therefore the left one.

**The closed form of the amplitude is an element, not a square root to be extracted.**

$$
\boxed{\;\tilde Q_H=a\,e_t+\frac{i}{2a}\,\vec W\quad(a>0),\qquad
\tilde Q_H=0\quad(\tilde Q=0)\;}
$$

with $a^{2}=\tfrac12\bigl(\langle\tilde Q\rangle_{*}+\lvert\langle\tilde Q\rangle_{\natural}\rvert\bigr)$ and $\vec W$ the real vector part of $\tilde Q\tilde Q^{*}$,

$$
\tilde Q\tilde Q^{*}=\langle\tilde Q\rangle_{*}\,e_t+i\vec W .
$$

**Two numbers and one direction carry the amplitude.** The scale $a$ and the length $\lvert\vec W\rvert$ are fixed by the two algebraic norms, and the direction of $\vec W$ is the axis of the amplitude's vector part. The vector part has length at most $a$, because $a^{2}-\lvert\vec W\rvert^{2}/(4a^{2})=\lvert N(\tilde Q)\rvert$, and that inequality is the positivity of the amplitude written as one line.

**The amplitude lies in the informational sector.** It is Hermitian, so it is an element of $\mathbb{B}_{\Psi}$, whatever sector $\tilde Q$ belonged to. This is the first structural fact of the entry: the polar decomposition is not a split of the element into two parts of the same kind. It is a split into a Hermitian part and a residual part, and the Hermitian part is the one the algebra's positivity is defined on.

**Uniqueness needs the two ideals and would not hold without them.** The pair is characterised by four conditions: $\tilde Q_H$ lies in the cone, $\tilde Q=\tilde Q_H\tilde Q_0$, $\tilde Q_0\tilde Q_0^{*}=\tilde\Pi_{\mathrm f}(\tilde Q)$, and $\tilde Q_H\mathbb{B}=\tilde Q\mathbb{B}$. The two counterexamples of the mathematical article are worth carrying, because each fails exactly one condition and both are built on the same null element $\tilde\Pi_{\vec u}$. With $\tilde Q_H'=e_t$ and $\tilde Q_0'=\tilde\Pi_{\vec u}$ the product is right but the amplitude generates the whole algebra rather than the line. With $\tilde Q_H'=\tilde\Pi_{\vec u}$ and $\tilde Q_0'=e_t$ the product is right and the amplitudes agree, but the frame is the identity and its final projection is not the line. The first counterexample fixes the amplitude by its ideal; the second fixes the frame by its projection.

**The two factors are continuous in different ways, and the difference is the physics.** The amplitude is continuous on the whole algebra. The frame is not: along a family that approaches the cone the frame tends to the identity, while its value on the cone is the rank-one projection onto the line. At the origin the frame falls to $0$ while its limit along $\tilde Q=\epsilon e_t$ is $e_t$.

## The Amplitude

**The amplitude carries the H-norm unchanged, and it carries the N-norm in modulus.**

$$
\boxed{\;H(\tilde Q_H)=H(\tilde Q),\qquad N(\tilde Q_H)=\bigl\lvert N(\tilde Q)\bigr\rvert\;}
$$

**The first identity is one line.** $\tilde Q_H$ is Hermitian and $\tilde Q_H^{2}=\tilde Q\tilde Q^{*}$, so

$$
H(\tilde Q_H)=\operatorname{Sc}\bigl(\tilde Q_H^{2}\bigr)=\operatorname{Sc}\bigl(\tilde Q\tilde Q^{*}\bigr)=H(\tilde Q).
$$

**The second identity uses multiplicativity and costs the phase.** $N(\tilde Q_H)^{2}=N(\tilde Q\tilde Q^{*})=N(\tilde Q)\overline{N(\tilde Q)}=\lvert N(\tilde Q)\rvert^{2}$, and the sign is fixed by the closed form, where $N(\tilde Q_H)=a^{2}-\lvert\vec W\rvert^{2}/(4a^{2})\ge0$.

**So the amplitude is the element with the same H-norm and a real non-negative N-norm.** Every nonzero element is carried by the decomposition to an element of the cone of positivity, at the price of the phase that $N$ loses. The two measures behave differently here, and the difference is the whole subject of the next two sections: one passes through the decomposition untouched, the other passes through as a modulus.

**The amplitude of the six worked elements is short enough to check by hand.**

| element $\tilde Q$ | $\tilde Q_H$ | $\tilde Q_0$ | $H(\tilde Q)$ | $H(\tilde Q_0)$ |
| --- | --- | --- | --- | --- |
| $e_t+\vec e_x$ | $\sqrt2\,e_t$ | $(e_t+\vec e_x)/\sqrt2$ | $2$ | $1$ |
| $e_t+\vec e_x+i\vec e_y$ | $\sqrt2\,e_t+\tfrac{i}{\sqrt2}(\vec e_y+\vec e_z)$ | $(e_t+\vec e_x)/\sqrt2$ | $3$ | $1$ |
| $e_t+i\vec e_x$ | $e_t+i\vec e_x$ | $(e_t+i\vec e_x)/2$ | $2$ | $\tfrac12$ |
| $\vec e_x+i\vec e_y$ | $e_t+i\vec e_z$ | $(\vec e_x+i\vec e_y)/2$ | $2$ | $\tfrac12$ |
| $(1+i)e_t$ | $\sqrt2\,e_t$ | $(1+i)e_t/\sqrt2$ | $2$ | $1$ |
| $0$ | $0$ | $0$ | $0$ | $0$ |

**Two lines of the table carry the distinction that the entry turns on.** The first and the fifth have the same amplitude $\sqrt2 e_t$ and different frames: a rotor and a phase. An amplitude cannot tell them apart, because both are units for $H$. The third and the fourth have rank-one frames and half the H-norm of a frame: they sit on the cone, and their frames are not units at all.

**The amplitude of the second element is worth reading once.** $\tilde Q=e_t+\vec e_x+i\vec e_y$ has $H=3$ and $N=1$, and its amplitude is $\sqrt2 e_t+i(\vec e_y+\vec e_z)/\sqrt2$, which is Hermitian, of H-norm $3$, and whose vector part has length $\sqrt2$. The two norms of the amplitude are $3$ and $1$, the same two numbers as those of the element. The frame is the rotor $(e_t+\vec e_x)/\sqrt2$, exactly the frame of the first element: the phase of the element went into the amplitude's vector part and the rotation stayed in the frame.

## The Frame

**The frame is a partial isometry, and a partial isometry is a projection written as an element.**

$$
\tilde Q_0\tilde Q_0^{*}\tilde Q_0=\tilde Q_0,\qquad
\tilde Q_0\tilde Q_0^{*}=\tilde\Pi_{\mathrm f}(\tilde Q),\qquad
\tilde Q_0^{*}\tilde Q_0=\tilde\Pi_{\mathrm i}(\tilde Q).
$$

**Two projections, one on each side, and they are the two ideals of $\tilde Q$.** The right ideal that $\tilde Q$ generates is the final projection; the left ideal is the initial one. Nothing of the size of $\tilde Q$ survives in either: a projection is an idempotent, and an idempotent has no scale.

**Off the cone both projections are the unit and the frame is $*$-unitary.** The $*$-unitary elements are the group $U(\mathbb{B})=\{\tilde U:\tilde U\tilde U^{*}=e_t\}$, which is isomorphic to $U(2)$ and has real dimension four. On the cone both projections are rank one and the frame is a rank-one partial isometry.

**The H-norm of the frame therefore takes three values and no others.**

| the frame | rank | $H(\tilde Q_0)$ | where |
| --- | --- | --- | --- |
| $*$-unitary | $2$ | $1$ | every element off the cone |
| rank-one partial isometry | $1$ | $\tfrac12$ | every nonzero element on the cone |
| $0$ | $0$ | $0$ | the origin |

**The pattern is $H(\tilde Q_0)=\tfrac12\operatorname{rank}\tilde Q_0$, because the trace of a projection is its rank.** In the algebra's convention the trace of the unit is $2$ and the trace of a minimal projection is $1$, so the H-norm of the frame is one half of an integer. This is the sharpest contrast with the amplitude: the amplitude's H-norm is an arbitrary positive real, and the frame's is $0$, $\tfrac12$ or $1$.

**The frame is where the two ideals live, and the amplitude is where the size lives.** The statement is a division of labour and not a metaphor: $\tilde Q_0$ determines and is determined by the pair of ideals, given the second factor's phase; and $\tilde Q_H$ determines and is determined by $\tilde Q\tilde Q^{*}$.

**A frame is not a phase.** A phase is an element of the centre, and the centre is one complex dimension. The frame is an element of $U(2)$, which is four real dimensions, and it does not commute with the amplitude in general. The distinction is the reason the decomposition has content: if the frame were a phase, the pair would be a rescaling and a rotation of the scalar, and no information about orientation would be carried.

**The frame is the part of the element that a right multiplication cannot remove and a left multiplication cannot create.** Right multiplication by a $*$-unitary is absorbed into the frame and leaves the amplitude alone. Left multiplication by a $*$-unitary moves the amplitude by conjugation and moves the frame by left multiplication. Neither operation changes the rank of the frame.

## The Modulus the Frame Cannot Change

**The invariance is two-sided and exact.**

$$
\boxed{\;H(\tilde U\tilde Q\tilde V)=H(\tilde Q)\quad(\tilde U,\tilde V\ *\text{-unitary})\;}
$$

**The proof is the definition read twice.** $(\tilde U\tilde Q\tilde V)(\tilde U\tilde Q\tilde V)^{*}=\tilde U\tilde Q\tilde V\tilde V^{*}\tilde Q^{*}\tilde U^{*}=\tilde U\tilde Q\tilde Q^{*}\tilde U^{*}$, and the trace of a unitary conjugate is the trace of the original. The scalar part is half the trace, so it is unchanged.

**The converse is the part that makes the norm canonical.** An element $\tilde V$ that preserves $H$ on the right for every $\tilde Q$ is $*$-unitary: if $\tilde Q\tilde V$ has the same H-norm as $\tilde Q$ for all $\tilde Q$, then $\tilde V\tilde V^{*}=e_t$. A numerical check on a hundred random non-unitary elements found a counterexample for every one of them, so the group of H-isometries is exactly $U(\mathbb{B})$ and not a larger group.

**The two-sided invariance is not shared.** Left multiplication by a $*$-unitary preserves $H$, and so does right multiplication, but the product of the two is the largest group that does. No other of the four measures is invariant under it, and the reason is the sign: the plain and the quaternionic forms are not positive, so a unitary motion can reverse them; the Krein form is indefinite, and the group that preserves it is $U(1,3)$.

**The invariance characterises the norm up to a scale.** The algebra is an irreducible module for the action of $U(\mathbb{B})\times U(\mathbb{B})$ by left and right multiplication, so any positive definite form invariant under that action is a scalar multiple of the trace form. This is Schur's lemma applied to a compact group, and it is the reason the entry can say *the* amplitude rather than *an* amplitude.

**The matrix picture makes the same statement in one line.** In $M_2(\mathbb{C})$ the Hermitian norm is half the squared Hilbert–Schmidt norm,

$$
2H(\tilde Q)=\operatorname{Tr}\bigl(\rho(\tilde Q)\rho(\tilde Q)^{*}\bigr)=\bigl\lVert\rho(\tilde Q)\bigr\rVert_{\mathrm{HS}}^{2},
$$

and the Hilbert–Schmidt norm of a matrix is invariant under left and right unitary multiplication by construction. The factor $2$ is the trace convention, $\operatorname{Tr}=2\operatorname{Sc}$, and it returns in the composition bound of a later section.

**The invariance is what makes the decomposition canonical, and the two facts are the same fact.** A pair $\tilde Q=\tilde Q_H\tilde Q_0$ with $\tilde Q_H$ in the cone and $\tilde Q_0$ unitary is a decomposition of the double coset $U(\mathbb{B})\backslash\mathbb{B}/U(\mathbb{B})$ into a positive representative and a group element. The amplitude is the positive representative and the frame is the group element. Changing the frame on the right moves the group element; changing the frame on the left conjugates the representative.

**The two transformations are worth writing side by side.**

$$
(\tilde U\tilde Q)_H=\tilde U\tilde Q_H\tilde U^{*},\qquad
(\tilde Q\tilde V)_H=\tilde Q_H .
$$

**A change of frame conjugates the amplitude and leaves it in the cone; a change of the element's own frame does not touch the amplitude at all.** The asymmetry is the precise sense in which the H-norm belongs to the amplitude: it is blind to the second factor and covariant under the first.

## The Frame on the Cone

**On the null cone the pair collapses to a projection and a rescaling.**

$$
\tilde Q_H=2a\,\tilde\Pi_{\vec u},\qquad
\tilde Q_0=\frac{\tilde Q}{2a},\qquad
\vec u=\frac{\vec W}{\lvert\vec W\rvert},\qquad
2a=\sqrt{2H(\tilde Q)} .
$$

**The amplitude is twice the scale times a minimal projection and the frame is the element divided by the same scale.** The frame is not a projection: it is a rank-one partial isometry with the element's own direction. Its final projection is $\tilde\Pi_{\vec u}$ and its initial projection is the corresponding projection on the other side.

**The two factors behave differently as the cone is approached.**

$$
\tilde Q_\epsilon=\sqrt{\tfrac{1+\epsilon^{2}}{2}}\,e_t+i\sqrt{\tfrac{1-\epsilon^{2}}{2}}\,\vec u,
\qquad
\tilde Q_H=\tilde Q_\epsilon,\qquad
\tilde Q_0=e_t\quad(\epsilon>0),
$$

and at $\epsilon=0$ the element is $\tfrac{1}{\sqrt2}(e_t+i\vec u)$, with $\tilde Q_H=\tilde Q$ and $\tilde Q_0=\tilde\Pi_{\vec u}$.

**The amplitude has a limit and the frame has a jump.** The amplitude's limit along the family is the element itself, which is Hermitian and positive semidefinite with one vanishing spectral value. The frame's limit is the identity, and its value is the projection. The two differ by exactly the rank, and the rank is not continuous.

**The jump is not an artefact of the formula.** The four conditions of uniqueness force the value on the cone: the frame must have final projection equal to the ideal that $\tilde Q$ generates, and on the cone that ideal is a line. Any pair satisfying the conditions agrees with the canonical pair, so no choice of Moore–Penrose inverse removes the discontinuity. The jump is the algebraic statement that a rank-one element generates a line and a full-rank element generates the algebra, and the two are not close.

**The origin is worse.** At $\tilde Q=0$ both factors vanish, while along $\tilde Q=\epsilon e_t$ the amplitude is $\epsilon e_t$ and the frame is $e_t$. The frame jumps from $e_t$ to $0$, which is the collapse of the rank from two to zero in one step.

**The half-norm of the frame on the cone is a physical number and not a curiosity.** A minimal projection has H-norm $\tfrac12$, so an element on the cone has a frame whose norm is half of the norm of a unit. The missing half is the second rank, and it is the same half that appears in the purity of a pure state.

## The Operator-to-State Map

**Every nonzero element defines a state, and the definition is the amplitude normalised.**

$$
\boxed{\;\tilde\varpi_Q=\frac{\tilde Q\tilde Q^{*}}{2H(\tilde Q)}=\frac{\tilde Q_H^{2}}{2H(\tilde Q)}\;}
$$

**The image is Hermitian, positive semidefinite and of trace one.** $\operatorname{Tr}\tilde\varpi_Q=\operatorname{Tr}(\tilde Q\tilde Q^{*})/(2H)=2H/(2H)=1$, and the positivity is the positivity of the Hermitian square. So the image is a state of the informational sector, of the form $\tfrac12(e_t+i\vec r)$ with $\lvert\vec r\rvert\le1$.

**The map forgets the frame and the scale, in that order.** A right multiplication by a $*$-unitary leaves the image alone, because $\tilde V\tilde V^{*}=e_t$. A multiplication by a nonzero complex scalar leaves it alone, because the numerator and the denominator carry the same factor. A left multiplication by a $*$-unitary conjugates the image, because it conjugates the amplitude.

**The image depends on the amplitude through its singular values only.**

$$
\tilde\varpi_Q=\tilde U_{\mathrm{s}}\operatorname{diag}(p_1,p_2)\tilde U_{\mathrm{s}}^{*},\qquad
p_i=\frac{\sigma_i^{2}}{\sigma_1^{2}+\sigma_2^{2}},\qquad p_1+p_2=1 ,
$$

with $\sigma_1\ge\sigma_2\ge0$ the two singular values of $\tilde Q$. The state is the normalised distribution of the squared singular values, which is the same statement as: the state is the amplitude with its scale removed, conjugated into the frame that diagonalises it.

**Written through the rapidity, the state is the boost.**

$$
\tilde\varpi_Q=\tfrac12\bigl(e_t+i\tanh\Xi\ \vec u_{\mathrm b}\bigr),
$$

with $\Xi$ the rapidity of the boost factor and $\vec u_{\mathrm b}$ its axis. The phase, the rotor angle and the rotor axis do not appear, and neither does the scale. Three of the four factors of the polar word leave no trace in the state; the fourth is the state.

**The purity is a function of the rapidity alone.**

$$
\operatorname{Tr}\tilde\varpi_Q^{2}=1-\frac{\lvert N(\tilde Q)\rvert^{2}}{2H(\tilde Q)^{2}}
=\frac{1+\tanh^{2}\Xi}{2},\qquad
\lvert\vec r\rvert=\tanh\Xi .
$$

**The two ends of the range are the two degenerations of the frame.** At $\Xi=0$ the state is maximally mixed, purity $\tfrac12$, and the element is a central phase times a real quaternion: no boost, two equal singular values, a frame of full rank. As $\Xi\to\infty$ the state becomes pure, purity $1$, and the element approaches the cone: infinite boost, one singular value zero, a frame of rank one.

**The map is therefore the statement that a pure state is a degenerate amplitude and a mixed state is a boosted one.** This is the backward-feeling half of the correspondence, and it is forced by the formulas: purity is rank deficiency, and rank deficiency is what the cone means.
