# __Rotor, Spin, Pair and Carrier: A Survey of the Closure Block__

## Introduction

This entry reads the block *Rotors, Spins, Carriers and Closures* of the mathematical category: four articles, in the order rotor, spin of a rotor, spin of a pair, carriers and closures. The first three derive the three spins from $SU(2)$; the fourth names, for each spin, the subspace that carries it and the subspace a field takes its values in. The last of them answers a single question — how the rotations act on the algebra, and into what pieces the algebra falls — and its answer is three subspaces of real dimensions one, two and three, carrying the weights zero, one half and one. Everything below is the reading of that answer, and the reading has one sentence at its centre: a field is a function with values in the closure of its carrier, and the spin of the field is the weight of the carrier.

The first claim is that the spin is a spectrum and not a name. The carrier is defined by an action, the action has a generator, and the generator has eigenvalues. The weights are the real numbers $\lambda$ such that $i\lambda$ is an eigenvalue of the generator on the carrier, and the spin is the largest weight. So $s=\tfrac12$ is a statement about the spectrum of one real operator on a real plane, and the identity $2s+1=\dim_\mathbb{R}$ of the mathematics is a relation between two readings of one string of eigenvalues and not between two independent numbers. Verified: on the plane the generator acts as the scalar $-\tfrac i2$ to $8.3\times10^{-17}$, and on the vector part as the cross product with the axis to $0$.

The second claim is that there are three carriers and no more, and that the reason is one line of module theory. The algebra is $\mathbb{B}\cong M_2(\mathbb{C})$, which is simple, so it has one isomorphism class of simple modules and every module is a sum of copies of it. The left action therefore sees one type, of complex dimension two, and its weight is $\tfrac12$. The adjoint action is an action of the group of invertibles, and it adds the fixed centre and the three-dimensional traceless part, whose weights are $0$ and $1$. A fourth value would need a second simple module, and there is none.

The third claim is that a carrier is a module and not a subspace, and that the passage from one to the other is a step of its own. The step is the closure. It is not one rule applied four times: the line closes by being made complex, the plane by the transverse direction, the spinor space by the second idempotent, and the vector part by the fixed line of the conjugation. The two lists of dimensions are therefore different, and the difference is the content of the entry: the carriers are $1,2,3$ and the spaces a field takes values in are $2,4,4$, with $8$ for the second step of the half-integer case. The arithmetic says the two lists are not one: $1+2+3=6$ while the algebra has real dimension $8$, and $2+4+8+4=18$, which counts the same algebra several times.

The fourth claim is that the closure performs two repairs and not a third. It restores invariance, which the plane does not have: no real subspace of dimension two is invariant under the whole rotation group, and the smallest invariant real subspace containing the plane has dimension four. It restores the norm, which the plane does not have either, and here the failure is total: the norm vanishes identically on a minimal left ideal, because every element of one has rank at most one. Verified on one hundred random elements of each ideal: the largest value of $\lvert N\rvert$ is $1.4\times10^{-15}$. What the closure does not repair is that vanishing: the norm of a pair of values is the pairing of the two, $N(\tilde\Xi_L+\tilde\Xi_R)=2\,\mathrm{Sc}(\tilde\Xi_L\tilde\Xi_R^{\natural})$, verified to $4.4\times10^{-15}$, so a single value of a spin-half field has no norm at any point of space-time and never acquires one. The mass of such a field is a coupling and not a modulus.

The fifth claim is that the three closures are not a decomposition of the algebra. The three carriers are three readings of one eight-dimensional object, not three summands of it. The only two decompositions available are the sector split $\mathbb{B}=\mathbb{B}_\Psi\oplus\mathbb{B}_\Phi$ and the Peirce split $\mathbb{B}=S_+\oplus S_-$ at an axis, and neither of them is the list of carriers.

The sixth claim is that the three carriers are the three answers to one question about an equation. Which subspaces of the algebra does the operator of a field equation preserve? A central operator preserves every complex subspace and therefore chooses nothing; the choice is made by the spin. A left multiplier preserves exactly the left ideals, and a sector equation preserves the sector. The three carriers, reached from the representation theory, are the same three spaces that the Klein–Gordon, Dirac and Proca operators select, and the two routes agree.

The first objection is that this is the representation theory of $\mathrm{SU}(2)$ and says nothing new. The values are standard, and the entry does not claim otherwise. What is not standard is that the carriers are subspaces of the algebra itself, so that all three live inside one eight-dimensional object and the three actions are actions of that object on itself. The consequence is the item the standard theory does not have: the norm vanishes identically on the half-integer carrier. That is a statement about the algebra, not about a module over it, and it is the reason the closure exists.

The second objection is that the two lists of dimensions are a bookkeeping muddle. They are two objects and the entry keeps the two words apart throughout: a carrier is a module, a closure is a subspace, and the words line, plane and vector part name the carriers while centre, spinor space, bispinor space and material sector name the closures. The lists differ because the passage is not free, and the section on the closure states what each passage costs.

The third objection is that a match between three algebraic labels and the observed spins is a prediction. It is not, and the mathematics does not make it. The algebra supplies the set $\{0,\tfrac12,1\}$; it does not say which particle carries which spin, and it does not say why the list is realised. The entry states the match, states its boundary, and does not lean on it.

The letters. The algebra is $\mathbb{B}$ with basis $e_t,\vec e_x,\vec e_y,\vec e_z$ and $\vec e_k^{2}=-e_t$, the central imaginary is $i$ with $i^{2}=-e_t$, and an element is $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu$ complex. The star is ${}^{*}$, the natural conjugation is ${}^{\natural}$, and the norm is $N(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$. The vector part is $\mathfrak{k}=\mathbb{R}\vec e_x\oplus\mathbb{R}\vec e_y\oplus\mathbb{R}\vec e_z$; the centre is $\mathbb{B}_C=\mathbb{C}e_t$; the sectors are $\mathbb{B}_\Psi=\{X^{*}=X\}$ and $\mathbb{B}_\Phi=\{X^{*}=-X\}$. At a unit real axis $\vec u$ the idempotents are $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec u)$, the plane is $\Sigma=\mathbb{C}\tilde\Pi_+$, and the ideals are $S_\pm=\mathbb{B}\tilde\Pi_\pm$. The generator is $A=\tfrac12\vec u$ and the rotor is $\tilde u=\cos\tfrac\theta2\,e_t+\sin\tfrac\theta2\,\vec u$. A representation is $\rho_{\mathrm{rep}}$, a weight is $\lambda$, the spin is $s$, and the quadratic element is $C=\sum_k\tilde S_k^{2}$ with $\tilde S_k=\tfrac12 i\vec e_k$.

Boundaries. The definition, the classification, the criterion, the quadratic element and the four closure rules are the mathematics' *From the Spin to the Carriers and the Closures*; $SU(2)$ and the two derivations of the spins are *The Spin Group via $4\times4$ Real Matrices*, *From the Spin Group to the Spin of a Single Rotor* and *From the Spin of a Single Rotor to the Spin of a Pair of Operators Acting on Two Sides*; the module theory behind the count is *The Category of Modules in the Biquaternion Algebra*; the Peirce basis and the corners are *The Peirce Decomposition of the Biquaternion Algebra*; the idempotents and their conjugacy are *The Square Roots of One and the Idempotents of the Biquaternion Algebra*; the polar form of the norm that carries the completeness proof is *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the averaging argument for compact groups is *Representations of Groups*. The three carriers are read one at a time in the three entries that follow this one, *Introduction to the Spin-Zero Centre Subspace*, *Introduction to the Spin-Half Bispinors Spaces* and *Introduction to the Spin-One Anti-Hermitian Subspace*. The reading of the carrier by a field equation is *The Klein–Gordon Equation in Biquaternionic Form*, *The Dirac Equation in Biquaternionic Form* and *The Proca Equation: Massive Spin 1 in Biquaternionic Form*. No dynamics, no action principle, no mass value and no quantum postulate appear below.

