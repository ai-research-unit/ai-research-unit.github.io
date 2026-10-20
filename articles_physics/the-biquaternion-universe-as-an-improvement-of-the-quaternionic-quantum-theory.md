# __The Biquaternion Universe as an Improvement of the Quaternionic Quantum Theory__

## Introduction

Between 1962 and the end of the twentieth century a sustained attempt was made to build quantum theory on the quaternion algebra. The attempt produced a complete formalism with a name and a literature of its own. It is called **quaternionic quantum theory**; it was founded by David Finkelstein, Josef Jauch, Samuel Schiminovich and David Speiser in 1962, and it was developed to full length by Stephen Adler in 1995. This article is about that theory, and about what the biquaternion universe of this corpus does with it.

The article has two parts, and they are meant to be read in order.

**Part I presents the quaternionic theory on its own terms.** It gives the algebra the theory is built on, the postulates it uses, what it achieved, and the limits it met. Part I does not refer to the biquaternion theory at all, and this is deliberate. The quaternionic theory is the older of the two, and it has to be described as what it was, not as an imperfect version of something that came later. Its sources are the quaternionic literature, named in Further Reading. No statement in Part I is a result of this corpus.

**Part II presents the biquaternion theory, limit by limit.** For each of the five limits of Part I it states what the biquaternion theory does, and it then states which parts of the quaternionic achievement are kept. The correspondence is summarised in two tables, each with the corpus article that owns the item, so that a reader can always tell which statements belong to the older theory, which belong to this corpus, and which belong to the standard physics against which both are measured.

**The sense of the word "improvement".** The biquaternion universe is offered here as an improvement of quaternionic quantum theory in the sense of a **successor that repairs and continues**, not in the sense of a refutation. The quaternionic theory was not incoherent, and its mathematics was not mistaken. It met five limits, and all five are consequences of one decision: putting the quaternion algebra where the scalar field goes. The biquaternion theory reverses that decision, and the reversal removes the first three limits outright and repairs the fourth in its scalar form. The fifth is not removed: the successor adopts it and proves it as a theorem, and states its consequence openly. That is what the improvement amounts to, and the article says it plainly rather than claiming a victory.

**The result in one sentence.** Quaternionic quantum theory placed the quaternion algebra where the **scalar field** of a quantum theory goes, and every one of its limits is a limit of that placement. The biquaternion theory takes the **complex numbers** as its scalars and keeps the quaternion units as **elements of its algebra**, where they supply the internal directions and generate the rotations. The relocation carries a price, stated at the end of Part II: a theory whose scalars are already complex agrees with ordinary quantum mechanics instead of departing from it.

**What "the quaternions" names, in each theory.** The word does different work in the two theories, and the article keeps the two uses apart throughout. In quaternionic quantum theory the quaternions are the **field of scalars**: the states live in a quaternion module, the amplitudes are quaternions, and the transition amplitude is a quaternion product. In the biquaternion theory the quaternion units $\vec e_x,\vec e_y,\vec e_z$ are **elements of an algebra over the complex scalars**. With $e_t=1$ and $\vec e_k^{2}=-e_t$ they supply the internal directions, they generate the rotations, and they act on the state module $S\cong\mathbb{C}^{2}$ through $\vec e_k\mapsto-i\sigma_{k}$. Two things the biquaternion theory does **not** use: the quaternions as a field of scalars, and the division-ring property, since $\mathbb{B}\cong M_{2}(\mathbb{C})$ has zero divisors. What it uses is the units, their sign $\vec e_k^{2}=-e_t$, and the centre $\mathbb{C}e_t$. The corpus states the same distinction in the form that the algebra's two roles — the imaginary unit of the coefficients and the quaternion units of the directions — cannot be exchanged (*Conventions in the Biquaternion Universe*, §*The Elements and their Coefficients*).

# Part I. The Quaternionic Quantum Theory

## The Quaternions as a Scalar Field

### The Algebra of Quaternions

Hamilton's quaternions form a four-dimensional real algebra,
$$
\mathbb{H}=\{a+bi+cj+dk : a,b,c,d\in\mathbb{R}\},
$$
whose multiplication is determined by
$$
i^{2}=j^{2}=k^{2}=-1,\qquad ij=k=-ji,\qquad jk=i=-kj,\qquad ki=j=-ik .
$$
Its elementary properties are the following.

- **It is associative and not commutative.** $ij=k$ while $ji=-k$, so the order of the factors matters, and every product may be bracketed freely.
- **It is a division ring.** The conjugation $q\mapsto q^{*}=a-bi-cj-dk$ satisfies $qq^{*}=q^{*}q=a^{2}+b^{2}+c^{2}+d^{2}=\lvert q\rvert^{2}\in\mathbb{R}$, so every non-zero element has the two-sided inverse $q^{-1}=q^{*}/\lvert q\rvert^{2}$.
- **Its norm is multiplicative.** $\lvert pq\rvert=\lvert p\rvert\lvert q\rvert$, which is the four-square identity.
- **Its unit sphere is the double cover of the rotation group.** The unit quaternions are $\{q:\lvert q\rvert=1\}\cong SU(2)\cong S^{3}$, and they cover the rotation group $SO(3)$ twice. The imaginary units $i,j,k$ are the generators of the rotations, with
$$
[i,j]=2k,\qquad [j,k]=2i,\qquad [k,i]=2j .
$$
- **It is not algebraically closed.** The equation $x^{2}+1=0$ has infinitely many solutions in $\mathbb{H}$, namely the whole two-sphere of pure unit quaternions. Among the normed division algebras only $\mathbb{C}$ is algebraically closed.
- **It is represented by complex matrices.** With $q=a+bi+cj+dk$, the map
$$
R(q)=\begin{pmatrix}a+bi & c+di\\ -c+di & a-bi\end{pmatrix}
$$
is an injective algebra homomorphism into the $2\times2$ complex matrices, and it turns quaternionic conjugation into conjugate transposition.

By Hurwitz's theorem of 1898 there are exactly four normed division algebras: $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ and the octonions. Of the four, $\mathbb{H}$ is the one that is non-commutative and still associative, which is what made it the natural candidate for a scalar field. A quantum theory whose scalars are quaternions would carry three-dimensional rotation inside its scalar field rather than in its operators, and the units of its scalars would be exactly the spin transformations.

### A Quantum Theory over a Non-Commutative Field

A scalar field does three things in a quantum theory. It multiplies the vectors of the state space, it takes the values of the inner product, and it supplies the phase of an amplitude. When the scalars are quaternions, all three have to be redefined, because multiplication on the left and multiplication on the right are different operations.

- **The state space.** States live in a right $\mathbb{H}$-module $V$ with an $\mathbb{H}$-valued inner product $\langle\cdot\mid\cdot\rangle$, conjugate-linear in one slot and linear in the other, with $\langle v\mid v\rangle$ real and non-negative and equal to zero only for $v=0$.
- **The states.** A state is the right $\mathbb{H}$-line generated by a non-zero vector, the set $v\mathbb{H}$. Two vectors name the same state exactly when one is the other multiplied on the right by a non-zero quaternion, so the state space is the quaternionic projective space of $V$.
- **The observables.** An observable is an $\mathbb{H}$-linear self-adjoint operator, that is, $\langle Av\mid w\rangle=\langle v\mid Aw\rangle$.
- **The amplitudes and the probabilities.** The amplitude of a transition from $v$ to $w$ is the quaternion $\langle v\mid w\rangle$, and the transition probability is the real number $\lvert\langle v\mid w\rangle\rvert^{2}/(\langle v\mid v\rangle\langle w\mid w\rangle)$. The probability is a real number, as in the complex theory. What is enlarged is the amplitude, whose phase is now a whole unit quaternion.
- **The dynamics.** The evolution is generated by an anti-self-adjoint operator, and the equation of motion has to place the scalar on one side of the state.
- **The measurement postulates.** The projection onto an eigenspace is stated with quaternionic projectors, and it inherits the same one-sided placement.

