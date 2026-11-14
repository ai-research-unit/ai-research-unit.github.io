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

## The Two Singular Values

**The amplitude is a pair of numbers and not one.** The Hermitian square $\tilde Q\tilde Q^{*}$ has two spectral values, and they are non-negative because the element is positive semidefinite. Their square roots are the two singular values.

$$
\sigma_1^{2}=\lambda_1\bigl(\tilde Q\tilde Q^{*}\bigr),\qquad
\sigma_2^{2}=\lambda_2\bigl(\tilde Q\tilde Q^{*}\bigr),\qquad
\sigma_1\ge\sigma_2\ge0 .
$$

**Both algebraic norms are symmetric functions of the pair, and they are the two elementary ones.**

$$
\boxed{\;2H(\tilde Q)=\sigma_1^{2}+\sigma_2^{2},\qquad
\bigl\lvert N(\tilde Q)\bigr\rvert=\sigma_1\sigma_2,\qquad
H(\tilde Q)-\bigl\lvert N(\tilde Q)\bigr\rvert=\frac{(\sigma_1-\sigma_2)^{2}}{2}\;}
$$

**The first is the trace of the Hermitian square read through the convention $\operatorname{Tr}=2\operatorname{Sc}$.** The second is the product of its spectral values, which is its quaternionic norm, and the third is the arithmetic–geometric gap written in the algebra's units. A numerical check on a hundred random elements confirmed all three to ten digits.

**The third identity is the reason the entry can be written at all.** It says that the difference between the amplitude and the mass is not a matter of taste but the square of the spread of the two singular values. An element whose two singular values are equal has $H=\lvert N\rvert$ and no other difference exists. An element whose singular values are far apart has a large amplitude relative to its mass, and the excess is quadratic in the spread.

**The two singular values are the parameters of the double coset.**

$$
\tilde Q=\tilde U_{\mathrm s}\operatorname{diag}(\sigma_1,\sigma_2)\tilde U_{\mathrm s}' ,
$$

with the diagonal pair invariant under no further $*$-unitary motion except the swap. The pair $(\sigma_1,\sigma_2)$, unordered, is a complete invariant of the orbit under left and right unitary multiplication, and $H$ and $\lvert N\rvert$ determine it and are determined by it.

**The pair is a Doppler pair, and the algebra's own parametrisation shows it.**

$$
\sigma_1=r e^{\Xi/2},\qquad \sigma_2=r e^{-\Xi/2},\qquad r=\bigl\lvert N(\tilde Q)\bigr\rvert^{1/2},
$$

with $\Xi$ the rapidity of the boost factor. The geometric mean of the two amplitudes is the square root of the mass, the ratio is $e^{\Xi}$, and the logarithm of the ratio is the rapidity. In this reading the amplitude is an element with two mode amplitudes, the mass is what the two modes share, and the boost is what separates them.

| element | $H$ | $\lvert N\rvert$ | $\sigma_1$ | $\sigma_2$ | $\sqrt{\lvert N\rvert}$ | $\Xi$ | $\tanh\Xi$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $e_t+\vec e_x$ | $2$ | $2$ | $1.414$ | $1.414$ | $1.414$ | $0$ | $0$ |
| $e_t+\vec e_x+i\vec e_y$ | $3$ | $1$ | $2.414$ | $0.414$ | $1$ | $1.763$ | $0.943$ |
| $\sqrt2\,e_t+\vec e_x+i\vec e_y$ | $4$ | $2$ | $2.732$ | $0.732$ | $1.414$ | $1.317$ | $0.866$ |
| $e_t+i\vec e_x$ | $2$ | $0$ | $2$ | $0$ | $0$ | $\infty$ | $1$ |
| $(1+i)e_t$ | $2$ | $2$ | $1.414$ | $1.414$ | $1.414$ | $0$ | $0$ |

**The ratio of the two measures is the one datum that the scale cannot move.** It is $1/3$ in the second row and $1/2$ in the third, and $\cosh\Xi$ is $3$ and $2$ respectively. Doubling an element doubles $H$ and $\lvert N\rvert$ together and leaves the ratio, the rapidity and the state unchanged, so the two measures carry the scale and the boost separately while their ratio carries the boost alone.

## The Amplitude Against the Mass

**The two measures of one element are related by one factor, and the factor is the boost.**