## The Source Table

| mathematical content | source article |
| --- | --- |
| $\mathrm{SU}(2)=S^3\to SO(\mathfrak{k})$ with kernel $\{\pm e_t\}$ | [The Spin Group via $4\times4$ Real Matrices](../articles_maths/the-spin-group-via-4x4-real-matrices.html) |
| the left-regular generators $L_k^2=-\mathrm{I}_4$ and $[L_x,L_y]=2L_z$, the Casimir $-3\,\mathrm{I}_4$, the spin $\tfrac12$ from $s(s+1)=\tfrac34$ | [From the Spin Group to the Spin of a Single Rotor](../articles_maths/from-the-spin-group-to-the-spin-of-a-single-rotor.html) |
| the pair on two sides, the two Casimirs, the total Casimir and the addition rule $\tfrac12\otimes\tfrac12=0\oplus1$ | [From the Spin of a Single Rotor to the Spin of a Pair of Operators Acting on Two Sides](../articles_maths/from-the-spin-of-a-single-rotor-to-the-spin-of-a-pair.html) |
| the rotation action and its generator, the three actions, the definition of a carrier, the two identities, the criterion of irreducibility by the weight string, the three carriers with their spectra, the completeness proof, the quadratic element, the four closure rules | [From the Spin to the Carriers and the Closures](../articles_maths/the-carriers-the-representation-the-spin-and-the-closure.html) |
| the simple module, the isomorphism $\mathbb{B}\cong\operatorname{End}_\mathbb{C}(S)$ and $\mathbb{B}\cong S\oplus S$, the classification of the modules | [The Category of Modules](../articles_maths/the-category-of-modules-in-the-biquaternion-algebra.html) |
| the two idempotents of an axis, the Peirce basis, the four corners, the minimal left ideals and the nilpotents | [The Peirce Decomposition of the Biquaternion Algebra](../articles_maths/the-peirce-decomposition-of-the-biquaternion-algebra.html) |
| the roots of one, the idempotents, their conjugacy and the families indexed by the axis | [Idempotents](../articles_maths/the-square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html) |
| the four forms of the twelve products, the Gram matrices and the inertias | [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](../articles_maths/the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html) |
| the compact group, complete reducibility, the averaging argument and the highest-weight string | [Representations of Groups](../articles_maths/representations-of-groups.html) |

**The fourth row owns the section, and the three above it give the spins that the section then places.** The other six supply the tools the section uses and does not prove: the module category, which makes the count of types a theorem; the Peirce basis, which produces the ideal from the axis; the idempotents, which make the family of ideals a family and not a choice; the polar form of the norm, which carries the completeness proof and does the work a trace form does in a treatment by matrices; and the compactness of the group, which makes the reducibility argument work without a finiteness hypothesis.

## The Results in Brief

The definition. A carrier is a nonzero real subspace of $\mathbb{B}$ that is invariant and irreducible under one of the algebra's own actions: left multiplication, or conjugation by an invertible element. The action is part of the carrier.

The route. The three spins come from $SU(2)$ alone, before any subspace is named. One rotor: on the quaternion layer the left-regular generators satisfy $L_k^2=-\mathrm{I}_4$ and $[L_x,L_y]=2L_z$, so the Casimir is $-3\,\mathrm{I}_4$, and $s(s+1)=\tfrac34$ gives $s=\tfrac12$. A pair acting on two sides: each factor carries $\tfrac12$, the addition rule gives $\tfrac12\otimes\tfrac12=0\oplus1$, and the total Casimir on the two-sided carrier has the spectrum $\{0,-2,-2,-2\}$. So $0$, $\tfrac12$ and $1$ are fixed first, and the subspaces are read afterwards.

The three carriers. The line $\mathbb{R}e_t$, of real dimension $1$, under the trivial action, with weight $0$ and spin $0$. The plane $\Sigma=\mathbb{C}\tilde\Pi_+(\vec u)$, of real dimension $2$, under left multiplication by the circle about $\vec u$, with weights $\pm\tfrac12$ and spin $\tfrac12$. The vector part $\mathfrak{k}$, of real dimension $3$, under the conjugation, with weights $\pm1,0$ and spin $1$. The dimensions are $1,2,3$ and the identity $2s+1=\dim_\mathbb{R}$ holds in the three cases.

The mechanism. Two identities carry every computation: $\vec u\tilde\Pi_+(\vec u)=-i\tilde\Pi_+(\vec u)$, and $[\tfrac12\vec u,\vec v]=\vec u\times\vec v$ for $\vec v\in\mathfrak{k}$. The first gives the scalar $-\tfrac i2$ on the plane, the second gives the cross product on the vector part. The commutator consumes the axis twice and the multiplication consumes it once, and that is the factor of two between the two spectra.

The criterion. A weight string that is simple and spaced by one is the string of an irreducible module, of complex dimension $2s+1$, where $s$ is its largest value. The three strings $\{0\}$, $\{\pm\tfrac12\}$ and $\{\pm1,0\}$ pass the test, so the three carriers are irreducible; a repeated weight is a direct sum, which is what the whole algebra shows, since its string is $\pm\tfrac12$ with multiplicity two.

The full turn. The operator of a full rotation is $+1$ on the line and on the vector part and $-1$ on the plane, that is $(-1)^{2s}$. On the plane the $-1$ is visible in the plane itself: a full rotation of space is a half turn of the plane.

The quadratic element. $C=\sum_k\tilde S_k^{2}=\tfrac34e_t$, and its values in the three modules are $0$, $\tfrac34$ and $2$, which are $s(s+1)$ at $s=0,\tfrac12,1$.

The completeness. Three types and no fourth, from the simplicity of $M_2(\mathbb{C})$ for the left action and from the compactness of the group for the conjugation. The two halves of the proof are different arguments and neither is a count of dimensions.

The two repairs. Invariance: no real two-dimensional subspace is invariant under the whole group, and the smallest invariant real subspace containing the plane is the ideal $S_+$, of real dimension $4$; verified, the residual of a transverse left multiplication on the plane is $2.24$ and the dimension of the invariant closure is $4$. Norm: the norm vanishes identically on each ideal, and the norm of a pair is twice the cross pairing, $N(\tilde\Xi_L+\tilde\Xi_R)=2\,\mathrm{Sc}(\tilde\Xi_L\tilde\Xi_R^{\natural})$.

The non-repair. A single value of a spin-half field has $N=0$ everywhere. The closure gives a norm to the pair and not to the value, so the mass of the field is a coupling of two values and never a modulus of one.

The closures. The line closes to the centre, $\dim_\mathbb{R}2$; the plane to the spinor space $S_+$, $\dim_\mathbb{R}4$; the spinor space to a bispinor space, $\dim_\mathbb{R}8$; the vector part to the anti-Hermitian space $\mathbb{B}_\Phi$, $\dim_\mathbb{R}4$, which the physics calls the material sector.

**No fourth.** The elementary list is closed on $\mathbb{B}$ alone. Higher spin requires a tensor product, and the algebra does not forbid it; it forbids only a fourth elementary value.

The match. The three values are the spins the established particles realise: the Higgs boson $0$, the six quarks and six leptons $\tfrac12$, the photon, the $W^{\pm}$, the $Z$ and the eight gluons $1$. The hadrons of higher spin are composites, and the massless spin-one field keeps two of its three states.

## What a Carrier Is

The two actions. The algebra acts on itself in two ways, and the classification uses both.