**The convention this creates.** Every one of these definitions contains a choice of side: whether the scalar multiplies on the left or on the right, and which slot of the inner product carries the conjugation. The choices are not independent, and the formalism is coherent only when they are fixed consistently. This is the first indication of what the limits in the last section of Part I are about. A non-commutative scalar field does not merely enlarge the complex numbers; it introduces a convention wherever the complex theory had none.

The formalism as described here was constructed in 1962 and developed in full in 1995. It is a theory and not a sketch, and the next section records what it obtained.

## What the Theory Achieved

### A Complete Formalism

The theory was built out in full: state space, observable algebra, probability rule, projection postulate, unitary dynamics, composite systems and scattering. Adler's 1995 monograph is a systematic development of the whole programme, including quaternionic field theory and the stability conditions that a quaternionic dynamics has to satisfy. The limits of the next section are therefore the limits of a finished theory and not of an unfinished one, and they are the limits of the theory as it stands.

### The Scalar Field Is an Input, Not a Theorem

The programme's foundational result is that **the scalar field of a quantum theory is an input and not a consequence of the structure of the propositions alone**. The argument has two halves, and they come from different sources.

- **The reconstruction theorems admit three scalar fields.** The propositional structure of a quantum theory, an orthomodular lattice of propositions or an orthomodular space in the infinite-dimensional case, admits more than one coefficient field. The reconstructions of Piron and, for the infinite-dimensional case, of Soler, yield exactly the three associative division algebras as candidates: $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$. The quaternionic case is therefore a genuine reconstruction of quantum theory and not an ad hoc proposal.
- **The commutativity requirement selects one.** Birkhoff and von Neumann, in the 1936 paper that founded quantum logic, argued for commutativity: the standard propositional calculus requires the coefficient field to commute, and a non-commutative field does not reproduce it. The modern form of the argument is that the additional regularity axioms on the lattice, over and above orthomodularity, are the ones a non-commutative coefficient field does not satisfy.

Read together, the two halves say this. **Orthomodularity alone permits $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$; commutativity of the coefficient field selects $\mathbb{C}$ among them.** The quaternionic theory is what one obtains when the second requirement is not imposed. That is a genuine achievement of the programme, and it is also the exact place where the limits begin.

### Spin and Rotations Inside the Scalars

The unit quaternions are $SU(2)$, the double cover of the rotation group, and the imaginary units $i,j,k$ are the rotation generators. A theory whose scalars are quaternions therefore has three-dimensional rotation built into its scalar field: the phase freedom of a state is a rotation, and the phase of a quaternionic amplitude is a point of $SU(2)$ rather than a point of the circle. This is the structural reason the programme was pursued, since it promised to make spin and the internal transformation structure intrinsic to the scalars. It is also the origin of the phase limit in the next section, because the same fact makes the phase group $SU(2)$ instead of $\mathrm{U}(1)$.

### Spacetime and the Lorentz Group

The older role of the quaternions is the geometry of space and of spacetime. The pure imaginary quaternions are three-dimensional space, the unit quaternions are the rotations, and the Lorentz transformations of Minkowski space are the corresponding transformations of the complexified algebra. The programme inherited this role, so a quaternionic quantum theory sits inside a formalism that already carries both the rotation group and the Lorentz group. This is the second reason the scalar field was attractive, and it is the part of the quaternionic achievement that is purely geometric and therefore not exposed to any of the limits of the next section.

### The Mathematics It Generated

The programme produced a body of mathematics that stands independently of its physical conclusions: the theory of quaternionic Hilbert spaces and their operators, the spectral theory of quaternionic linear operators, quaternionic matrix analysis, and the classification of quantum theories over the associative division algebras. This mathematics is not in doubt, and it is not a casualty of the limits below.

### What It Reproduces of Ordinary Quantum Mechanics

A quaternionic quantum theory contains the ordinary theory as the case in which the scalars are restricted to a commutative subfield. Fixing a complex subfield of $\mathbb{H}$, which is the same as choosing a square root of $-1$ inside the quaternions, reduces the module, the operators and the dynamics to the complex theory. Ordinary quantum mechanics is therefore a sector of the quaternionic theory rather than a rival to it. The programme's difficulty was never that it contradicted ordinary quantum mechanics. It was that the quaternionic structure could not be kept while the requirements of the next section were met.

## The Limits of the Theory

The limits are stated in the order in which they were raised. The first three concern a single system, the fourth concerns two systems or more and is the decisive one, and the fifth is the conclusion the programme reached about its own physical content. Each is stated as a requirement that could not be met, not as a failure of reasoning.

### The Scalars Do Not Commute

**The requirement.** The standard propositional calculus of quantum theory, with its operations on propositions and its lattice of subspaces, is coordinatised by a commutative field.

**What happens instead.** The quaternionic scalars do not commute, and the consequences run through the formalism. The inner product has to choose a side, and the two choices give different structures. The closure properties of the observable algebra have to be re-examined, because products of self-adjoint operators no longer behave as they do in the complex theory. The spectral equations acquire a convention, as the next subsection records. And the set of allowed superpositions is restricted by the non-commutativity.

**What the limit is and is not.** The concession of the previous section stands: the pure orthomodular structure admits $\mathbb{H}$, so this is not a contradiction inside the logic. It is a departure from the standard formalism, and each of the later limits is a consequence of it.

### The Spectrum Is a Set of Classes

**The requirement.** The possible values of an observable are the eigenvalues of its operator, each with its eigenspace, and the measurement postulates are stated in terms of them.

**One version of this limit is often repeated and is not correct.** It is said that the spectral theorem does not hold over $\mathbb{H}$. For the operators a quantum theory uses, it does hold.

**The quaternionic spectral theorem, Hermitian case.** A quaternionic Hermitian matrix is diagonalisable by a quaternionic unitary, and its eigenvalues are real.

*The reason.* Under the regular representation above, a quaternionic $n\times n$ matrix becomes a complex $2n\times 2n$ matrix, quaternionic conjugation becomes conjugate transposition, and the quaternionic Hermitian condition becomes the ordinary Hermitian condition. The measurement postulates are therefore not lost.

*The check.* Under the regular representation introduced above, one hundred random quaternionic Hermitian $2\times2$ matrices were generated and realised as complex Hermitian $4\times4$ matrices. Every sample had a real spectrum, every eigenvalue occurred with even multiplicity, and every sample was diagonalisable.

**What genuinely remains is three points, and all three concern conventions and choices rather than existence.**

- **The diagonal is forced to be real.** The Hermitian condition $H_{jk}=H_{kj}^{*}$ forces every diagonal entry to be a real quaternion. This is a constraint the complex theory does not carry.
- **The eigenvalue equation needs a side.** The equations $Av=v\lambda$ and $Av=\lambda v$ are different over $\mathbb{H}$, and the left and right spectra need not agree. A convention is required before a spectrum can be written down at all.
- **The spectrum of a general operator is a set of classes.** For a non-normal quaternionic operator the eigenvalues are quaternions, and the eigenvalue set is closed under conjugation by units. For the $1\times1$ matrix whose entry is $1+2i$, the eigenvalues are exactly the conjugates $uqu^{-1}$. Over one hundred random unit quaternions $u$, the real part stayed at $1$ and the imaginary norm stayed at $2$ to machine precision, while the imaginary part spread over the sphere. An eigenvalue is a **conjugacy class**, a two-sphere, and not a number.

**The choice this forces.** Selecting a representative in each conjugacy class is equivalent to selecting a **maximal commutative subfield** of $\mathbb{H}$, and every such subfield is isomorphic to $\mathbb{C}$. Stated correctly, the limit is therefore not that there is no spectral theory over $\mathbb{H}$. It is that **the spectral theory over $\mathbb{H}$ requires a complex structure, and that structure has to be chosen**. The complex numbers are not absent from the theory. They are an input to it.