$$
\boxed{\;H(\tilde Q)=\bigl\lvert N(\tilde Q)\bigr\rvert\cosh\Xi\;}
$$

**The identity follows from the last section in one line.** $2H=\sigma_1^{2}+\sigma_2^{2}=r^{2}(e^{\Xi}+e^{-\Xi})=2r^{2}\cosh\Xi$ and $\lvert N\rvert=r^{2}$. A check on a hundred elements built from the four-factor word confirmed it to ten digits.

**Three consequences follow, and each is a statement about what the two measures are for.** The amplitude is never smaller than the modulus of the interval, because $\cosh\Xi\ge1$. The two are equal exactly when the boost is absent, which is the case of a central phase times a real quaternion. And the ratio $H/\lvert N\rvert$ is the Lorentz factor of the element's boost.

**The amplitude is therefore the mass times the boost factor and not the mass.** This is the honest statement of what the polar decomposition adds to the interval. The interval answers how much invariant mass the element carries. The amplitude answers how much mass and motion together, and the extra is the boost. Any reading that identifies the amplitude with the mass will fail on the first element with a nonzero rapidity, and the table of the last section exhibits four of them.

**The same number appears in the state.** The Bloch length of $\tilde\varpi_Q$ is $\tanh\Xi$, so the state's departure from maximal mixing is the velocity of the boost and the amplitude's excess over the mass is the Lorentz factor of the same velocity. The two are one statement written twice, through the identity $\cosh\Xi=1/\sqrt{1-\tanh^{2}\Xi}$.

**The H-norm sees the scale and the boost and nothing else.**

$$
H(\tilde Q)=r^{2}\cosh\Xi,\qquad
\lvert N(\tilde Q)\rvert=r^{2},\qquad
H\bigl(e^{i\theta}\tilde Q\bigr)=H(\tilde Q),\qquad
H\bigl(\tilde Q\tilde u_{\mathrm r}\bigr)=H(\tilde Q).
$$

**The central phase, the rotor angle and both axes leave the amplitude alone.** The phase is removed by the modulus of $N$; the rotor is removed by the invariance; and the two axes enter only through the boost's magnitude. So the H-norm is a function of the scale and the rapidity and of nothing else, and the polar decomposition is the statement that everything else is carried by the frame.

**This is why the amplitude is the right object for a state and the wrong object for a charge.** A state is what survives when the phase and the rotation are discarded, and $H$ is exactly the measure that survives with them. A charge is what survives when the boost is discarded, and that is $\lvert N\rvert$. The two measures are the two halves of the same discard.

## What the H Norm Cannot Do

**The H-norm is not multiplicative.** The cleanest counterexample is an element of the null cone,

$$
\tilde Q=e_t+i\vec e_z=2\tilde\Pi_{\vec e_z},\qquad
\tilde Q^{2}=2\tilde Q,\qquad
H(\tilde Q)=2,\qquad
H\bigl(\tilde Q^{2}\bigr)=8 .
$$

**The square doubles the element and quadruples the norm, so the norm of the square is twice the square of the norm.** The mechanism is the cross term: $(\tilde Q_1+\tilde Q_2)^{2}$ carries $2\tilde Q_1\tilde Q_2$, and a norm built from moduli of coefficients has no way to cancel it.

**Composition is even worse than this example suggests, and the bound is two.**

$$
\boxed{\;\lVert\tilde Q_1\tilde Q_2\rVert_{\mathrm{HS}}\le\lVert\tilde Q_1\rVert_{\mathrm{HS}}\lVert\tilde Q_2\rVert_{\mathrm{HS}}
\quad\Longrightarrow\quad
H(\tilde Q_1\tilde Q_2)\le2H(\tilde Q_1)H(\tilde Q_2)\;}
$$

**The proof is the Hilbert–Schmidt inequality and the factor $2$ of the trace convention.** In the matrix picture $2H=\lVert\rho(\tilde Q)\rVert_{\mathrm{HS}}^{2}$, so submultiplicativity of the Hilbert–Schmidt norm gives $2H(\tilde Q_1\tilde Q_2)\le4H(\tilde Q_1)H(\tilde Q_2)$.

**The constant is attained, and the witness is short.** Take

$$
\tilde Q_1=(-1+i)\vec e_x+(-1-i)\vec e_y,\qquad
\tilde Q_2=e_t-i\vec e_z=2\tilde\Pi_{-\vec e_z},
$$