$$
L_X(Y)=XY,\qquad \mathrm{Ad}_u(Y)=uYu^{*},
$$

the first for every element $X$ and the second for every invertible $u$, that is for $uu^{*}=e_t$. The first is multiplicative on the whole algebra and needs no hypothesis; the second is an action of the group of invertibles by automorphisms, and it needs the unit condition, since $u^{-1}=u^{*}$ is what makes $\mathrm{Ad}_{uv}=\mathrm{Ad}_u\mathrm{Ad}_v$ hold. Right multiplication adds no type, because $\mathbb{B}$ is a full matrix algebra and left and right ideals correspond; and the bracket $\operatorname{ad}_X=L_X-R_X$ is the derived form of the second action, so a carrier of the conjugation at the identity is a carrier of the bracket.

The definition. A **carrier** is a nonzero real subspace $W\subseteq\mathbb{B}$ that is invariant and irreducible under one of these two actions. The action is part of the carrier, because the same subspace can be reducible for one and irreducible for the other, and there are examples at hand in both directions. The centre $\mathbb{B}_C$ is fixed pointwise by the conjugation and is therefore reducible for it: it is two real lines, each invariant. The vector part $\mathfrak{k}$ is irreducible for the conjugation and is not even invariant under left multiplication, since $i\vec e_x$ leaves it. So the word carrier without the action is not a word.

Why the action is part of the definition. The reason is not pedantry. The question a field theory asks is which subspaces survive the operator of its equation, and the operator is a multiplication or a conjugation and not an abstract map. A subspace can be minimal for one action and not closed for the other, and the closure of the later section is exactly the passage from a subspace that is minimal for a circle of rotations to one that survives an arbitrary multiplication. If the action were not part of the carrier, that passage would be invisible.

The three actions and the three carriers. Three representations occur, and each has one carrier.

The **trivial action** on the real line $\mathbb{R}e_t$: the conjugation fixes $e_t$, since $ue_tu^{*}=e_t$ for every invertible element, so the line is fixed pointwise and the operator of the generator is zero.

The **spinor action** on the plane $\Sigma=\mathbb{C}\tilde\Pi_+(\vec u)$: left multiplication, restricted to the circle of rotors about the axis $\vec u$. It acts on the plane by a phase of half the angle, which is where the half-integer weight comes from.

The **adjoint action** on the vector part $\mathfrak{k}$: the conjugation by the whole group of invertibles, which preserves $\mathfrak{k}$ and preserves the form, so it is a homomorphism onto $SO(\mathfrak{k})$ with kernel $\{\pm e_t\}$.

**Irreducibility means two different things in the two cases, and the difference is the point.** For the trivial action every real subspace is invariant, so irreducible means one-dimensional: the carrier of spin zero is a line, and the centre, which has real dimension two, is reducible and therefore not a carrier. For a nontrivial action irreducibility is a real condition, and the mathematics turns it into a reading of the spectrum by the criterion of the next section but one.

The generator. The generator along the axis is $A(\vec u)=\tfrac12\vec u$, a real pure element, and the representation of the rotor is its exponential,

$$
\rho_{\mathrm{rep}}(\tilde u)=\exp\bigl(\theta\,\rho_{\mathrm{rep}}(A(\vec u))\bigr),
$$

with a real operator and a real exponent. The halved angle of the rotor is not inserted into this formula; it is already in the element, since $\tilde u=\cos\tfrac\theta2+\sin\tfrac\theta2\vec u=\exp(\tfrac\theta2\vec u)$.

The weights. The **weights** of a carrier are the real numbers $\lambda$ such that $i\lambda$ is an eigenvalue of $\rho_{\mathrm{rep}}(A(\vec u))$ on the carrier's space, counted with multiplicity; the **spin** is the largest of them. The definition is well posed for two reasons, and the mathematics proves both. The weights are real, because the three operators are real-linear with purely imaginary eigenvalues: zero on the line, the scalar $-\tfrac i2$ on the plane, and the cross product on the vector part. And the weights do not depend on the axis, because the operators at two axes are similar, the similarity being the conjugation by a rotor that carries one axis to the other.

What the definition does not use. No angle, no array and no coordinate. The spin is read at the identity of the group, and the only place an angle enters is the full turn, where it enters as $2\pi$.

## The Route: a Rotor, a Pair and Three Spins

The rotor. A rotation of the pure part is a real-linear map that preserves the form and has determinant one, and the rotors are the unit quaternions $S^3=\{\tilde q:N(\tilde q)=1\}$. The map $S^3\to SO(\mathfrak{k})$ is onto with kernel $\{\pm e_t\}$, so a rotation has two rotors. Read on the quaternion layer $\mathbb{H}=\mathbb{R}e_t\oplus\mathbb{R}\vec e_x\oplus\mathbb{R}\vec e_y\oplus\mathbb{R}\vec e_z$ as a real space of dimension four, left multiplication by $\vec e_k$ is a real operator $L_k$, and the three satisfy

$$
L_k^2=-\mathrm{I}_4,\qquad [L_x,L_y]=2L_z\quad\text{and cyclically.}
$$

Verified on the layer: the three squares are $-\mathrm{I}_4$ to $0$, and the bracket identity to $0$.

**Part A: one rotor, and the spin follows from a sum of squares.** The generators of the action are the halved ones, $A_k=\tfrac12\vec e_k$, and with them the bracket is standard, $[A_x,A_y]=A_z$. The sum of their squares is a scalar,

$$
\sum_kL_k^2=-3\,\mathrm{I}_4,\qquad \sum_kA_k^2=-\tfrac34\,\mathrm{I}_4,
$$

verified to $0$. On a carrier of spin $s$ the same sum is $-s(s+1)$, so $s(s+1)=\tfrac34$ and the spin is $\tfrac12$. The number is read from one sum of squares on one real space of dimension four.

Part B: two rotors, and the other two spins from an addition rule. One factor on one side is not an action by automorphisms, since $L_X(YZ)=XYZ$ while $L_X(Y)L_X(Z)=XYXZ$: the two displays carry one copy of $X$ and two. A two-sided product carries one copy on each side, so a pair of rotors acts by $X\mapsto\tilde qX\tilde p$, and the diagonal generator is the difference of the two families,

$$
A_k^{\mathrm{tot}}=A_k-A_k',\qquad A_k'=\tfrac12R_{\vec e_k},
$$

which satisfies the standard bracket, because the minus sign of the right bracket cancels the minus sign of the difference. Each factor carries $\tfrac12$, and the addition rule for the labels of $SU(2)$ gives

$$
\tfrac12\otimes\tfrac12=0\oplus1 .
$$

The check by the total Casimir. On the two-sided carrier, of real dimension four, the total Casimir has spectrum $\{0\}$ once and $\{-2\}$ three times; on the tensor carrier, of real dimension sixteen, $0$ four times and $-2$ twelve times. Both verified. The equation $-j(j+1)\in\{0,-2\}$ has the two solutions $j=0$ and $j=1$, so the pair carries $0$ and $1$ and nothing else.

The three spins. One rotor gives $\tfrac12$, a pair gives $0$ and $1$, and the three are the whole list. The next question is which subspace of $\mathbb{B}$ of real dimension $2s+1$ carries each of them, and it is answered in *The Carriers*, after the criterion.

The quadratic element. The same three numbers are values of one element of the algebra. With $\tilde S_k=\tfrac i2\vec e_k$ the quadratic element is $C=\sum_k\tilde S_k^{2}=\tfrac34e_t$, verified, and its values on the three carriers are $0$, $\tfrac34$ and $2$, which are $s(s+1)$ at $s=0,\tfrac12,1$. The element is central and the values are those of the composed operator, so the algebra element and the operator are two objects; the mathematics says so in one remark, and the entry does not need more.