### The Phase Is Non-Abelian

**The requirement.** Two amplitudes combine with a **relative phase**, the phase group is the circle $\mathrm{U}(1)$, and interference is the addition of amplitudes that differ by a phase.

**What happens instead.** The phase group of the quaternionic theory is the unit quaternions, which is $SU(2)$. A non-abelian phase group changes the composition of amplitudes: two amplitudes cannot be combined by a single relative factor in the way the complex theory combines them, and the allowed superpositions inherit the non-commutativity. The interference structure is not lost, since the transition probability is still a real number, but it is no longer the interference of the complex theory. The burden then falls on showing that the difference is not observable.

### Composite Systems Do Not Compose

**The requirement.** The state space of two systems is the tensor product of their state spaces, and the observable algebra of the pair is generated by the algebras of the parts acting on that product. This is not a convention of one formalism. It is the composition rule of quantum theory, and entanglement, quantum correlations and quantum information are built on it.

**What happens instead.** The quaternionic theory cannot meet the requirement at the level of its scalars, because
$$
\mathbb{H}\otimes_{\mathbb{R}}\mathbb{H}\cong M_{4}(\mathbb{R})\neq\mathbb{H}.
$$
The dimensions give $4\times4=16=4^{2}$, so the tensor square is a full matrix algebra over $\mathbb{R}$ and not the quaternions. Equivalently, the class of $\mathbb{H}$ in the Brauer group of $\mathbb{R}$, which is $\mathbb{Z}/2$, has order two, so its square is the identity class and the tensor square is split.

**Why this is the decisive limit.** The first three could be treated as conventions, as choices to be made, or as features to be checked against experiment. This one cannot. A scalar field that does not compose cannot carry the composition rule, and no better analysis of the theory repairs it. This is the reason the programme did not return.

**Its further consequence.** The same mechanism suppresses the theory's departures from ordinary quantum mechanics in composite systems. Once two quaternionic systems are combined, the resulting structure carries a complex structure, and the quaternionic effects are no longer available to be measured. The composition limit is therefore also the reason the programme could not obtain a distinguishable prediction from composite systems.

### The Conclusion Reached by the Programme Itself

The fifth item is not an objection from outside. It is the programme's own finding, and it is the strongest statement of the position.

**Consistency forces a complex structure.** The requirements of a conserved probability, a well-defined dynamics, and a stable notion of orthogonality under the evolution, taken together, force a complex structure on the state space. Once that structure is fixed, the theory is complex quantum mechanics equipped with additional sectors.

**The consequence for prediction.** The theory is not separated from ordinary quantum mechanics by experiment. Its departures are confined to the structure that the consistency requirements remove. This is the same statement as the previous subsection in another form, and it is where Part I ends.

# Part II. The Biquaternion Theory

The biquaternion theory of this corpus does not contest the conclusion reached at the end of Part I. It adopts it: the complex structure that the quaternionic requirements force is placed at the centre of the algebra from the outset, and the theory that follows is the subject of this part.

## The Algebra of the Biquaternion Universe

The biquaternion algebra is the complexification of the quaternions:
$$
\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_{2}(\mathbb{C}).
$$
Its elements are written
$$
\tilde Q=Q_{t}e_{t}+Q_{x}\vec e_{x}+Q_{y}\vec e_{y}+Q_{z}\vec e_{z},\qquad Q_{\mu}\in\mathbb{C},
$$
with $e_t=1$, $\vec e_k^{2}=-e_t$ for $k=x,y,z$, and $\vec e_x\vec e_y=\vec e_z$ together with its cyclic companions. The algebra is associative, and it is not commutative.

**What the complexification changes, in three items.**

- **The scalar imaginary is central.** The element $i$ commutes with every $\vec e_k$, so the centre of the algebra is $Z(\mathbb{B})=\mathbb{C}e_t$, the complex numbers.
- **The algebra is central simple over its centre.** The isomorphism $\mathbb{B}\cong M_{2}(\mathbb{C})$ is an isomorphism of complex algebras, so $\mathbb{B}$ is a full matrix algebra over $\mathbb{C}$. This is precisely the property that quaternionic scalars lack, and the whole of Part II turns on it.
- **The units survive as elements and cease to be scalars.** The elements $\vec e_x,\vec e_y,\vec e_z$ remain, with $\vec e_k^{2}=-e_t$ and the rotation bracket, but they commute with the scalars $i$ and do not commute with one another. They are elements of the algebra over $\mathbb{C}$, not the field of scalars.

**The conjugations and the sectors.** Three operations act on $\mathbb{B}$: the coefficientwise conjugation $\overline{\cdot}$, which conjugates the complex coordinates; the natural conjugation ${}^{\natural}$, which fixes $e_t$, negates $\vec e_x,\vec e_y,\vec e_z$ and is $\mathbb{C}$-linear; and the Hermitian conjugation ${}^{*}={}^{\natural}\circ\overline{\cdot}$, so that $Q^{*}_{\nu}=\varepsilon_{\nu}\overline{Q_{\nu}}$ with $\varepsilon=(1,-1,-1,-1)$. The Hermitian conjugation splits the algebra into its two fixed spaces,
$$
\mathbb{B}=\mathbb{M}_{+}\oplus\mathbb{M}_{-},
$$
where $\mathbb{M}_{+}$ is the Hermitian sector, the elements with $\tilde Q^{*}=\tilde Q$, and $\mathbb{M}_{-}$ is the anti-Hermitian sector. The material sector carries Minkowski space, $\mathbb{M}_{-}\cong\mathbb{R}^{3,1}$, and $\mathbb{M}_{+}$ is the four-dimensional Hermitian sector that the state side uses.

**The matrix model.** The isomorphism is fixed by its values on the basis,
$$
\mathsf{M}_2(e_t)=I_{2},\qquad \mathsf{M}_2(\vec e_k)=-i\sigma_{k},\qquad \mathsf{M}_2(i\tilde Q_1)=i\,\mathsf{M}_2(\tilde Q_1),
$$
so that $\mathsf{M}_2$ is an isomorphism of $\mathbb{C}$-algebras onto the $2\times2$ complex matrices. The trace convention of the series is $\mathrm{Tr}=2\,\mathrm{Sc}$, where $\mathrm{Sc}(\tilde Q_1)$ is the coefficient of $e_t$.

**The four forms.** The scalar parts of the four general products give the four series forms,
$$
\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2),\quad
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2),\quad
\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*}),\quad
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*}).
$$
Two of them are the metric and the probability. The form $\langle\cdot\rangle_{\natural}$ is the biquaternion norm, and on the material sector it is the **Minkowski interval**. The form $\langle\tilde Q_1,\tilde Q_2\rangle_{*}$ is the Hermitian form,
$$
\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=\sum_{\mu}Q_{1\mu}\overline{Q_{2\mu}},
$$
which is linear in the first slot, conjugate-linear in the second, and **positive definite**; its unit group is $\mathrm{U}(2)$, its signature is $(8,0)$ on $\mathbb{B}$ and $(4,0)$ on $\mathbb{M}_{-}$, and it is the internal Hilbert-space structure that the Born rule and the unitary evolution use. On the material sector all four forms are real and $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=-\langle\tilde Q_1,\tilde Q_2\rangle$, so the definite form and the indefinite form meet there in the way that the quaternionic conjugation and the quaternionic norm met.