so that $H(\tilde Q_1)=4$, $H(\tilde Q_2)=2$, and $\tilde Q_1\tilde Q_2=(-2+2i)\vec e_x+(-2-2i)\vec e_y$ with $H=16$. The ratio is exactly $2$, and no larger ratio was found in a search over three hundred thousand pairs of small Gaussian-integer elements.

**The excess is the normalisation of a pure state.** The factor $2$ is $\tfrac{1}{H(\tilde\Pi_{\vec u})}$, because a minimal projection has H-norm $\tfrac12$. An amplitude is not an algebra norm; it is a norm that agrees with composition only up to the normalisation of the states it is made of.

**The H-norm is also blind to the sector.** $\tilde Q$ and $i\tilde Q$ have the same H-norm and lie in opposite sectors, so the norm cannot say which sector an element belongs to. The sector is a datum of the interval and of the Krein form, and it is invisible to the weight.

**And the H-norm does not determine the element.** The state map of an earlier section has five-dimensional fibres in an eight-dimensional algebra, so a state determines three numbers and an element needs eight. The missing five are the frame and the scale, and no function of $H$ and the state can recover them.

## The H Norm Among the Four

**The four measures of the previous entry are still four, and the polar decomposition uses exactly one of them.**

| measure | on the amplitude | on the frame | why |
| --- | --- | --- | --- |
| $P$ | complex, not positive | complex | not a real measure |
| $\lvert N\rvert$ | $\lvert N(\tilde Q)\rvert$ | $1$ or $0$ | multiplicative, loses the argument |
| $H$ | $H(\tilde Q)$ | $1$, $\tfrac12$ or $0$ | positive definite |
| $\mathrm{Kr}$ | signed | signed | indefinite |

**The weight is the only column that is a measure in the strict sense.** The pairing is complex, the interval is a modulus, and the volume is signed. A polar decomposition needs a positive factor, and only one of the four supplies positivity.

**The weight is also the only one that adds across the two sectors.** The material sector is spanned by the four real axes $ie_t,\vec e_x,\vec e_y,\vec e_z$ and the informational sector by the four axes $e_t,i\vec e_x,i\vec e_y,i\vec e_z$, so the two share no coordinate axis and the weight of a sum is the sum of the weights,

$$
H\bigl(\tilde R_{\Phi}+\tilde H_{\Psi}\bigr)=H\bigl(\tilde R_{\Phi}\bigr)+H\bigl(\tilde H_{\Psi}\bigr),
$$

while the interval of a sum carries the cross terms and the volume carries them with signs. A check on a hundred random pairs of one element from each sector confirmed the additive identity to ten digits.

**Additivity is the property a probability needs and the property a mass cannot have.** A measure that must add over independent alternatives has to be positive and diagonal in the coordinate splitting. The weight is the only candidate, and the polar decomposition is the operation that exposes its argument.

**The weight is the topological norm, and the other three are not.** The previous entry established that only one of the four is positive definite and that its square root is the norm of the topology. The polar decomposition is the place where that fact becomes structural: it is the only measure that can sit inside a positive square root and come out unchanged.

## The Interpretations

### I.8.a — What the Frame Cannot Change Is the Norm

**Read:** the amplitude carries the whole H-norm, $H(\tilde Q_H)=H(\tilde Q)$, and no $*$-unitary multiplication on either side changes it.

**A size that depends on orientation is not a size.** If a quantity fell when the element was rotated, it would be a component and not a magnitude, and no state could be normalised by it. The weight is the one measure of the four that is invariant under the largest compact motion, and that invariance is what makes it a magnitude rather than a coordinate.

**The physical interpretation is that the amplitude is a magnitude and the frame is a set of angles.** A magnitude and a set of angles are the two things a theory wants from a vector, and the polar decomposition is the theorem that says an element of this algebra has exactly those two and no third. The measure belongs to the magnitude, and the magnitude is the positive element that the decomposition exhibits.

**The boundary.** The reading does not say the frame is physically irrelevant. It says the frame is *what the measure cannot see*, which is a statement about the measure and not about the world.

### I.8.b — The Isometry Group Is the Unitary Group and Nothing Larger

**Read:** the elements that preserve $H$ on one side for every element are exactly the $*$-unitary ones, and among positive definite forms invariant under both sides $H$ is unique up to scale.