## The Criterion

Irreducibility is the one property of a carrier that no dimension supplies. The mathematics replaces the case-by-case check by one test, and the test is worth stating on its own because it is what makes the word spin a spectral word.

**The theorem.** Let $V$ be a finite-dimensional complex module for the rotation algebra, and suppose the weights of $\rho_{\mathrm{rep}}(A(\vec u))$ on $V$ are simple and spaced by one, the largest being $s$. Then $V$ is irreducible, $s$ is its highest weight, and $\dim_\mathbb{C}V=2s+1$.

The proof in one paragraph. The group is compact, so $V$ splits into irreducibles. On an irreducible the weights form one string, symmetric about zero and spaced by one: the module is generated by an eigenvector of the largest weight, and the two ladder elements built on an oriented pair completing the axis raise and lower the weight by one, or annihilate at the ends. A string that is symmetric and spaced by one contains $0$ exactly once, so the multiplicity of the weight $0$ on $V$ is the number of its summands, and the hypothesis makes that number one.

What the test buys. The three strings $\{0\}$, $\{\pm\tfrac12\}$ and $\{\pm1,0\}$ are simple and spaced by one, so the three carriers are irreducible and their complex dimensions after complexification are $1,2,3$. The largest weight is read from the string and the length of the string is the complex dimension, so a carrier is determined in both respects by its spectrum, and $2s+1=\dim$ is a relation between two readings of one string.

What a repeated weight means. A weight that occurs twice is a direct sum. The whole algebra under left multiplication has the string $\pm\tfrac12$ with multiplicity two, and the reason is $\mathbb{B}=S_+\oplus S_-$: two carriers of one type, not two types. This is why the criterion is a statement about multiplicities and not only about the set of values, and it is the sentence that keeps the corpus from counting the two ideals as two particles.

The reading. A spin-$s$ multiplet has $2s+1$ states, and here the count is the count of the real dimensions of the carrier. The two numbers are the same number because the carrier is a real space and the rotation acts on it by a real operator whose eigenvalues are purely imaginary and come in pairs. Nothing in the criterion refers to a particle, a field or a representation of the Lorentz group; it refers to the spectrum of one element on one real space.

## The Carriers

The three carriers are stated in the order of their spins, $0$, $\tfrac12$, $1$, which is also the order fixed line, spinor plane, vector part: the two rotation-invariant pieces first, the one-sided one after. Each is described by the same template: the subspace, the action, the operator, the spectrum, the dimension, the spin, and the sign of a full turn.

| carrier | $\dim_\mathbb{R}$ | action | $\rho_{\mathrm{rep}}(A(\vec u))$ | weights | $s$ | $2s+1$ | full turn |
| --- | --- | --- | --- | --- | --- | --- | --- |
| fixed line $\mathbb{R}e_t$ | $1$ | trivial | $0$ | $\{0\}$ | $0$ | $1$ | $+1$ |
| spinor plane $\Sigma=\mathbb{C}\tilde\Pi_+$ | $2$ | $L$ on the circle about $\vec u$ | the scalar $-\tfrac i2$ | $\{\pm\tfrac12\}$ | $\tfrac12$ | $2$ | $-1$ |
| vector part $\mathfrak{k}$ | $3$ | $\mathrm{Ad}$ of the invertibles | $\vec u\times$ | $\{\pm1,0\}$ | $1$ | $3$ | $+1$ |

### The Fixed Line

The line is $\mathbb{R}e_t$. The conjugation fixes it pointwise, because $e_t$ is central and $uu^{*}=e_t$. The operator is zero, the spectrum is $\{0\}$ with multiplicity one, the dimension is one, the spin is zero, and a full turn has operator $+\mathrm{id}$. The line is the smallest carrier in the list and the only one whose action is trivial, and the triviality is not a degenerate case to be apologised for: it is what spin zero is, and the whole of the scalar sector of the corpus rests on it.

### The Spinor Plane

The plane is $\Sigma=\mathbb{C}\tilde\Pi_+(\vec u)=\mathbb{R}\{\tilde\Pi_+,\,i\tilde\Pi_+\}$, where $\tilde\Pi_+=\tfrac12(e_t+i\vec u)$ is the idempotent of the axis. It lies in the left ideal $S_+=\mathbb{B}\tilde\Pi_+$, so every left multiplication carries it into $S_+$ and not necessarily into itself.

The action is one line of algebra. The axis commutes with the idempotent, since the idempotent is a polynomial in it, and $\vec u\tilde\Pi_+=\tfrac12(\vec u+i\vec u^{2})=\tfrac12(\vec u-ie_t)=-i\tilde\Pi_+$. So the rotor multiplies the plane by a phase of half its angle,

$$
\tilde u\,\tilde\Pi_+(\vec u)=\Bigl(\cos\tfrac\theta2-i\sin\tfrac\theta2\Bigr)\tilde\Pi_+(\vec u)=e^{-i\theta/2}\,\tilde\Pi_+(\vec u).
$$

The half angle is therefore not a convention and not an insertion: it is what the identity gives. The operator of the generator is the scalar $-\tfrac i2$, and as a real operator on two real dimensions its eigenvalues are $-\tfrac i2$ and $+\tfrac i2$. The spectrum is $\{\pm\tfrac12\}$, the dimension two, the spin $\tfrac12$, and a full turn has operator $-1$.

**The plane is not invariant under the whole group.** Left multiplication by the transverse axis sends $\tilde\Pi_+(\vec u)$ out of $\Sigma(\vec u)$, and the plane is carried by the circle of rotations about its own axis and by no larger group. This is the failure that the closure repairs, and the repair is forced: the smallest real subspace that contains the plane and is invariant under all left multiplications has real dimension four, and it is $S_+$.

### The Vector Part

The vector part is $\mathfrak{k}=\mathbb{R}\vec e_x\oplus\mathbb{R}\vec e_y\oplus\mathbb{R}\vec e_z$. The conjugation preserves it, because $u\vec vu^{*}$ is a real pure element for an invertible element $u$ and a real pure $\vec v$, and it preserves the norm, so it preserves the form and gives a homomorphism onto $SO(\mathfrak{k})$ with kernel $\{\pm e_t\}$.

The operator is the cross product with the axis. The identity is the quaternion product rule $\vec u\vec v=-\vec u\cdot\vec v+\vec u\times\vec v$ applied to the difference $\vec u\vec v-\vec v\vec u$:

$$
[\tfrac12\vec u,\vec v]=\tfrac12(\vec u\vec v-\vec v\vec u)=\vec u\times\vec v ,
$$

and the commutator with half the axis is the cross product with the whole axis. The cross product annihilates the axis and turns the perpendicular plane by a quarter turn, so with an oriented orthonormal pair $\vec u_2,\vec u_3$ completing the axis the eigenvectors are $\vec u_2\pm i\vec u_3$, with eigenvalues $\mp i$. The weights are $\pm1$ and $0$; the dimension is three, the spin one, and a full turn has operator $+\mathrm{id}$.

### The Factor of Two

The generator is the same real element $\tfrac12\vec u$ in both nontrivial cases, and the two spectra differ by a factor of two. The reason is one sentence: the commutator consumes the axis twice and the multiplication consumes it once. On the vector part the operator is $[\tfrac12\vec u,\cdot]$, which equals the cross product with the whole axis, and the quarter turn of the cross product gives the eigenvalues $\mp i$, hence the weights $\pm1$. On the plane the operator is a single multiplication by half the axis, which gives the scalar $-\tfrac i2$, hence the weights $\pm\tfrac12$. This is the algebraic content of the difference between integer and half-integer spin, and it is a statement about how many times an element is used in the operator, not about a group.