**The state module.** The algebra is an algebra of operators on a complex two-dimensional module,
$$
\mathbb{B}\cong \mathrm{End}(S),\qquad S\cong\mathbb{C}^{2}.
$$
The states are the positive elements of the cone of $\mathbb{M}_{+}$ normalised by $\langle\tilde{Ϛ},e_t\rangle=\tfrac12$ (trace one in the $2\times2$ image), their space is the Bloch ball, and the three imaginary directions $\vec e_x,\vec e_y,\vec e_z$ supply its three axes. The Born rule is the pairing $\langle\tilde Q_1,\tilde Q_2\rangle_{*}$ on this module.

The definitions and the numerical values used above are those of *Conventions in the Biquaternion Universe*; the sector identification is argued in *The Anti-Hermitian Subspace $\mathbb{M}_{-}$ as the Material Sector*; the state side is developed in *The Native Qubit and the Defining Module of the Biquaternion Algebra*.

## The Corrections

Each subsection below names a limit from Part I and states what the biquaternion theory does with it. The first, second and third are removed outright. The fourth is repaired in its scalar form and remains in a form common to the whole of quantum mechanics, and the subsection states exactly how the two parts divide. The fifth is neither removed nor denied: the successor adopts it and proves it as a theorem. The whole correspondence is then summarised in the Ledger.

### The Scalar Field Is Commutative by Construction

**The limit addressed.** The scalars do not commute, so the standard formalism is not reproduced (Part I, *The Scalars Do Not Commute*).

**What the biquaternion theory does.** It takes the algebra as an algebra over its own centre. The scalars of $\mathbb{B}$ are $Z(\mathbb{B})=\mathbb{C}e_t\cong\mathbb{C}$, which is commutative and algebraically closed, and the quaternion units are elements of the algebra and not its scalars. Every consequence of the limit is removed with that single change:

- conjugate-linearity belongs to one slot, so the inner product has one reading;
- the spectral equations have one reading, since the scalars commute;
- the observable algebra is closed under the operations the theory uses;
- the coefficient field of the propositional calculus is commutative.

The first limit is therefore not answered by an argument. It is avoided by construction, because the biquaternion theory has no quaternionic scalars.

**The metric is not a family either.** In the quaternionic theory the generator is anti-Hermitian, and it is not made Hermitian by multiplying by a c-number; a positive metric $\eta$ for a generator $G$ is a positive operator commuting with it, equivalently $\eta G\eta^{-1}=-G^{\dagger}$, and it is not unique. Every such metric endows the state space with its own inner product, and the same system then receives several descriptions with different mean values. In the two-level example of Blasi, Scolarici and Solombrino, with $\omega$ the real coefficient of the diagonal generator, $\Omega$ the complex off-diagonal coefficient and $z$ the off-diagonal parameter of the metric, the modulus of the mean value of the generator is $|\omega|/2$ under the plain inner product and $\sqrt{\omega^{2}/4+|z|^{2}\lvert\Omega\rvert^{2}}$ under the alternative one, and the two agree only as $|z|\to0$. The biquaternion theory has no family of this kind. A positive operator on the state module $S\cong\mathbb{C}^{2}$ that is to serve as a metric for the whole operator algebra must commute with every anti-Hermitian element, hence with all of $\mathsf{M}_{2}(\mathbb{C})$, hence is a scalar multiple of the identity, and such a multiple changes only the normalisation of the inner product. The forms of the biquaternion theory are fixed by the algebra and carry no parameter. The definite Hermitian form $\langle\tilde Q_1,\tilde Q_2\rangle_{*}$ pairs the states of the module, and its adjoint is the Hermitian adjoint owned by the probability band (*The Eight Derived Structures: Symmetric and Antisymmetric*); the indefinite Krein form $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$ pairs the gauge structure, and its adjoint is the J-adjoint owned by the gauge bands (*The Eight Derived Structures: Symmetric and Antisymmetric*). Neither form is one of a family, and neither offers a second reading of the same states. This is the non-commutativity limit once more, removed by the same centrality that removes the first.

**And the choice is not merely available, it is selected.** The corpus proves that a dynamics which preserves the Hermitian norm for **every** Hermitian generator forces its unit into the centre (*Unitarity from Centrality: The Biquaternion Norm-Preservation Theorem*). The central roots of $-e_t$ are $\pm i$, and a non-central unit fails: with the non-central unit $\vec e_z$ and $\tilde H=i\vec e_x$, the generator $\tilde H\vec e_z=-i\vec e_y$ is Hermitian rather than anti-Hermitian, so the norm grows. A uniform norm-preserving evolution therefore requires commutative scalars, and the biquaternion theory is what that requirement selects. This is why the fifth limit is treated below as a theorem rather than as a difficulty.

### The Spectrum Is the Ordinary Spectrum

**The limit addressed.** The eigenvalue of a general operator is a conjugacy class, and a representative, equivalently a complex structure, must be chosen (Part I, *The Spectrum Is a Set of Classes*).

**What the biquaternion theory does.** With the scalars in the centre, the state module $S\cong\mathbb{C}^{2}$ is a complex vector space, $\mathbb{B}$ is the algebra of complex-linear operators on it, and the observables, the elements of $\mathbb{M}_{+}$, are ordinary Hermitian operators. Their eigenvalues are real numbers, their eigenspaces are the orthogonal projectors, and the spectral theorem is the complex one. There are no conjugacy classes, because the scalars commute and an eigenvalue is a scalar.

The Born rule is the normalised Hermitian plain form; in the $2\times2$ image it is the trace pairing with the Hermitian form. With $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ positive definite, the Born weight of a transition is the normalised $\langle\tilde Q_1,\tilde Q_2\rangle_{*}$-pairing, and the positivity of $\langle\tilde Q_1,\tilde Q_2\rangle_{*}$ is what makes the weight a probability; the derivation is owned by *The Born Rule from the Plain Form — Derivation and Comparison*.

**What became of the complex structure.** In the quaternionic theory the complex structure was a choice forced by the spectral limit, and it had to be made operator by operator. In the biquaternion theory it is the scalar field itself. It is fixed once, in the centre, and it is the same structure for the whole theory. The corpus records that the Hermitian sector carries no intrinsic complex structure of its own (*What the Biquaternion Algebra Cannot Do*, in the sector-structure group); the reason the spectral theorem nonetheless applies is that the complex structure is carried by the scalar field and the module, which is where the theorem needs it.

**The diagonal, and the quaternionic constraint.** As in the quaternionic case, the diagonal of a Hermitian element is real. Here it is the ordinary statement about Hermitian matrices, with no quaternionic constraint attached, and it comes from the same Hermitian condition that the quaternionic theory had to impose separately.

### The Phase Is Abelian

**The limit addressed.** The phase group is $SU(2)$ instead of $\mathrm{U}(1)$, so interference is not the interference of the complex theory (Part I, *The Phase Is Non-Abelian*).

**What the biquaternion theory does.** The phase is generated by the central imaginary $i$. Its unit group is $\mathrm{U}(1)$, the phase of an amplitude is a point of the circle and not a point of $SU(2)$, two amplitudes combine with a relative complex phase, and interference is the standard interference, with the fringe pattern of the double-slit reproduced from the algebra. The corpus owns the central phase and its role as the algebra's continuous symmetry in *The Gauge Extension of the Central Phase: Why the Centre Caps the Group*, and the interference itself in *The Double-Slit Experiment in Biquaternionic Form*.

**What is given up here.** The units $\vec e_x,\vec e_y,\vec e_z$ still generate $SU(2)$, but they are not scalars, so they act as transformations of the representation rather than as phases of an amplitude. The non-abelian phase is not available to the biquaternion theory. Nothing physical is lost by that, because the non-abelian phase was the source of this limit.

### Composition: What Is Repaired and What Remains

**The limit addressed.** The scalars do not compose, $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{H}\cong M_{4}(\mathbb{R})\neq\mathbb{H}$, so the composition rule of quantum theory cannot be carried (Part I, *Composite Systems Do Not Compose*).

This is the one limit that has to be divided into two parts, and the division is exact.