**A conservation law is a group, and the group is a small one.** The invariance of $H$ is the group $U(2)$, of real dimension four. If a larger group preserved it, the measure would be constant on larger orbits and would carry less; if a smaller one did, it would not be a scalar under a unitary rotation.

**The physical interpretation is that the amplitude is the unique scalar of the compact group.** Every function of the element invariant under both-sided unitary multiplication is a function of $H$. This is why the amplitude can be normalised once and for all, and why the frame can be discarded without loss of the magnitude.

**The boundary.** Uniqueness is up to a positive scale. The scale is fixed by the trace convention $\operatorname{Tr}(e_t)=2$, and that convention is a normalisation of the algebra and not a law of physics.

### I.8.c — What It Is and How It Is Oriented

**Read:** the amplitude is the scale times the boost, and the frame is the central phase times the rotor.

**The four-factor word splits two and two.** The scale and the rapidity are the amplitude's; the central phase and the rotor angle are the frame's; and the two axes go one to each. The decomposition is a partition of the word and not a partition of the element into large and small pieces.

**The physical interpretation is that magnitude and orientation are separate questions with separate answers.** An element's size and its boost answer what it is. Its phase and its rotation answer how it is turned. A theory that asks both questions needs both factors, and it must not expect either factor to answer the other's question.

**The boundary.** The split is not the split of the algebra into the two sectors. Both factors are complex elements. The amplitude happens to be Hermitian and the frame happens to be unitary, and neither fact follows from a sector assignment of the original element.

### I.8.d — The State Is the Boost

**Read:** $\tilde\varpi_Q=\tfrac12(e_t+i\tanh\Xi\,\vec u_{\mathrm b})$, with $\vec u_{\mathrm b}$ the boost axis and $\Xi$ its rapidity.

**The normalised amplitude is the boost and nothing else.** The scale cancels in the quotient, the central phase cancels because it is unitary on the right, and the rotor cancels because a real unit quaternion is unitary on the right. What survives is the boost, and the boost is a positive Hermitian element of trace one, with one spectral value possibly vanishing.

**The physical interpretation is that the mixedness of a state is the motion of the element that produced it.** A state's departure from maximal mixing is $\tanh\Xi$, the velocity of the boost in units where the cone is the speed of light. A pure state is an element on the light cone. A maximally mixed state is an element at rest.

**The boundary.** The statement uses the four-factor word and therefore the complement of the cone. On the cone it holds as a limit, $\tanh\Xi\to1$, and the limit is the pure state. At the origin the state is undefined.

### I.8.e — Pure Where the Frame Degenerates

**Read:** the purity is $1-\lvert N\rvert^{2}/(2H^{2})$, which is $1$ exactly when $N=0$, which is the cone; and on the cone the frame has rank one.

**Purity is rank deficiency.** The amplitude is a rank-two positive element off the cone and a rank-one element on it, and the state inherits the rank. The pure state is the degenerate case of the amplitude, not the generic one.

**The physical interpretation is that purity is a boundary condition and not a species of object.** A pure state is what an element becomes when it loses a rank. It is not a separate kind of element that happens to have no entropy. The entropy of the state measures how far the amplitude is from the boundary, and the boundary itself has measure zero in the algebra.

**The boundary.** The statement is about the amplitude of a single element and not about the reduced state of a composite. A reduced state can be mixed without any element being off the cone, and this reading does not apply to it.

### I.8.f — The Mass Is the Geometric Mean of the Two Squared Amplitudes

**Read:** $2H=\sigma_1^{2}+\sigma_2^{2}$, $\lvert N\rvert=\sigma_1\sigma_2$, and $H-\lvert N\rvert=(\sigma_1-\sigma_2)^{2}/2$.

**The two measures are the two means of one pair.** The weight is the arithmetic mean of the two squared singular values and the interval is their geometric mean, so the mass of an element is the geometric mean of the squares of its two amplitudes and the amplitude is their arithmetic mean. The inequality between the means is the inequality between the measures, and its equality case is the equality of the two amplitudes.

**The physical interpretation is that the mass is what the two modes share.** An element with two mode amplitudes has a mass that both contribute to multiplicatively and an amplitude that both contribute to additively. A boost makes one mode larger and the other smaller without changing what they share, and that is why the mass is boost invariant and the amplitude is not.

**The boundary.** The two modes are the two spectral values of $\tilde Q\tilde Q^{*}$. They are a decomposition of one element's amplitude and not a claim that the element is a pair of particles.