## Three and No More

The left action sees one type. The algebra is $\mathbb{B}\cong M_2(\mathbb{C})$ and $M_2(\mathbb{C})$ is simple, so it has one isomorphism class of simple modules, of complex dimension two, and every finite-dimensional left module is a sum of copies of it. On that module the generator $\tfrac12\vec u$ is a traceless matrix whose square is a quarter of the unit, with weights $\pm\tfrac12$. A one-dimensional module would be a unital algebra map $M_2(\mathbb{C})\to\mathbb{C}$, whose kernel is a two-sided ideal; the algebra is simple, so the kernel is zero or everything, and neither is possible. There is therefore no one-dimensional module, and the left action has no spin zero.

The conjugation adds two. As a Lie algebra the biquaternion algebra is $\mathbb{B}=\mathbb{C}e_t\oplus\mathfrak{k}$ with $\mathfrak{k}\cong\mathfrak{sl}_2(\mathbb{C})$; the centre is the trivial module, of weight $0$, and the traceless part is the three-dimensional irreducible module, of weights $\pm1,0$. There is no other irreducible invariant subspace, because the conjugation is a compact group action and the two summands are the fixed space and its orthogonal complement for the invariant form.

The count. One type from multiplication and two from conjugation, and no fourth: a fourth would need a second simple module, and the algebra has one.

Where higher spin lives. The closure is a statement about $\mathbb{B}$ alone, and it does not forbid higher spin. Spin $2$ is the symmetric traceless square of the vector part, spin $\tfrac32$ is the symmetric cube of the plane, and the general construction is a tensor product. The mathematics states this and stops there; it is the subject of *Higher Spin from Tensor Products: The Three Carriers and the Absence of a Fourth*, which is the archived reading of the same closure from the side of the tensors.

The reading of the count. The set $\{0,\tfrac12,1\}$ is what one algebra of dimension eight can carry as elementary types. That the observed elementary particles carry exactly these three spins is a match of labels and is stated as such: the Standard Model assigns the spins by hand, and the algebra does not select which particle carries which.

**The two halves of the proof are different arguments.** The half for the left action is module theory and it is sharp: one simple module, hence one type. The half for the conjugation is compactness and averaging: the group is compact, so the module splits, and the fixed space of the action is the centre by the invariance of the polar form of the norm. Neither half is a count of dimensions, and neither would survive without its hypothesis.

## The Closure of a Carrier

A carrier is a module and a field takes values in a subspace. The passage from one to the other is the **closure**: to a carrier attach a real subspace of $\mathbb{B}$ that contains its space, is invariant under the action, and is the smallest subspace with a further property named by the rule of the case. The definition is deliberately incomplete, because the further property is not the same in the four cases. The table below is the mathematics' own, reproduced because every one of its four rows is a placement of a field.

| carrier | $\dim_\mathbb{R}$ | closure | $\dim_\mathbb{R}$ | property the rule adds |
| --- | --- | --- | --- | --- |
| line | $1$ | centre $\mathbb{C}e_t$ | $2$ | being a complex subspace |
| plane | $2$ | spinor space $S_+\cong\mathbb{C}^{2}$ | $4$ | none: invariance under the whole group |
| spinor space | $4$ | a bispinor space | $8$ | containing both members of the Peirce pair |
| vector part | $3$ | material sector $\mathbb{B}_\Phi$ | $4$ | being the whole eigenspace of the conjugation |

### The First Repair: Invariance

The failure. No real subspace of $\mathbb{B}$ of dimension two is invariant under the whole rotation group. The plane is invariant under the rotations about its axis and under no others: the transverse axis is an element whose left multiplication carries $\tilde\Pi_+(\vec u)$ out of $\Sigma(\vec u)$.

The measurement. The residual of $L_{\vec w}\Sigma$ on $\Sigma$ for an invertible element $\vec w$ perpendicular to the axis is $2.24$ in the Euclidean norm on the eight real coordinates, over one hundred random axes, so the failure is not marginal. The dimension of the real span of $L_X\Sigma$ over a basis of the algebra is $4$ in every trial, and that span is $S_+$, which is closed under every left multiplication.

The repair. The smallest invariant real subspace containing the plane is the minimal left ideal $S_+=\mathbb{B}\tilde\Pi_+$. The step is not a convenience and not a supply of $i$ either: the plane is a complex line already and multiplication by $i$ acts inside it. What the plane lacks is the transverse direction, and the repair adds it. The step is inside the ideal, from one complex line to two, and it costs two real dimensions.

The reading. The field equation of a half-integer field is a left multiplication, and a subspace survives an arbitrary left multiplication only if it is a left ideal. The plane therefore cannot be the space a spin-half field takes values in, and the reason is not that the plane is too small for the spin but that it is too small for the equation. This is the precise sense in which a field takes values in a closure: the closure is the smallest space that the equation cannot push it out of.

### The Second Repair: The Norm

The failure. The norm vanishes identically on a minimal left ideal. The reason is that every element of an ideal has rank at most one as an endomorphism of the two-dimensional complex module, and an element of rank at most one is a zero divisor, so its norm is zero. Verified on one hundred random elements of each of the two ideals at one hundred random axes: the largest value of $\lvert N\rvert$ is $1.4\times10^{-15}$.

What the failure costs. No length, no mass, no normalisation and no probability density from the algebra's own form. A value of a spin-half field cannot be assigned a modulus, and the failure is not a defect of a particular element: it holds at every element of the ideal, at every axis, at every point of space-time. Nothing that the closure does can give a norm to a single value, and this is the one thing the closure does not repair.

The repair. The norm of a pair of values is the cross pairing of the two. With $\tilde\Xi_L\in S_+$ and $\tilde\Xi_R\in S_-$,

$$
N(\tilde\Xi_L+\tilde\Xi_R)=2\,\mathrm{Sc}\bigl(\tilde\Xi_L\tilde\Xi_R^{\natural}\bigr),
$$

verified to $4.4\times10^{-15}$ on one hundred random pairs. Each term on the right is a pairing of the two ideals, and the left side is the norm of the sum; so the norm of a bispinor is twice its pairing, and the pairing is the only place a norm can live.

The reading. A mass term of a spin-half field cannot be a modulus, because a modulus of one value is zero at every point; it must couple two values, and the only invariant coupling available is the pairing. This is the strongest single statement of the section, and it is exact rather than approximate: the vanishing is an identity.

The boundary of the reading. The two Peirce ideals are copies of one module, and the copy index is not a chirality; the chiral pairing is between a value and its conjugate space, not between the two Peirce summands. The pairing statement above holds for both readings because both are a pairing of two slots, and the entry does not identify the two. What the entry claims is the shape: a spin-half mass is off-diagonal in whatever two-slot structure the field is written in.

### What Is Not Repaired

**The vanishing is not a symptom.** A reader may expect the closure to restore the norm of the value, since it restores invariance. It does not, and the mathematics says why in the same breath: the norm on the bispinor space is off-diagonal. The diagonal is zero on each summand, and the closure adds the second summand and the pairing between them, not a modulus on either.

The contrast with the other two carriers. On the centre the norm is the square of a complex number, real and positive on the real axis and real and negative on the imaginary one, so the modulus exists on the two copies of the carrier and not on the complex plane they span. On the material sector the norm is real and indefinite, so a vector field has a modulus that can have either sign. On the ideals the norm is zero, and the field has a modulus only through a pair. The three carriers therefore behave in three different ways under the one operation that a field theory needs most, and the difference is a property of the carrier and not of the field.

## The Closures

### The Centre