**What is repaired: the scalars.** The scalar field of the biquaternion theory is $\mathbb{C}$, and
$$
\mathbb{C}\otimes_{\mathbb{C}}\mathbb{C}\cong\mathbb{C}.
$$
The scalars compose. The scalar-level composition limit, which is the form in which it closed the quaternionic programme, does not arise here at all.

**What remains: the observable algebra.** The algebra is not closed under the tensor product,
$$
\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}\cong M_{4}(\mathbb{C})\neq\mathbb{B},
$$
the dimensions being $16\neq4$. A pair of two-state systems does not have $\mathbb{B}$ as its algebra, and the corpus records this as a numbered obstruction (*What the Biquaternion Algebra Cannot Do: A Catalogue of Algebraic Obstructions*, entry O13).

**The clarification that matters for the comparison.** This residue is the standard situation in quantum mechanics, and not a defect of the biquaternion choice. In ordinary quantum mechanics
$$
M_{2}(\mathbb{C})\otimes_{\mathbb{C}}M_{2}(\mathbb{C})\cong M_{4}(\mathbb{C})\neq M_{2}(\mathbb{C}),
$$
for the same dimensional reason, and it is not treated as an obstruction there, because composition is defined on the **state spaces**: the state space of a pair is the tensor product of the state spaces, and the algebra of the pair is an algebra of operators on that product rather than the algebra of a single system. The enlargement is the ordinary situation: no matrix algebra of more than one dimension is closed under the tensor product, in any quantum theory.

**How the biquaternion theory handles it.** In three steps, all of them explicit in the corpus.

- **The algebra is a one-mode algebra.** $\mathbb{B}$ is the observable algebra of one internal mode, one two-state system, and this is the corpus's one-mode reading of the theory rather than a defect to be repaired.
- **Composition is carried by the module.** The state space of $n$ modes is the tensor power $S^{\otimes n}$, and the many-mode arena is the tensor tower built over $S$, with $\mathbb{B}\otimes\mathbb{B}\cong M_{4}(\mathbb{C})$ appearing as the two-mode algebra. This is the standard construction, and it is the one ordinary quantum mechanics uses.
- **The obstruction is recorded on the strongest reading.** The catalogue's entry O13 states the algebra's non-closure as an obstruction, and it is an obstruction precisely against the reading in which the single algebra is the whole theory. On the module reading, which the corpus adopts and which ordinary quantum mechanics also uses, it is the normal arrangement.

**What remains a genuine limit.** $\mathbb{B}$ is a one-mode algebra, so the many-mode theory is a construction over it and not the algebra itself. The corpus states this, and it is the reason the biquaternion theory's finite content is one fermionic mode (*Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, by way of the catalogue's one-mode reading).

### The Forced Complex Structure Becomes a Theorem

**The limit addressed.** Consistency forces a complex structure, and no experiment separates the quaternionic theory from ordinary quantum mechanics (Part I, *The Conclusion Reached by the Programme Itself*).

**What the biquaternion theory does.** It does not treat the conclusion as a defeat. It takes the conclusion as the definition of the theory. The complex structure is placed at the centre from the outset, the scalar field is $\mathbb{C}$, the phase is central, and the spectral theorem is the ordinary complex one. The consistency requirement that the programme discovered is then proved inside the biquaternion algebra as the forcing theorem of *Unitarity from Centrality*, where a uniform norm-preserving evolution is shown to leave the unit no place but the centre. The finding that ended the quaternionic programme is a theorem of its successor.

**What this means for prediction, stated plainly.** The corpus does not claim a quaternionic signature, and it says why. Its empirical position is that the framework is equivalent to standard physics on the domains it reformulates, and *The Empirical Status of the Biquaternion Framework* states that position and lists what a signature would have to look like. Part I's fifth limit is therefore neither removed nor denied. It becomes the biquaternion theory's own statement about its observables, made before the reader discovers it. That is the honest form of the continuity between the two theories, and it is the price named at the end of this part.

## What the Theory Keeps of the Quaternions

The biquaternion theory would be empty if it discarded the quaternion structure, and it does not. It keeps the structure in the place where it does the work and does no harm: the quaternion units, the rotations they generate, and the geometry. Each item below is a part of the quaternionic achievement that survives, together with the reason it survives.

### The Units Are the Rotation Generators

The units of the quaternion algebra are $SU(2)$, the double cover of the rotation group, and they remain so in the biquaternion theory. With the matrix model above, the elements
$$
\tilde S_{k}=\tfrac{\hbar}{2}\,i\,\vec e_k
$$
have the images $\mathsf{M}_2(\tilde S_{k})=\tfrac{\hbar}{2}\sigma_{k}$, the spin operators, and they satisfy
$$
[\tilde S_{i},\tilde S_{j}]=i\hbar\sum_{k}\epsilon_{ijk}\tilde S_{k}.
$$
This was checked on the corpus's matrix model for the two values $\hbar=1$ and $\hbar=2.7$ and for every pair of indices, and the same check confirms the quaternion bracket $\mathsf{M}_2([\vec e_j,\vec e_k])=2\epsilon_{jkl}\mathsf{M}_2(\vec e_l)$, which is the bracket Part I records for the imaginary units $i,j,k$. The spin achievement of the quaternionic theory is therefore kept **exactly**: the units are still $SU(2)$ and still the rotation generators. What has changed is only their role. In the quaternionic theory they multiplied the states as scalars; here they generate the representation, which is the angular-momentum algebra of the corpus. The bracket is owned by *Angular Momentum and Spin in Biquaternionic Form*.

### The Material Sector Is Spacetime

The older role of the quaternions is geometry, and the biquaternion theory keeps it in the material sector. The anti-Hermitian sector is Minkowski space,
$$
\mathbb{M}_{-}\cong\mathbb{R}^{3,1},
$$
with the biquaternion norm $\langle\cdot\rangle_{\natural}$ as the interval, the pure imaginary directions as space, the central imaginary as the source of the sign, and the unit-norm elements as the Lorentz transformations. On $\mathbb{M}_{-}$ all four forms are real and $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=-\langle\tilde Q_1,\tilde Q_2\rangle$, so the definite form and the indefinite form differ by a sign there, which is the precise statement of how the Euclidean structure and the Lorentzian structure sit together in one algebra. This is the quaternions' classical role, kept in full. The sector identification is owned by *The Anti-Hermitian Subspace $\mathbb{M}_{-}$ as the Material Sector*.

### Associativity, Centrality, and the Explicit Formalism

The quaternionic theory was built on an associative algebra, and the biquaternion theory keeps associativity and adds centrality. Because $\mathbb{B}$ is central simple over $\mathbb{C}$, it is a full matrix algebra, and every result of finite-dimensional complex linear algebra and representation theory is available without qualification. The four forms $\langle\tilde Q_1,\tilde Q_2\rangle,\langle\tilde Q_1,\tilde Q_2\rangle_{\natural},\langle\tilde Q_1,\tilde Q_2\rangle_{*},\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$, the trace convention $\mathrm{Tr}=2\,\mathrm{Sc}$, the matrix model $\mathsf{M}_2$, and the two sector dictionaries together give an explicit finite-dimensional formalism with **no unbounded operators and no domain questions at the level of the algebra**. That explicitness is a genuine inheritance from the quaternionic programme, which also worked with finite-dimensional operators rather than with the analytic machinery of the complex theory. The conventions and the four forms are owned by *Conventions in the Biquaternion Universe*.

### The Quaternions Survive Inside the Algebra