### I.8.g — The Weight Is the One That Adds

**Read:** the two sectors share no real coordinate axis, and $H(\tilde R_{\Phi}+\tilde H_{\Psi})=H(\tilde R_{\Phi})+H(\tilde H_{\Psi})$ while the other three forms carry cross terms.

**A measure that must add over independent alternatives has to be positive and diagonal.** The weight is both by construction: it is a sum of squared moduli over the eight real axes, and the two sectors occupy four axes each.

**The physical interpretation is that the weight is the measure a probability needs.** A probability that did not add over exclusive alternatives would not be a probability. The interval cannot play this role, because a difference of squares carries the cross terms and can fall when one term rises.

**The boundary.** Additivity is a statement about the coordinate splitting and not about composition. The weight does not add over a product, and the next interpretation supplies the counterexample.

### I.8.h — A Frame Is a Rank, Not a Phase

**Read:** $H(\tilde Q_0)=\tfrac12\operatorname{rank}\tilde Q_0$, so the frame's norm is $1$, $\tfrac12$ or $0$ and nothing else.

**An orientation has no size.** The frame is a partial isometry, and the only number it carries is the dimension of the space it acts on. Off the cone that dimension is two, on the cone it is one, and at the origin it is zero.

**The physical interpretation is that a frame cannot carry a coupling.** A quantity that takes three values, one of them zero, is a bookkeeping device and not a strength. Any reading in which the frame's norm measures an interaction strength is a misreading, and the factor $\tfrac12$ on the cone is the diagnostic.

**The boundary.** The value $\tfrac12$ is the trace convention again: a minimal projection has trace one and the unit has trace two. The statement that the frame is normalised to one is therefore false on the cone, by a factor of two.

### I.8.i — The Amplitude Is Not a Conserved Charge

**Read:** $H$ is not multiplicative, the norm of a square can be twice the square of the norm, and the sharp composition bound is $H(\tilde Q_1\tilde Q_2)\le2H(\tilde Q_1)H(\tilde Q_2)$.

**If the amplitude were a charge, composition would multiply it.** It does not, and the failure is not small: the witness attains the bound. So the amplitude is neither additive over a process nor multiplicative over a product. It is the norm of an element and nothing more.

**The physical interpretation is that amplitudes are not conserved and probabilities are not multiplicative under composition.** A conservation law needs a multiplicative invariant, and the only multiplicative invariant of this algebra is the quaternionic norm, which is not positive and therefore not an amplitude. The division of labour is forced by the algebra.

**The boundary.** The bound of two is the sharp constant for this normalisation. It is a fact about the trace convention and not a universal law; a rescaled norm would carry a rescaled constant.

### I.8.j — Two Senses of Frame

**Read:** a change of frame is a left multiplication $\tilde Q\mapsto\tilde U\tilde Q$; the frame of an element is the second polar factor $\tilde Q_0$.

**The two differ in what they act on.** A change of frame acts on the algebra and moves every element. The frame is a factor of one element and moves with it. Under a change of frame the amplitude conjugates and the frame multiplies on the left, and neither is quotiented away.

**The physical interpretation is that the polar decomposition is a decomposition and not a gauge fixing.** A gauge fixing removes a redundancy and leaves a representative of a class. The polar decomposition keeps the element and splits it into two invariantly defined pieces. A reader who conflates the passive and the active sense will conclude that the frame is unphysical, and the conclusion is a category error.

**The boundary.** The two senses coincide only when the frame is central, and then only up to the sign that the double cover supplies.

### I.8.k — The Amplitude Is the Hermitian Half

**Read:** $\tilde Q_H$ is Hermitian for every $\tilde Q$, so it lies in $\mathbb{B}_{\Psi}$ whatever sector the element belonged to.

**The decomposition maps the algebra onto its sector of positivity.** An element of the material sector has an informational amplitude. The material and the informational are not two kinds of object but two readings of one object, and the polar decomposition is the map between the readings.

**The physical interpretation is that a state is made from an operator by a canonical operation and not by a choice.** The operation is: take the Hermitian square, take the positive square root, normalise by its trace. Each step is canonical, so the state is a function of the element and not a convention about it.

**The boundary.** The sector of the original element is not lost, and it is not in the amplitude. It appears in the frame as the central phase $i$: the element $i\tilde Q$ has the same amplitude and the frame $i\tilde Q_0$. A sector flip is therefore a frame datum, and this is the precise sense in which the two sectors are one algebra read twice.