The carrier is the line $\mathbb{R}e_t$ and the closure is the centre $\mathbb{C}e_t=\mathbb{R}e_t\oplus\mathbb{R}(ie_t)$, of real dimension two. The property named by the rule is being a complex subspace, and the smallest complex subspace containing the line is the line together with $ie_t$. That the result is the whole fixed space of the conjugation, and not merely a complex line through $e_t$, is a theorem and not part of the rule: $uXu^{*}=X$ for every invertible element holds only for the central elements.

The carrier sits inside with multiplicity two: the real and the imaginary lines are two copies of the trivial carrier, and they are the real and imaginary parts of one complex line. This is why the centre is a closure and not a carrier: as a space under the trivial action it is reducible, and the carrier is the line.

The reading. The closure adds one degree of freedom and it is the phase. A real line has a magnitude and no phase; a complex line has a magnitude and a phase, and the phase is what a charge is. The step from the carrier to the closure is therefore the step from a real scalar to a complex scalar, and it is the smallest step in the list: one real dimension, one phase, one charge.

### The Spinor Space

The carrier is the spinor plane and the closure is the spinor space $S_+=\mathbb{B}\tilde\Pi_+=\mathbb{C}\{\tilde\Pi_+,\vec u_2\tilde\Pi_+\}$, of real dimension four and complex dimension two. It is a minimal left ideal: no nonzero left subspace of it is invariant. It carries the same carrier as the plane, with weights $\pm\tfrac12$, and the step adds the transverse direction.

The reading. The closure adds the state the equation reaches. The plane is the set of values a spinor can have at a point in a basis of one complex line; the ideal is the set of values it can have when the equation is allowed to multiply by anything. The two differ by one complex direction, and that direction is not a second spin: it is the same spin, in the other basis vector of the module.

### The Bispinor Spaces

The complementary idempotent $\tilde\Pi_-=\tfrac12(e_t-i\vec u)=e_t-\tilde\Pi_+$ gives a second ideal $S_-=\mathbb{B}\tilde\Pi_-$, of the same dimension, and the sum is direct, $\mathbb{B}=S_+\oplus S_-$. Each axis therefore produces a **bispinor space**: the algebra read through the Peirce basis of that axis, that is, the pair of ideals and their sum.

The family. There is one bispinor space per Peirce basis, so there are as many as there are unit axes, and two axes that differ by a sign give the same unordered pair, so the family is indexed by the real projective plane. As sets the members coincide, because each of them is $\mathbb{B}$; what varies is the splitting. The family is therefore a family of decompositions of one space and not a family of subspaces of it, and the naming keeps that apart: a spinor space is a subspace, and a bispinor space is the whole space together with a splitting.

The reading. The pair of values is a pair and not two particles. The two ideals are isomorphic, metrically orthogonal, and exchanged by nothing in the algebra's structure; the second is added because the field must be able to occupy both, and the reason it must is the norm of the previous section, which is off-diagonal. And the axis is a frame and not a datum: the algebra carries every axis and singles out none, so the choice of Peirce basis is a choice of basis and not a statement about the algebra.

### The Anti-Hermitian Space

The carrier is the vector part and the closure is the anti-Hermitian space $\mathbb{B}_\Phi=\{X:X^{*}=-X\}=\mathbb{R}(ie_t)\oplus\mathfrak{k}$, of real dimension four. The property named by the rule is being the whole eigenspace of the conjugation, and the star is an involution, so the algebra splits into its $+1$ and $-1$ eigenspaces and the closure takes the whole of the $-1$ one.

The extra line. The vector part lies in the $-1$ eigenspace and is not the whole of it: multiplication by $i$ carries the vector part to a Hermitian space, so the eigenspace needs a real line as well, and the line is $\mathbb{R}(ie_t)$. That line is not a second carrier: it is the degenerate summand, fixed by the action, and it is the same carrier as the line of the centre.

Why this half and not the other. The Hermitian half $\mathbb{B}_\Psi$ is also invariant, also of dimension four, and also splits as a line and a three-dimensional summand; the two halves carry the same module, since multiplication by $i$ is a real-linear isomorphism carrying one onto the other. What separates them is the involution identity $(XY)^{*}=Y^{*}X^{*}$, which needs no axis: on $\mathbb{B}_\Phi$ the bracket of two elements stays in the half, and on $\mathbb{B}_\Psi$ it does not. Of the four halves of the algebra exactly two are closed under the bracket, and only $\mathbb{B}_\Phi$ both contains the carrier and is closed. Verified: the bracket of two random anti-Hermitian elements is anti-Hermitian with defect $0$.

The reading. The closure adds the time slot. A spin-one field's value has three states, and the material sector has four real dimensions; the fourth is the temporal direction $ie_t$, and it is the generator of the central phase and not a state. The constraint of the theory removes it, and the carrier that survives the constraint is the vector part again. This is why the spin-one closure is the only one whose dimension does not equal $2s+1$: the fourth slot is not a state.

**The exact statement of the mismatch.** On the centre the real dimension of the closure is $2$ and $2s+1=1$; on the ideal the real dimension is $4$ and $2s+1=2$; on the material sector the real dimension is $4$ and $2s+1=3$. In the first two cases the closure is complex and its complex dimension is $2s+1$; in the third the closure is a real form, so no complex dimension exists and the identity has no reading at all. The identity is therefore a statement about the carrier, and every attempt to read it directly on the closure either doubles it or fails.

## The Carrier and the Field Equation

The question the dynamics asks. An equation is an operator acting on a field, and a subspace carries the solutions of the equation when the operator maps that subspace into itself for every field in it. The three carriers are the three answers, and the answers are reached from the dynamics without using the representation theory.

| equation | field | spin | the space | the operator preserves it by |
| --- | --- | --- | --- | --- |
| Klein–Gordon | $\tilde\Xi$ | $0$ | the centre | being a central real scalar |
| Dirac | $\tilde\Xi_L,\tilde\Xi_R$ | $\tfrac12$ | $S_+,S_-$ and their sum | multiplying on the left |
| Proca | $\tilde A_\Phi$ | $1$ | the material sector, then the vector part | the two-sided action, and the constraint |

The scalar case, and why the equation chooses nothing. The Klein–Gordon operator is central and real, so it multiplies all four complex coefficients by the same number and preserves every subspace closed under real scalars. The equation is therefore satisfied by a field with four independent complex coefficients and by a field with one, and nothing in the equation prefers either. The spin prefers one: a spin-zero field has one complex value at each event, and the carrier of one complex number is the centre. The restriction of the field to the centre costs nothing in the equation, because the operator is central.

The spinor case, and why the sector cannot hold it. The Dirac operator is the gradient, an element multiplying on the left, so it preserves exactly the left ideals. No nonzero subspace of the material sector is a left ideal, and the proof is one line: if $W\subseteq\mathbb{B}_\Phi$ were a nonzero left ideal, then $iW\subseteq W$ because $i$ is central, but $i\mathbb{B}_\Phi=\mathbb{B}_\Psi$, so $iW\subseteq\mathbb{B}_\Phi\cap\mathbb{B}_\Psi=\{0\}$ and $W=\{0\}$. Verified: a random left multiple of a random anti-Hermitian element leaves the sector by $22.4$. A spin-half field therefore cannot be confined to the material sector, whatever the frame, and this is a theorem and not an opinion.

The vector case, and why the sector is the space. The Proca potential is an element of the material sector, the operator is built from one material gradient, and the sector is preserved by the two-sided action and by real central multiplication. The sector is therefore the space the field takes values in, and the vector part inside it is the carrier of the spin; the difference of one dimension is the constraint, which removes the temporal slot.

The two routes agree. The representation theory says three carriers of dimensions one, two and three. The dynamics says a central operator, a left multiplier and a sector. The two lists are the same list, and the agreement is not an accident: both are asking which subspaces the algebra's own actions preserve.