The quaternion algebra is not replaced in the biquaternion theory; it is a real form of it. The complex algebra $M_{2}(\mathbb{C})$ has two real forms, the compact one and the split one, and correspondingly the real forms of the biquaternion algebra are the quaternions and the split quaternions:
$$
\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{B},\qquad \mathbb{H}_{\mathrm{s}}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{B},
$$
where $\mathbb{H}_{\mathrm{s}}$ is the split quaternion algebra ($\mathbb{H}_{\mathrm{s}}\cong M_{2}(\mathbb{R})$), in the notation of the mathematical corpus. The quaternions are therefore present twice over: as the compact real form, and concretely inside $\mathbb{B}$ as the four-dimensional real subalgebra $\mathbb{H}_{\mathbb{B}}=\mathbb{R}\text{-span}\{e_t,\vec e_x,\vec e_y,\vec e_z\}\cong\mathbb{H}$, the corpus's real-quaternion subspace, whose four coefficients are real and which carries the material space together with the informational time. The framework does not discard the quaternions; it stops using them as scalars. The two real forms are different real algebras with different physics: $\mathbb{H}$ carries the compact structure, and $\mathbb{H}_{\mathrm{s}}$ the split one. The corpus works on both, so the quaternion algebra is present in the biquaternion theory under its own name, as one of the two real forms of the complexified algebra. The split branch is owned by the corpus's articles on complex split biquaternions, among them *Left-Right Symmetric Fermions from Complex Split Biquaternions and Bioctonions*.

### The Two-State Structure

The natural home of the quaternionic theory was a single system with $SU(2)$ symmetry, and that is the biquaternion theory's exact finite content. The Hermitian sector $\mathbb{M}_{+}$ is the observable algebra of one two-state system, the states are the trace-one elements of its positive cone, the state space is the Bloch ball, the imaginary units $\vec e_x,\vec e_y,\vec e_z$ are the three axes of the Bloch vector, and the Born rule is the pairing $\langle\tilde Q_1,\tilde Q_2\rangle_{*}$ on the defining module $S\cong\mathbb{C}^{2}$. Nothing of the quaternionic theory's two-state content is lost; it is made the exact finite content of the successor. This is owned by *The Native Qubit and the Defining Module of the Biquaternion Algebra*.

### The Scalar Field Is an Input, and the Corpus Says Which Input

The programme's foundational lesson was that the scalar field is an input to a quantum theory and not a theorem about its propositions. The biquaternion theory keeps the lesson and answers the question the lesson raises, because it proves which input a norm-preserving dynamics selects: the unit is forced into the centre, and the centre is $\mathbb{C}$. That finding is owned by *Unitarity from Centrality: The Biquaternion Norm-Preservation Theorem*.

## The Price and the Boundary

The repairs and the price are one fact, and the price is stated here rather than left to be discovered.

- **No position operator.** The observable algebra is finite-dimensional and internal, so the canonical commutation relation cannot be written inside it. Position is not an element of the algebra; it enters as the argument of the field and as the dual variable of the transform, with the carrier of the transform infinite-dimensional while the algebra stays finite. The obstruction, and the precise sense in which the theory is independent of the relation, are owned by *The Biquaternion Framework and the Canonical Commutation Relation: Independence, Not a Defect*.
- **No scale.** The algebra is dimensionless and contains no length, time or action; a scale enters as a conventional unit and is not fixed by the algebra. This is recorded in §*Physical Units* of *Conventions in the Biquaternion Universe* and in the empirical assessment below.
- **One mode.** The observable algebra is the algebra of one internal mode, so the many-mode theory is a construction over it and not the algebra itself. This is the residue of the composition limit discussed above.
- **No distinguishing prediction.** The complexification that repairs the first three limits of Part I is the same step that removes the quaternionic departures which would have been a signature. The corpus states its position as empirical equivalence on the domains it reformulates, in *The Empirical Status of the Biquaternion Framework*, which also lists what a signature would have to look like.

**The trade in one sentence.** A theory that keeps the quaternions as its scalar field has the limits of Part I. A theory that takes the complex numbers as its scalars and keeps the quaternion units as generators has the predictions of ordinary quantum mechanics and the boundary above. The biquaternion theory makes the second choice, and that choice is the whole of the improvement.

## Ledger

The first table is the correspondence of Part II: each limit of Part I, what the biquaternion theory does about it, and where this corpus works it out. The second table is the inheritance: each part of the quaternionic achievement that is kept, and where it lives.

| Limit of the quaternionic theory | What the biquaternion theory does | Where this corpus owns it |
|---|---|---|
| The scalars do not commute, so the standard formalism is not reproduced | The scalar field is the centre $Z(\mathbb{B})=\mathbb{C}e_t$, commutative and algebraically closed; the algebra is central simple over $\mathbb{C}$ | *Conventions in the Biquaternion Universe* |
| The eigenvalue of a general operator is a conjugacy class, and a representative must be chosen | The scalars commute, the state module is a complex vector space and the eigenvalues are numbers; the complex structure is the scalar field, fixed once for the whole theory | *The Born Rule from the Plain Form*; *The Native Qubit and the Defining Module* |
| The phase group is $SU(2)$, so interference is not the interference of the complex theory | The phase is generated by the central imaginary, whose unit group is $\mathrm{U}(1)$; amplitudes combine with a relative complex phase and the interference is standard | *The Gauge Extension of the Central Phase*; *The Double-Slit Experiment in Biquaternionic Form* |
| The scalars do not compose, $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{H}\cong M_{4}(\mathbb{R})\neq\mathbb{H}$ | The scalars compose, $\mathbb{C}\otimes_{\mathbb{C}}\mathbb{C}\cong\mathbb{C}$; the algebra is not closed under the tensor product, $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}\cong M_{4}(\mathbb{C})$, which is the standard situation for every matrix algebra and is carried on the module | *What the Biquaternion Algebra Cannot Do* (O13) |
| Consistency forces a complex structure, and no experiment separates the theory from ordinary quantum mechanics | The forced complex structure is the starting point of the theory, and the forcing is proved as a theorem; the empirical position is stated openly | *Unitarity from Centrality*; *The Empirical Status of the Biquaternion Framework* |

| Part of the quaternionic achievement | Where it lives in the biquaternion theory | Where this corpus owns it |
|---|---|---|
| The units are $SU(2)$ and the rotation generators | The elements $\tilde S_{k}=\tfrac{\hbar}{2}i\vec e_k$ are the spin operators, with $[\tilde S_{i},\tilde S_{j}]=i\hbar\sum_{k}\epsilon_{ijk}\tilde S_{k}$ | *Angular Momentum and Spin in Biquaternionic Form* |
| The Lorentz group and Minkowski space | $\mathbb{M}_{-}\cong\mathbb{R}^{3,1}$, the interval is the biquaternion norm, and the unit-norm elements are the Lorentz transformations | *The Anti-Hermitian Subspace $\mathbb{M}_{-}$ as the Material Sector* |
| An associative algebra with an explicit finite-dimensional formalism | $\mathbb{B}\cong M_{2}(\mathbb{C})$, the four forms $\langle\tilde Q_1,\tilde Q_2\rangle,\langle\tilde Q_1,\tilde Q_2\rangle_{\natural},\langle\tilde Q_1,\tilde Q_2\rangle_{*},\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$, the trace convention $\mathrm{Tr}=2\,\mathrm{Sc}$, and no unbounded operators at the algebra level | *Conventions in the Biquaternion Universe* |
| The quaternion algebra itself | $\mathbb{H}$ is the compact real form of $\mathbb{B}$ and the real subalgebra $\mathbb{H}_{\mathbb{B}}\subset\mathbb{B}$; the split quaternions are the other real form | the corpus's split-biquaternion articles |
| A single system with $SU(2)$ symmetry as the natural home | $\mathbb{M}_{+}$ is the observable algebra of one two-state system, with the Bloch ball and the Born rule as the $\langle\tilde Q_1,\tilde Q_2\rangle_{*}$-pairing | *The Native Qubit and the Defining Module of the Biquaternion Algebra* |
| The scalar field is an input to a quantum theory | The corpus proves which input a uniform norm-preserving dynamics selects, namely the centre | *Unitarity from Centrality* |