## The Limits

**The amplitude is not the mass, and the difference is not a correction term.** The identity $H=\lvert N\rvert\cosh\Xi$ is exact, and the factor is the Lorentz factor of the element's boost. An identification of the two holds only on the set of elements with no boost, which is the set of central phases times real quaternions.

**The H-pair is not the four-factor word.** The pair is defined on the whole algebra and its second factor is a partial isometry. The word needs the complement of the cone and its second factor is $*$-unitary. Results proved for one are not automatically results for the other, and the passage between them is the subject of the next entry.

**The H-norm is not an algebra norm.** Composition does not multiply it, and the failure is the constant two. Any argument that treats the amplitude as a charge, as a rate, or as a weight that multiplies under convolution is unsupported by the algebra.

**The state map is not injective and cannot be inverted.** Its fibres are five-dimensional in an eight-dimensional algebra. A state determines the boost and nothing else: not the scale, not the phase, not the rotor. Reading an element off a state requires five of the eight dimensions to be supplied from elsewhere.

**The purity reading is about an element and not about a subsystem.** The statement that a pure state is a null element is a statement about the amplitude of one element. It does not license the inference that every pure state of a composite is null, and it does not compute a reduced state.

**The decomposition removes nothing.** It is not a quotient, not a gauge choice, and not a coarse-graining. It is an identity in the algebra, and the two factors are as much a part of the element as the element is.

## Summary

The polar decomposition reads the Hermitian norm as the amplitude of an element and the residual factor as its frame.

| item | result |
| --- | --- |
| the pair | $\tilde Q=\tilde Q_H\tilde Q_0$, positive factor first, defined on the whole algebra |
| the amplitude | $\tilde Q_H=(\tilde Q\tilde Q^{*})^{1/2}=ae_t+i\vec W/(2a)$, Hermitian, in $\mathbb{B}_{\Psi}$ |
| the frame | $\tilde Q_0=\tilde Q_H^{+}\tilde Q$, a partial isometry, $*$-unitary off the cone |
| the invariants | $H(\tilde Q_H)=H(\tilde Q)$ and $N(\tilde Q_H)=\lvert N(\tilde Q)\rvert$ |
| the invariance | $H(\tilde U\tilde Q\tilde V)=H(\tilde Q)$, and $U(\mathbb{B})$ is exactly the group that does it |
| the frame's size | $H(\tilde Q_0)=\tfrac12\operatorname{rank}\tilde Q_0$, that is $1$, $\tfrac12$ or $0$ |
| the two singular values | $2H=\sigma_1^{2}+\sigma_2^{2}$, $\lvert N\rvert=\sigma_1\sigma_2$, $H-\lvert N\rvert=(\sigma_1-\sigma_2)^{2}/2$ |
| the rapidity | $\sigma_{1,2}=re^{\pm\Xi/2}$ with $r^{2}=\lvert N\rvert$, so $H=\lvert N\rvert\cosh\Xi$ |
| the state | $\tilde\varpi_Q=\tilde Q\tilde Q^{*}/(2H)=\tfrac12(e_t+i\tanh\Xi\,\vec u_{\mathrm b})$ |
| the purity | $1-\lvert N\rvert^{2}/(2H^{2})=(1+\tanh^{2}\Xi)/2$ |
| the composition bound | $H(\tilde Q_1\tilde Q_2)\le2H(\tilde Q_1)H(\tilde Q_2)$, sharp |
| the continuity | the amplitude everywhere; the frame everywhere except the cone and the origin |

The decomposition is characterised by four conditions: the amplitude in the cone, the product equal to the element, the final projection equal to the right ideal, and the amplitude generating the left ideal. The frame's norm is a rank, the amplitude's norm is the element's, and the state is the amplitude with its scale removed.

### What the Reader Should Retain