**One asymmetry the three closures do have, and it is a property of ideals rather than of subspaces.** Each closure survives *its own* operator, but only one survives an *arbitrary* left multiplication, which is what a general coupling would exert. A left multiplier $L_X$ with arbitrary $X$ carries the centre out of itself, since $X(\lambda e_t)=\lambda X$ is central only if $X$ is, and it carries the traceless part out of itself for the same reason at one order higher; an ideal, by contrast, is closed under every $L_X$ by definition. **So the bispinor space is the only one of the three whose home is stable against a coupling operator the algebra can supply, and the other two are stable only against the specific operators their equations use.** The limit: this is a statement about left multiplication, and a coupling that acts by the two-sided action or by conjugation is a different question, answered by the invariance of the corresponding subspace.

## Why the Three Are Not a Direct Sum

**The arithmetic.** The carriers are $1+2+3=6$ real dimensions while the algebra has $8$. The closures are $2+4+8+4=18$, which is more than twice the algebra. Neither sum is a decomposition, and the second is not even a sum of disjoint subspaces: the bispinor space is the whole algebra, the spinor space is one of its summands, and the centre meets the material sector in the line $\mathbb{R}(ie_t)$.

The two decompositions that do exist. The star splits the algebra into the two sectors, of real dimensions $4+4$, and the Peirce basis splits it into the two ideals, also $4+4$. The first is a split into a Lie algebra and its complement; the second is a split into two minimal left modules. The carriers are neither.

The reading. A biquaternion field is not a scalar plus a spinor plus a vector. It is one eight-real-dimensional value at each event, and the three carriers are three readings of that value, one for each action. The distinction has teeth: a model that added the three would have six real dimensions at each event and would not be this algebra, and a model that added the closures would have eighteen and would not be a space at all.

## The Interpretations

The spin is the top of a ladder. The spin of a carrier is its largest weight, and the weights of an irreducible carrier are $s,s-1,\dots,-s$, so the carrier has $2s+1$ of them and that number is its real dimension. The warrant is the criterion and the three computations. The boundary is that this is the rotation spin: the Lorentz label of a field is a pair of spins, and the massless case uses helicity.

A field takes values in the closure, not in the carrier. The carrier is what the action sees; the closure is what the equation cannot push the field out of. The warrant is the first repair: the plane fails invariance by $2.24$ in the Euclidean norm, and the smallest invariant space containing it has dimension four. The boundary is that the closure is a subspace condition and not an equation of motion: it says where the field may live, not how it moves.

The carrier fixes the dimension of the value, and the equation does not. The Klein–Gordon operator is central, so it preserves every subspace and chooses nothing; the spin chooses. The warrant is the centrality, which is exact. The boundary is that the choice is by dimension and by action, and the equation of a given spin is a separate statement.

One value has no norm; the mass is a pairing. The norm vanishes on the ideal at every element, and the norm of a pair is twice the cross pairing. The warrant is the identity $N(\tilde\Xi_L+\tilde\Xi_R)=2\,\mathrm{Sc}(\tilde\Xi_L\tilde\Xi_R^{\natural})$ to $4.4\times10^{-15}$ and the vanishing to $1.4\times10^{-15}$. The boundary is that the pairing is a shape and not a number, and that the two Peirce ideals are copies and not chiralities.

The axis is a frame, not a datum. The idempotents exist at every unit axis, the spectrum does not depend on the axis, and the family of bispinor spaces is indexed by the real projective plane. The warrant is the lemma that the operators at two axes are similar and the theorem that the algebra singles out no axis. The boundary is that a choice of quantisation axis is a choice of basis; nothing in the algebra makes one axis preferred.

A full turn is $(-1)^{2s}$. The operator of the full turn is $+\mathrm{id}$ on the integer carriers and $-\mathrm{id}$ on the half-integer one, so the half-integer carrier is an action of the double cover and the integer carriers are actions of the rotation group. The warrant is the eigenvalue $e^{2\pi i\lambda}$ at $\lambda=\pm\tfrac12$, verified as $\rho_{\mathrm{rep}}(-e_t)=-\mathrm{id}$ on the plane to $8.7\times10^{-17}$. The boundary is that the sign is a statement about the action and not about statistics.

Charge belongs to the closure and not to the carrier. The centre carries every phase, since a central phase commutes with everything and preserves the complex line; the material sector carries only $\pm1$, since every other phase leaves it. The warrant is the centrality of $i$ and the reality of the sector. The boundary is that this is a statement about which phases preserve the space of values, and not about a coupling constant.

The extra line of the material sector is the time slot. The carrier has three dimensions and the closure has four, and the fourth is $\mathbb{R}(ie_t)$, which is the generator of the central phase and not a state; the constraint removes it. The warrant is the split $\mathbb{B}_\Phi=\mathfrak{k}\oplus\mathbb{R}(ie_t)$ and the fact that the field strength is pure, hence already in the carrier. The boundary is that the constraint is an input and not a consequence.

**The three carriers are three readings and not three summands.** The carriers are $1+2+3=6$ dimensions against an algebra of $8$, and the closures $2+4+8+4=18$. The warrant is the arithmetic and the overlaps. The boundary is that the two decompositions that exist, by the star and by the Peirce basis, are not the list.

The three values are the spins of the observed elementary particles. The set $\{0,\tfrac12,1\}$ is not only the algebra's list; it is the list that the established particles realise, and no established particle carries another value. The warrant is the classification and the table.

| $s$ | established elementary particles | carrier |
| --- | --- | --- |
| $0$ | the Higgs boson $H$ | the line |
| $\tfrac12$ | the six quarks $u,d,c,s,t,b$ and the six leptons $e,\mu,\tau,\nu_e,\nu_\mu,\nu_\tau$ | the plane |
| $1$ | the photon $\gamma$, the $W^{\pm}$ and the $Z$, and the eight gluons $g$ | the vector part |

The boundary is that the match is a match of labels. The algebra supplies the set and does not select which particle carries which value, and it says nothing about masses, generations, charges or colour. The quarks and the gluons are counted by flavour and by colour although they are observed only as confined constituents of hadrons and jets, and the gluon's colour octet is an $SU(3)$ structure that the algebra does not host: what the vector part carries for a gluon is its free kinematics and not its colour.

Two boundaries hold the match in place. The first is that hadrons are composites. The values $\tfrac32$, $2$ and $\tfrac52$ do occur, and the particles that carry them — the $\mathcal{B}(1232)$ and the $\Omega^-$, the tensor mesons, the $N(1680)$ — are bound states of quarks and gluons and not elementary, so they are excluded from the table rather than left unexplained by it. The second is that the massless spin-one field keeps two states and not three: the carrier has three dimensions, and for a massless field the longitudinal state is removed by gauge invariance, leaving the two helicities of the photon and of the gluon. The warrant is the count $2s+1=3$ and the gauge reduction. The boundary is that the reduction is an input of the massless theory and not a consequence of the carrier: the algebra supplies the triplet, and the two-state count is what gauge invariance does to it.

## The Limits