## Physical Readings

- **The programme's difficulty was placement, and not arithmetic.** Every limit of Part I is a limit of putting $\mathbb{H}$ where the scalar field goes. None of them is a limit of the quaternion units, which are elements that generate the rotations. The biquaternion theory keeps the units and gives up the scalar field, and that single move accounts for the whole of the comparison.
- **The decisive limit has a scalar form and an algebra form, and they must not be confused.** The scalar form, $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{H}\neq\mathbb{H}$, is repaired by complexifying. The algebra form, $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}\neq\mathbb{B}$, remains, and it is the ordinary non-closure of a matrix algebra under the tensor product, which ordinary quantum mechanics shares and does not treat as an obstruction. The corpus records its own version as a numbered obstruction against the strongest reading of the theory. This division is the clearest available answer to the question of what belongs to the quaternionic theory, what belongs to this corpus, and what belongs to standard physics.
- **The spectral limit is the one most often misstated.** Quaternionic Hermitian matrices do have a real spectrum and do diagonalise, and the check is reproduced above under the regular representation. What the limit really is, is that a complex structure must be chosen before a spectrum can be written for a general operator. The biquaternion theory's entire strategy is to make that choice once, in the scalar field, instead of making it operator by operator.
- **The programme's own conclusion is adopted rather than answered.** Consistency forces a complex structure. The biquaternion theory begins from that structure and proves the forcing as a theorem of its own algebra. The absence of a quaternionic prediction is therefore a consequence of the repair and not a separate deficiency, and the corpus states it in the same place where it states its positive results.
- **The correspondence principle is another face of the same placement.** In its anti-Hermitian field-theory formulation (Adler 1986) the placement of $\mathbb{H}$ where the scalar field goes surfaces as a physical difficulty rather than a formal one: there the correspondence principle breaks down on all three of its routes. The Ehrenfest theorem fails, because the canonical momenta are not quaternion real and no analogue relates $d^{2}\langle\varphi\rangle/d{t'}^{2}$ to the mean force; Feynman's identity fails, because the quaternion units at one time do not commute; and the stationary-phase approximation fails, because the three real components of a quaternionic action are not stationary on the same trajectories. A classical limit is reached only by projecting onto a chosen complex substructure, which then has the ordinary complex limit. **The breakdown belongs to that formulation and not to quaternion-valued wave functions as such.** A later non-anti-Hermitian formulation of quaternionic quantum mechanics, with a real scalar product, reports a well-defined classical limit of its own, and the same programme carries a Virial theorem; what the placement of $\mathbb{H}$ fixes is therefore not whether a classical limit exists, but where the complex structure that supplies it is chosen. The biquaternion theory takes that projection from the start: its complex structure is the centre $Z(\mathbb{B})=\mathbb{C}e_t$, supplied by the algebra and not chosen, and its classical limit as stationary phase is proved for it in *The Action Principle and the Classical Limit as Stationary Phase in Biquaternionic Form*. The same field-theory form carries a second warning. There the second-order fermion forces an indefinite-metric **state** space, with zero-norm states and a physical subspace; in the corpus the indefinite forms — the norm $\langle\cdot\rangle_{\natural}$ as the metric of the material sector and the Krein form $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$ as the gauge pairing — are never state spaces, and only the definite form $\langle\tilde Q_1,\tilde Q_2\rangle_{*}$ pairs states.
- **What is kept is the geometry.** The units remain the rotation generators and the unit-norm elements remain the Lorentz transformations, so the part of the quaternion tradition that never had a scalar-field problem, the geometry of rotations and of spacetime, is kept in full. It is also the part that the biquaternion theory's physics actually uses.
- **The word "improvement" is used in the sense of a successor.** The quaternionic theory was not refuted and was not incoherent. It could not meet the first three requirements while keeping its scalars, could meet the fourth only in its scalar form, and its own analysis supplied the fifth. The biquaternion theory removes the first three by the one change a successor can make, repairs the fourth in its scalar form, adopts the fifth as a theorem and as a stated position, and keeps the algebra and the geometry. That is the sense in which it is the improvement, and the price is named with it.

## Summary

Quaternionic quantum theory is the theory obtained by making the quaternion algebra $\mathbb{H}$ the scalar field of quantum mechanics, with $\mathbb{H}$-valued inner products on right $\mathbb{H}$-modules, $\mathbb{H}$-linear self-adjoint observables, an anti-self-adjoint generator of the evolution, and a real transition probability built from a quaternionic amplitude. It was founded by Finkelstein, Jauch, Schiminovich and Speiser in 1962 and developed to full length by Adler in 1995, and it is a finished formalism rather than a sketch. Its achievements are four: a complete theory of states, observables, probabilities and dynamics; the foundational result that the scalar field is an input rather than a consequence of the propositional structure, since the reconstructions of Piron and of Soler admit $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$ while Birkhoff and von Neumann's commutativity requirement selects $\mathbb{C}$ among them; the embedding of spin and of the rotation group directly in the scalars, the unit quaternions being $SU(2)$; and the incorporation of the Lorentz group and of Minkowski space, which is the classical role of the quaternions. Its limits are five. The scalars do not commute, so the standard formalism is not reproduced, and every other limit follows from that one. The spectrum of a general operator is a set of conjugacy classes rather than a set of numbers, since a quaternionic eigenvalue is defined only up to conjugation by a unit, and choosing a representative is choosing a maximal commutative subfield, which is isomorphic to $\mathbb{C}$; the spectral theorem itself holds for Hermitian matrices, with a real spectrum, and the widespread claim that it does not is incorrect. The phase group is $SU(2)$ rather than the circle $\mathrm{U}(1)$, so interference is no longer the interference of the complex theory. Composite systems do not compose, since $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{H}\cong M_{4}(\mathbb{R})\neq\mathbb{H}$, and this is the decisive limit, because the composition rule of quantum theory cannot be relaxed the way a convention can; it is also the reason the quaternionic departures are unavailable in composite systems. And the programme's own analysis found that consistency forces a complex structure on the state space, after which the theory is complex quantum mechanics with additional sectors and no experimental separation from it. The biquaternion theory of this corpus begins at that conclusion. Its algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_{2}(\mathbb{C})$, whose centre is $\mathbb{C}e_t$, so its scalars are the complex numbers and the quaternion units survive as elements of the algebra and as its rotation generators rather than as its field. Three of the five limits are removed outright by that one change: the scalars commute, so the inner product, the spectral equations and the propositional calculus have one reading each; the state module is a complex vector space, so the spectral theorem is the ordinary complex one and the Born rule is the pairing with the positive-definite Hermitian form $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$; and the phase is generated by the central imaginary, so its unit group is $\mathrm{U}(1)$ and interference is standard. The fourth limit is repaired in its scalar form, since $\mathbb{C}\otimes_{\mathbb{C}}\mathbb{C}\cong\mathbb{C}$, and remains in its algebra form, $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}\cong M_{4}(\mathbb{C})\neq\mathbb{B}$, which is the ordinary non-closure of a matrix algebra under the tensor product and is carried on the state module, with the corpus recording its own version as a numbered obstruction against the strongest reading of the theory. The fifth limit is adopted and proved: the corpus shows that a dynamics preserving the Hermitian norm for every Hermitian generator forces its unit into the centre, so the complex structure that the quaternionic requirements forced is a theorem of the successor. What is kept is the geometry and the representation theory: the units are the rotation generators with $[\tilde S_{i},\tilde S_{j}]=i\hbar\sum_{k}\epsilon_{ijk}\tilde S_{k}$, the material sector $\mathbb{M}_{-}$ is Minkowski space with the interval as the biquaternion norm and the Lorentz transformations as the unit-norm elements, the algebra is central simple over $\mathbb{C}$ and therefore fully explicit and finite-dimensional, the quaternions survive as its compact real form and as the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}\subset\mathbb{B}$, beside the split quaternions, and the two-state system with $SU(2)$ symmetry is its exact finite content. The price, stated in the same breath as the repairs, is that a theory whose scalars are already complex agrees with ordinary quantum mechanics instead of departing from it: it has no position operator inside the algebra, no scale, one mode, and no distinguishing prediction. The biquaternion universe is therefore the improvement of the quaternionic quantum theory in the sense of its corrected successor: the same algebra, the same geometry, the one changed placement that removes three limits and repairs a fourth, and the honest statement of the fifth.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra; associative, non-commutative, a division ring |
| $\mathbb{H}_{\mathbb{B}}=\mathbb{R}\text{-span}\{e_t,\vec e_x,\vec e_y,\vec e_z\}$ | The real-quaternion subspace, the subalgebra of $\mathbb{B}$ isomorphic to $\mathbb{H}$ |
| $\mathbb{H}_{\mathrm{s}}$ | The split quaternion algebra, $\cong M_{2}(\mathbb{R})$; the second real form of $\mathbb{B}$ |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_{2}(\mathbb{C})$ | The biquaternion algebra; central simple over $\mathbb{C}$ |
| $Z(\mathbb{B})=\mathbb{C}e_t$ | The centre; the scalar field of the biquaternion theory |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | The basis, with $e_t=1$ and $\vec e_k^{2}=-e_t$ |
| $i$ | The central scalar imaginary, commuting with every $\vec e_k$ |
| $\overline{\cdot}$, ${}^{\natural}$, ${}^{*}$ | The coefficientwise conjugation, the natural conjugation, and the Hermitian conjugation ${}^{*}=\overline{\cdot}\circ{}^{\natural}$ |
| $\mathbb{M}_{+}$, $\mathbb{M}_{-}$ | The Hermitian and anti-Hermitian sectors, the fixed spaces of ${}^{*}$ |
| $\mathbb{M}_{-}\cong\mathbb{R}^{3,1}$ | The material sector as Minkowski space |
| $\mathsf{M}_2(e_t)=I_{2}$, $\mathsf{M}_2(\vec e_k)=-i\sigma_{k}$ | The matrix model of $\mathbb{B}$ onto the $2\times2$ complex matrices |
| $\mathrm{Sc}$, $\mathrm{Tr}=2\,\mathrm{Sc}$ | The scalar part, the coefficient of $e_t$, and the trace convention |
| $\langle\tilde Q_1,\tilde Q_2\rangle,\langle\tilde Q_1,\tilde Q_2\rangle_{\natural},\langle\tilde Q_1,\tilde Q_2\rangle_{*},\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$ | The four forms: $\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)$, $\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$, $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})$ |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=\sum_{\mu}Q_{1\mu}\overline{Q_{2\mu}}$ | The Hermitian form; positive definite, linear in the first slot and conjugate-linear in the second |
| $\langle\cdot\rangle_{\natural}$ | The biquaternion norm; the Minkowski interval on $\mathbb{M}_{-}$ |
| $S\cong\mathbb{C}^{2}$ | The defining state module, with $\mathbb{B}\cong\mathrm{End}(S)$ |
| $\tilde S_{k}=\tfrac{\hbar}{2}i\vec e_k$ | The spin generators, with $[\tilde S_{i},\tilde S_{j}]=i\hbar\sum_{k}\epsilon_{ijk}\tilde S_{k}$ |
| $R(q)$ | The regular representation of $q=a+bi+cj+dk$ (Part I; there $i,j,k$ are Hamilton's quaternion units): $R(q)_{11}=a+bi$, $R(q)_{12}=c+di$, $R(q)_{21}=-c+di$, $R(q)_{22}=a-bi$ |
| $uqu^{-1}$ | The conjugacy class of a quaternionic eigenvalue (Part I); a two-sphere for $q\notin\mathbb{R}$ |
| $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{H}\cong M_{4}(\mathbb{R})$ | The non-composition of the quaternionic scalar field |
| $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}\cong M_{4}(\mathbb{C})$ | The composition residue of the biquaternion algebra |
| $\mathrm{Br}(\mathbb{R})=\mathbb{Z}/2$ | The Brauer group of $\mathbb{R}$; $\mathbb{H}$ has order two in it |