The three statements to carry away are these. The Hermitian norm is the only measure of the four that a positive factor can carry and the only one that both-sided unitary multiplication leaves alone, and that is why the polar decomposition is written with $H$ and not with $N$. The amplitude is the element's mass times its boost factor, $\lvert N\rvert\cosh\Xi$, and the frame is what remains: the phase, the rotation and the two axes, with a norm equal to half its rank. And the operator-to-state map is the normalised Hermitian square, whose image is the boost and whose purity measures how far the element sits from the light cone.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\tilde Q=\tilde Q_H\tilde Q_0$ | the polar decomposition, positive factor first |
| $\tilde Q_H$ | the amplitude, Hermitian positive semidefinite |
| $\tilde Q_0$ | the frame, a partial isometry, $*$-unitary off the cone |
| $\tilde Q_H^{+}$ | the Moore–Penrose inverse of the amplitude |
| $\tilde\Pi_{\mathrm f}(\tilde Q)$, $\tilde\Pi_{\mathrm i}(\tilde Q)$ | the final and initial projections, the two ideals of $\tilde Q$ |
| $a$, $\vec W$ | the scale and the real vector part of $\tilde Q\tilde Q^{*}$ |
| $\sigma_1\ge\sigma_2\ge0$ | the two singular values, the square roots of the spectral values of $\tilde Q\tilde Q^{*}$ |
| $r$, $\Xi$ | the scale and the rapidity of the polar word, $r^{2}=\lvert N\rvert$ and $\sigma_{1,2}=re^{\pm\Xi/2}$ |
| $\theta$, $\Theta$ | the central phase and the rotor angle of the polar word |
| $\tilde u_{\mathrm r}$, $\vec u_{\mathrm b}$ | the rotor, a real unit quaternion, and the axis of the boost |
| $H(\tilde Q)=\operatorname{Sc}(\tilde Q\tilde Q^{*})$ | the weight, the positive definite form, $\tfrac12\lVert\rho(\tilde Q)\rVert_{\mathrm{HS}}^{2}$ |
| $\lvert N(\tilde Q)\rvert$ | the modulus of the interval, the invariant mass |
| $\tilde\varpi_Q$ | the state, $\tilde Q\tilde Q^{*}/(2H)$, of trace one |
| $\lvert\vec r\rvert=\tanh\Xi$ | the Bloch length of the state, the boost velocity |
| $U(\mathbb{B})\cong U(2)$ | the $*$-unitary group, the group of H-isometries, real dimension four |
| $2H=\lVert\rho\rVert_{\mathrm{HS}}^{2}$ | the matrix picture of the weight and the source of the constant two |

## Further Reading

**In the mathematics corpus.** The ten articles of the source table, and inside the first of them the sections *The Hermitian Factor*, which owns the closed form and the invariants; *The Isometry Factor*, which owns the projections and the two counterexamples of uniqueness; and *Continuity*, which owns the discontinuity on the cone and at the origin. The cone of positivity and the uniqueness of the square root are in *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*. The two ideals and their projections are in *The Peirce Decomposition of the Biquaternion Algebra* and *Hermitian Idempotents and the Peirce Decomposition*.

**In this category.** *The Four Forms and the Four Norms* supplies the four measures, their definiteness and their multiplicativity. *The Four Products: Composition, Probability, Causality and Gauge* supplies the products whose scalar parts the measures are. *The Spectrum and the Two Modes* supplies the two invariants of an element and the pair whose product is the interval. *The Two Sectors: Split and the Four Bridges* supplies the coordinate split and the additivity of the weight across it. *The Element: the Six Subspaces and the Two Ledgers* supplies the six subspaces on which the polar factors are restricted.

**In the archive, until they are rewritten.** [The General Polar Decomposition, the Amplitude and the Operator-to-State Map](../articles_physics/the-general-polar-decomposition-the-amplitude-and-the-operator-to-state-map.html) is the earlier statement of the same pair and the same map. [The Polar Decomposition and Its Three Pairings](../articles_physics/the-polar-decomposition-and-its-three-pairings.html) compares the Cartan, Hamilton and quaternion pairings. [The Polar Decomposition of a Jones Matrix: Diattenuation, Retardance and Polarizers](../articles_physics/the-polar-decomposition-of-a-jones-matrix-diattenuation-retardance-and-polarizers.html) reads the amplitude as diattenuation and the frame as retardance. [The Polar Decomposition of a Kraus Operator: Effect, Backaction and the Measurement Boundary](../articles_physics/the-polar-decomposition-of-a-kraus-operator-effect-backaction-and-the-measurement-boundary.html) reads the amplitude as an outcome's strength and the frame as its backaction. [The Massless Limit as a Boundary Value of the Polar Word](../articles_physics/the-massless-limit-as-a-boundary-value-of-the-polar-word.html) is the limit in which the frame loses a rank and the state becomes pure.