- No dynamics. The entry states which subspaces carry a field and what the operator preserves. It does not write an equation of motion, an action or a propagation.
- No mass value. The pairing is a shape; the number is dynamical and belongs to the equations.
- The rotation spin only. The label $s$ is the highest weight of the rotation generator. The Lorentz label is a pair, and the massless case is a helicity.
- No spin-statistics. The split between the associative carrier and the adjoint carriers is algebraic. The link from that split to Fermi and Bose statistics is a separate theorem, and the entry does not make it.
- The particle match is a label match. The three values are the observed elementary spins, stated under The three values are the spins of the observed elementary particles, with the two boundaries under Two boundaries hold the match in place. The algebra supplies the set and does not select which particle carries which, the hadrons of higher spin are composites and not elementary, and the massless spin-one field keeps two states and not three.
- **The closure is not positivity.** The material sector is indefinite, and the norm on the ideal vanishes. Nothing in the entry produces a positive definite form on a carrier.
- No canonical axis. The bispinor family is indexed by the real projective plane and the algebra singles out no member. Whether a condition internal to the algebra could fix one is an open question of the mathematics.
- Families, not spaces. The bispinor spaces coincide as sets and differ as splittings. A statement about one of them is a statement about a decomposition, not about a subspace.
- One algebra. The classification is for $\mathbb{B}$ alone. Higher spin needs a tensor product, and the algebra does not forbid it.
- Copies are not chiralities. The two Peirce ideals are isomorphic copies of one module. The chirality of a field is the side of a basis operator, and the entry does not identify the two.

## Summary

Three spins, and they come from $SU(2)$ before any subspace is named. One rotor: on the quaternion layer the left-regular generators satisfy $L_k^2=-\mathrm{I}_4$ and $[L_x,L_y]=2L_z$, so the Casimir is $-3\,\mathrm{I}_4$ and $s(s+1)=\tfrac34$ gives $s=\tfrac12$. A pair on two sides: each factor carries $\tfrac12$, the addition rule gives $0$ or $1$, and the total Casimir confirms it. The subspaces are read afterwards, and not before.

The carrier is a nonzero real subspace of the algebra, invariant and irreducible under one of the algebra's own actions, and the action is part of the carrier. There are three: the line, of real dimension one, under the trivial action, with weight $0$; the plane, of real dimension two, under left multiplication by the circle about its axis, with weights $\pm\tfrac12$; and the vector part, of real dimension three, under the conjugation, with weights $\pm1,0$. The spins are $0,\tfrac12,1$, the identity $2s+1=\dim_\mathbb{R}$ holds in the three cases, and the count is complete because the algebra is a full matrix algebra with one simple module and because the group of invertibles is compact.

The weights come from two identities and no array: the axis times the idempotent is $-i$ times the idempotent, which gives the scalar $-\tfrac i2$ on the plane, and the commutator with half the axis is the cross product with the whole axis, which gives the quarter turn on the vector part. The factor of two between the two spectra is the number of times the axis is used in the operator.

The closure is the passage from a module to a subspace, and it is four rules: the line becomes complex, the plane gains the transverse direction, the spinor space gains the second idempotent, and the vector part gains the fixed line of the conjugation. The closure performs two repairs. It restores invariance, which the plane lacks by $2.24$ and which the ideal supplies at the cost of two real dimensions. It restores the norm, which the ideal lacks entirely, since every element of an ideal has rank at most one and the norm vanishes at every element; the norm of a pair is twice the cross pairing, so a spin-half mass is a coupling of two values. The closure does not repair the vanishing of the norm of a single value, and that is the one exact statement of the entry: a single value of a spin-half field is massless at every point of space-time.

The three closures are not a decomposition. The carriers are one algebra read three ways, and the arithmetic $1+2+3=6$ and $2+4+8+4=18$ is the proof. The two decompositions the algebra has are the sector split and the Peirce split, and the carriers are neither.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\mathbb{B}$ | the biquaternion algebra, real dimension $8$, $\cong M_2(\mathbb{C})$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the quaternion basis, $\vec e_k^{2}=-e_t$ |
| $i$ | the central imaginary, $i^{2}=-e_t$ |
| $\tilde Q=Q_te_t+\vec Q$ | an element, with complex coefficients $Q_\mu$ |
| ${}^{*}$, ${}^{\natural}$ | the star and the natural conjugation |
| $N(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the norm |
| $\mathrm{Sc}$ | the scalar part of a product |
| $\mathfrak{k}$ | the vector part, $\mathbb{R}\vec e_x\oplus\mathbb{R}\vec e_y\oplus\mathbb{R}\vec e_z$ |
| $\mathbb{B}_C=\mathbb{C}e_t$ | the centre, real dimension $2$ |
| $\mathbb{B}_\Psi$, $\mathbb{B}_\Phi$ | the Hermitian and anti-Hermitian sectors, the second being the material sector |
| $\vec u$ | a unit real axis |
| $\theta$ | the rotation angle, twice the angle of the rotor |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec u)$ | the idempotents of the axis, a Peirce basis |
| $\Sigma=\mathbb{C}\tilde\Pi_+$ | the spinor plane, real dimension $2$ |
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | the spinor spaces, real dimension $4$ |
| $\mathbb{H}$ | the quaternion layer, $\mathbb{R}e_t\oplus\mathfrak{k}$, real dimension $4$ |
| $L_k$, $R_k$ | left and right multiplication by $\vec e_k$, real $4\times4$ operators |
| $A_k=\tfrac12\vec e_k$, $A_k'=\tfrac12R_{\vec e_k}$ | the halved generators of the two sides |
| $A(\vec u)=\tfrac12\vec u$ | the generator along the axis |
| $\tilde S_k=\tfrac12 i\vec e_k$ | the Hermitian generator of the coordinate axis |
| $C=\sum_k\tilde S_k^{2}=\tfrac34e_t$ | the quadratic element |
| $\rho_{\mathrm{rep}}$ | a representation of an action on a carrier |
| $\lambda$, $s$ | a weight, and the spin, the largest weight |

## Further Reading

- [The Spin Group via $4\times4$ Real Matrices](../articles_maths/the-spin-group-via-4x4-real-matrices.html), for $SU(2)$ and its kernel.
- [From the Spin Group to the Spin of a Single Rotor](../articles_maths/from-the-spin-group-to-the-spin-of-a-single-rotor.html), for the left-regular generators, the Casimir and $s=\tfrac12$.
- [From the Spin of a Single Rotor to the Spin of a Pair of Operators Acting on Two Sides](../articles_maths/from-the-spin-of-a-single-rotor-to-the-spin-of-a-pair.html), for the pair, the two Casimirs and the addition rule.
- [From the Spin to the Carriers and the Closures](../articles_maths/the-carriers-the-representation-the-spin-and-the-closure.html), for the definition, the criterion, the completeness proof and the four closure rules.
- [The Category of Modules](../articles_maths/the-category-of-modules-in-the-biquaternion-algebra.html), for the simple module, the isomorphism $\mathbb{B}\cong\operatorname{End}_\mathbb{C}(S)$ and the classification of the modules.
- [The Peirce Decomposition of the Biquaternion Algebra](../articles_maths/the-peirce-decomposition-of-the-biquaternion-algebra.html), for the two idempotents, the four corners and the minimal left ideals.
- [Idempotents](../articles_maths/the-square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), for the roots of one and the families indexed by the axis.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](../articles_maths/the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the polar form of the norm and the inertias.
- [Representations of Groups](../articles_maths/representations-of-groups.html), for complete reducibility and the highest-weight string.
- [The Rotations, the Boosts and the Groups](../articles_internal/the-rotations-the-boosts-and-the-groups.html), for the actions whose carriers these are.
- [The Klein–Gordon Equation in Biquaternionic Form](the-klein-gordon-equation-in-biquaternionic-form.html), for the central operator and the restriction to the centre.
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), for the left multiplier and the two ideals.
- [The Proca Equation: Massive Spin 1 in Biquaternionic Form](the-proca-equation-massive-spin-1-in-biquaternionic-form.html), for the sector as the space of a four-vector.
- [Higher Spin from Tensor Products: The Three Carriers and the Absence of a Fourth](higher-spin-from-tensor-products-the-three-carriers-and-the-absence-of-a-fourth.html), for what the closure does not forbid.