## Further Reading

- D. Finkelstein, J. M. Jauch, S. Schiminovich and D. Speiser, "Foundations of Quaternion Quantum Mechanics", *Journal of Mathematical Physics* **3** (1962) 207–220, for the original construction of quantum theory over the quaternions.
- S. Adler, *Quaternionic Quantum Mechanics and Quantum Fields* (Oxford University Press, 1995), for the complete development of the programme, its unitarity and stability conditions, and the finding that consistency forces a complex structure. The field-theory form of the programme is in S. L. Adler, "Quaternionic Quantum Field Theory", *Communications in Mathematical Physics* **104** (1986) 611–656, for the boson–fermion degree matching, the second-order fermion, the forced indefinite metric, and the breakdown of the correspondence principle.
- G. Birkhoff and J. von Neumann, "The logic of quantum mechanics", *Annals of Mathematics* **37** (1936) 823–843, for the commutativity requirement on the coefficient field of the propositional calculus.
- C. Piron, *Foundations of Quantum Physics* (Benjamin, 1976), for the reconstruction of quantum theory from the propositional lattice and the admissible coefficient fields.
- M. P. Soler, "Characterization of Hilbert spaces by orthomodular spaces", *Communications in Algebra* **23** (1995) 219–243, for the infinite-dimensional reconstruction admitting the real, complex and quaternionic cases.
- D. R. Farenick and B. A. F. Pidkowich, "The spectral theorem in quaternions", *Linear Algebra and its Applications* **371** (2003) 75–102, for the diagonalisation of quaternionic Hermitian matrices and the structure of quaternionic spectra.
- B. Farb and R. K. Dennis, *Noncommutative Algebra* (Springer, 1993), for the tensor product of matrix algebras, the splitting of $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{H}$, and the Brauer group of $\mathbb{R}$.
- A. Hurwitz, "Über die Composition der quadratischen Formen von beliebig vielen Variabeln", *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen* (1898) 309–316, for the theorem that there are exactly four normed division algebras.
- W. R. Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original algebra and its geometry of rotations.
- S. Giardino, "Quaternionic quantum mechanics in real Hilbert space", *Journal of Geometry and Physics* **158** (2020) 103956 (arXiv:1803.11523), for a non-anti-Hermitian formulation in which the wave functions are quaternionic and the scalar product is real, with a real expectation value for every operator, real eigenvalues only, a well-defined classical limit, and a quaternionic Fourier series on a basis of unit quaternions. The same programme's Virial theorem is in his "Virial theorem and generalized momentum in quaternionic quantum mechanics", *The European Physical Journal Plus* **135** (2020) 114 (arXiv:1911.06831).
- A. Blasi, G. Scolarici and L. Solombrino, "Alternative descriptions in quaternionic quantum mechanics", *Journal of Mathematical Physics* **46** (2005) 042104 (arXiv:quant-ph/0407158), for the several positive metrics a single quaternionic generator admits, for the unique metric of an irreducible generating set, and for the two-level example whose metric family changes the mean values.
- M. A. Graydon, "Quaternionic quantum dynamics on complex Hilbert spaces", *Foundations of Physics* **43** (2013) 656–664 (arXiv:1103.3547), for the exact representation of quaternionic channels and POVMs by complex maps on a doubled space with the selecting structure retained.
- H. Barnum, M. A. Graydon and A. Wilce, "Composites and Categories of Euclidean Jordan Algebras", *Quantum* **4** (2020) 359, for the several incompatible composite frameworks of quaternionic systems and the categorical boundaries that separate them.

