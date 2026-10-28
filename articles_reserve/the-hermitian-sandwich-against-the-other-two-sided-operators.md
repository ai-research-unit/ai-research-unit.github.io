# __The Hermitian Sandwich Against the Other Two-Sided Operators__

## Introduction

The physics corpus calls one operator *the* sandwich, the Hermitian sandwich $\Theta_Q(X)=Q\,X\,Q^{*}$, and it writes a family of other forms that resemble it. This article identifies each form and states, for the occurrences that remain, why the Hermitian sandwich cannot stand in its place.

The arithmetic of the question is settled. Write an element in its polar word $\tilde Q=r\,e^{i\alpha}B\tilde u$, with $B$ the Hermitian positive boost factor and $\tilde u$ the unit real rotor. Then

$$
\tilde Q\tilde Q^{*}=r^{2}B^{2},
$$

so $\tilde Q\tilde Q^{*}$ is a positive scalar exactly when $B=e_t$. Inner conjugation and the Hermitian sandwich therefore agree **exactly on the boost-free class** $\mathbb R_{>0}\cdot U(2)$, and differ everywhere else.

The arithmetic is necessary but not sufficient. A formula also names an object: a gauge transformation is used as an automorphism of the algebra, a rotation of a vector as a congruence of its Hermitian form, and the same number can be the value of two maps of different type. Replacing an automorphism by a congruence is a change of subject, even when the two agree on the parameter at hand. The rule of this article is therefore:

> Replace only where the article uses the map as a transport of an object — a state, a field, a vector — and never where it uses the map as an automorphism.

The transports that pass that test now carry the Hermitian sandwich. What remains is nineteen occurrences in nine articles: nine **conceptually different**, where the parameter is unitary, the two maps agree numerically, and the formula still states an automorphism; and ten **structurally impossible**, where no parameter gives the map, or the claim ranges over a domain on which the two differ.

The GNS construction is no longer in the count. It has been rewritten in Hermitian form in [The Hermitian GNS Construction in the Biquaternion Framework](../articles_physics/the-hermitian-gns-construction-in-the-biquaternion-framework.html): the state is the Hermitian pairing $\omega(\tilde Q_3)=\mathrm{Tr}(\tilde{Ϛ}\tilde Q_3)$, the modular Hamiltonian is $K_{\tilde{Ϛ}}=-\log\tilde{Ϛ}\in\mathbb{M}_+$, and the modular operator is $\Delta_{\tilde{Ϛ}}=L_{e^{-K}}R_{e^{K}}$. The issue is solved and the entry is removed.

The Spectral Regularity article is also solved, by writing its central-element formula on the unitary slice. The claim in words stays "fixed by every inner automorphism", which for a central element holds for every unit. The displayed form, $\tilde U\tilde Q\tilde U^{*}=\tilde Q$ for every unitary $\tilde U$, is the Hermitian-adjoint form, and on that slice the adjoint is the inverse. The superselection reading is unchanged. It is removed from the count.

The Lorentz article is purged as well, without changing what its formulas mean. The general norm automorphism is written $T_{A,B}\tilde Q=A\tilde QB^{*}$ with $\det A\,\overline{\det B}=1$, and the inner automorphisms are the subfamily $AB^{*}=I$. The right factor is still an independent parameter; it is constrained to be the adjoint-inverse of the left, so the map remains an automorphism of the algebra and is not replaced by a single-parameter congruence. The rotor action was already the Hermitian sandwich. Its three occurrences are removed from the count.

The reflection formula in *Frames, Rotations and the Lorentz Group* is purged as well. The parameter is a real unit vector $v$ of the spatial slice, so $v^{*}=v$ and $v^{2}=-e_t$. The reflection is the Hermitian sandwich $\rho_v(X)=vXv^{*}=\Theta_v(X)$; the spacelike normal makes it minus the inner automorphism by $v$. The two occurrences are removed from the count.

The Pin action in *The Reflection and the Rotation in Biquaternionic Form* is purged as well. It is now written $\rho(u):x\mapsto-\epsilon(u)\,u\,x\,u$ with $u^{2}=\epsilon(u)I_4$ and $\epsilon(u)=\pm1$; a unit normal has inverse $\epsilon(u)u$, so the formula uses only the Clifford product and the sign of the normal. The article's one occurrence is removed from the count.

The chiral articles are purged as well. *Custodial Symmetry*, *The Nonlinear Sigma Model* and *The Pion and the Chiral Lagrangian* now write $g_LXg_R^{*}$ and $X^{*}dX$ throughout. On the unit real quaternions, where $g^{*}=g^{-1}$, the formulas keep their meaning, and the two-parameter action is an adjoint sandwich on both sides, so it is not a non-Hermitian operator. The three articles are removed from the count; each carries a short note stating why the second parameter is needed for its physics.

The gauge field strength is the archetype of the first class. On $SU(2)$, $\tilde U F_{\mu\nu}\tilde U^{-1}$ and $\tilde U F_{\mu\nu}\tilde U^{*}$ are the same number; the first is the adjoint law that makes the covariant derivative covariant and the Bianchi identity hold, and the second is a congruence that would rescale the field and break the bracket. Replacing it is not a notation change; it is a different gauge theory. It is treated in full in §*The Gauge Case in Detail*.

## The Two-Sided Operators

The general two-sided operator with two independent parameters is

$$
T_{a,b}(X)=a\,X\,b=L_a\circ R_b .
$$

The theory writes six distinguished members.

| name | form | right factor |
|---|---|---|
| Hermitian sandwich | $\Theta_Q(X)=Q\,X\,Q^{*}$ | the adjoint of the left factor |
| inner conjugation | $\mathrm{Ad}_Q(X)=Q\,X\,Q^{-1}$ | the inverse |
| natural sandwich | $Q\,X\,Q^{\natural}$ | the quaternion conjugate |
| signed Hermitian sandwich | $\Theta^{\alpha}_Q(X)=\alpha(Q)\,X\,Q^{*}$ | adjoint, with the parity twist on the left |
| signed inner conjugation | $\mathrm{Ad}^{\alpha}_Q(X)=\alpha(Q)\,X\,Q^{-1}$ | inverse, with the parity twist on the left |
| two-parameter adjoint sandwich | $g_L\,X\,g_R^{*}$ | an independent right parameter, itself an adjoint |

The star on the argument gives a seventh object, the sesquilinear sandwich $S_{a,b}(X)=a\,X^{*}\,b=T_{a,b}\circ{}^{*}$. It is conjugate-linear in $X$ and is not a member of the family above.

The naming is fixed by *The Element and Operator Representations*: there the sandwich is defined as the two-sided operator whose right parameter is the Hermitian conjugate of the left, and the general two-sided operator is introduced in the same section. The general theory is *The Hermitian Sandwich on a Hermitian Algebra with Hermitian Adjoint*, its biquaternion instance *The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint*, its indefinite counterpart *The Hermitian Sandwich on a Krein Space*, and the two-parameter family *The Sesquilinear Sandwich Operator*.

## The Algebraic Criterion

**Proposition.** Let $Q,R$ be units of $\mathbb B$. Then $\Theta_R=\mathrm{Ad}_Q$ if and only if there is $\lambda\in\mathbb C^{\times}$ with

$$
R=\lambda\,Q,\qquad Q\,Q^{*}=\lvert\lambda\rvert^{-2}e_t\in\mathbb R_{>0}\,e_t .
$$

*Proof.* The two-sided operators obey $T_{a,b}=T_{c,d}$ if and only if there is a central unit $p$ with $c=ap$ and $d=p^{-1}b$; this is the kernel of the two-parameter family. Apply it to $(a,b)=(Q,Q^{-1})$ and $(c,d)=(R,R^{*})$: $R=Qp$ and $R^{*}=p^{-1}Q^{-1}$. Multiplying gives $RR^{*}=e_t$, so $R$ is of norm one, and $R=\lambda Q$ with $\lambda=p$. The norm condition reads $\lvert\lambda\rvert^{2}QQ^{*}=e_t$, that is $QQ^{*}=\lvert\lambda\rvert^{-2}e_t$. Conversely, if $R=\lambda Q$ and $QQ^{*}=\lvert\lambda\rvert^{-2}e_t$, then $Q^{*}=\lvert\lambda\rvert^{-2}Q^{-1}$ and $R^{*}=\bar\lambda Q^{*}=\lambda^{-1}Q^{-1}$, so $\Theta_R=\mathrm{Ad}_Q$. $\square$

**Corollary (the polar reading).** With $\tilde Q=r\,e^{i\alpha}B\tilde u$ and $B$ of biquaternion norm one,

$$
\tilde Q\tilde Q^{*}=r^{2}B^{2},
$$

which is a positive scalar exactly when $B=e_t$. The class on which the two agree is therefore

$$
\mathcal U=\mathbb R_{>0}\cdot U(2)=\{\tilde Q:\tilde Q\tilde Q^{*}\in\mathbb R_{>0}e_t\},
$$

of real dimension $1+1+3=5$. An inner conjugation can be written as a Hermitian sandwich exactly when its parameter has a trivial polar boost factor.

**Why the two operators differ.** Take a boost rotor $\tilde U=\cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\vec u$ and the identity $e_t$. Then

$$
\mathrm{Ad}_{\tilde U}(e_t)=e_t,
\qquad
\Theta_{\tilde U}(e_t)=\tilde U^{2}=\cosh\psi\,e_t+i\sinh\psi\,\vec u .
$$

The adjoint action fixes the identity; the Hermitian sandwich does not. The difference is not confined to the centre. For every $X$ with $X^{*}=-X$,

$$
(\Theta_{\tilde U}X)^{*}=\tilde U X^{*}\tilde U^{*}=-\Theta_{\tilde U}X,
$$

so the Hermitian sandwich preserves the Hermiticity type of every element, with no condition on $\tilde U$. The adjoint action preserves it only on the unitary slice: for a Hermitian boost,

$$
(\mathrm{Ad}_{\tilde U}X)^{*}=(\tilde U^{-1})^{*}X^{*}\tilde U=-\mathrm{Ad}_{\tilde U^{-1}}X,
$$

which differs from $-\mathrm{Ad}_{\tilde U}X$ whenever $\tilde U^{2}\neq e_t$. This is why the Bloch article cannot use conjugation: the Lorentz action on the material sector must preserve the sector, and only the sandwich does.

**The three structural obstructions.** Beyond the polar criterion there are three obstructions that no choice of parameter can remove.

- **Two parameters.** The chiral action is $g_LXg_R^{*}$ with independent parameters, and the Hermitian sandwich is its diagonal $g_R=g_L$. One parameter has three real dimensions and the pair has six, so no single parameter reproduces the off-diagonal action; the adjoint on the right does not supply the missing parameter. On the unit real quaternions the adjoint is the group inverse, and the formula is the usual chiral action with no operator inverse.
- **Conjugate-linearity.** $aX^{*}b$ is conjugate-linear in $X$; the Hermitian sandwich is linear. They can never be equal as maps. When $b=a^{*}$, however, $aX^{*}a^{*}=\Theta_a(X^{*})$: the sesquilinear sandwich is the Hermitian sandwich composed with the involution.
- **Odd elements and signs.** $\alpha$ is the identity on $\mathbb B$, because every biquaternion is even. The signed forms differ from the unsigned ones only on the odd part of $\mathrm{Cl}_{1,3}$. A minus sign cannot be produced either: $\mathrm{Sc}(QQ^{*})>0$ for every nonzero $Q$, so no Hermitian sandwich equals $-\Theta_Q$.

**Numerical check.** The algebraic criterion was recomputed on at most 100 elements per row.

| test | result |
|---|---|
| $\mathrm{Ad}_Q=\Theta_{Q/\rho}$ for $Q\in U(2)$ | 25/25 |
| for $Q\in SU(2)$ | 25/25 |
| for $Q=\rho U$, $\rho>0$ real, $U\in SU(2)$ | 25/25 |
| for a boost $Q\in SL(2,\mathbb C)$ | 0/25 |
| two-parameter adjoint equals $\Theta$ | 48/100, exactly the diagonal draws |
| sesquilinear $aX^{*}a^{*}$ equals $\Theta$ | 0/100 |
| $\mathrm{Ad}_{\tilde U}$ preserves the sector, boost | 0/100 |
| $\Theta_{\tilde U}$ preserves the sector, boost | 100/100 |

## The Conceptual Criterion

Agreement of values is checked by the proposition. Agreement of meaning is checked by three questions, asked of the sentence in which the formula occurs.

1. **Does the claim use that the map preserves the product?** If the sentence is about an algebra automorphism, a group law, a derivation, an adjoint representation, or the covariance of a commutator, then the inverse is the object and the Hermitian sandwich is a different object. This is the gauge case, and it is the most common one in the corpus.
2. **Does the claim quantify over a group larger than the unitary slice?** If the parameter ranges over all units, or over a general linear group, then even the numerical equality fails on part of the domain, and the replacement is not merely conceptual but false.
3. **Is the map applied to an object as a transport — a state, a field, a vector — with only the norm, the sector and positivity used?** If so, the Hermitian sandwich is the natural operator and the inverse is its special case.

The rule is one line: **replace only when the answers are no, no, yes.** The occurrences that remain are those for which at least one answer is wrong. There are two verdicts.

- **Conceptually different.** The map is an automorphism, the parameter is unitary, and the values agree; the replacement would not change any number but would change what the formula says. It becomes legitimate only if the article, or the theory it belongs to, is rewritten so that the congruence is the primitive object.
- **Structurally impossible.** No parameter gives the map, or the claim quantifies over a domain on which the two differ.

A formula in a definition is not only a value. It fixes the type of the object, and the type is what later proofs may use. A reader who meets $\Theta$ expects a congruence: the norm may scale, the sector is preserved, the product is not. A reader who meets $\mathrm{Ad}$ expects an automorphism: the product, the bracket and the centre are preserved. Writing one where the other is meant is a type error even when the number is right, because it invites the wrong lemma at the next step.

## The Census

The count is a regular-expression scan of the 400 markdown files of `articles_physics`. A formula is counted when it is a product of three factors whose first and third are the same symbol, classified by the exponent on the third. A formula restated in a summary table is counted again. The rows are grouped by the section of this article that treats the occurrences, so that the seven gauge articles appear as one block.

| class | group | form | occurrences | articles | articles involved |
|---|---|---|---:|---:|---|
| inner conjugation | gauge field strength | $Q\,X\,Q^{-1}$ | 9 | 7 | [Non-Abelian (3)](../articles_physics/non-abelian-gauge-fields-in-biquaternionic-form.html)<br>[Yang–Mills (1)](../articles_physics/the-yang-mills-equation-in-biquaternionic-form.html)<br>[Gauge Curvature (1)](../articles_physics/gauge-curvature-and-the-bianchi-identity-in-biquaternionic-form.html)<br>[QCD (1)](../articles_physics/quantum-chromodynamics-under-the-biquaternion-framework-a-research-agenda.html)<br>[Standard Model (1)](../articles_physics/the-standard-model-under-the-biquaternion-framework-a-research-agenda.html)<br>[Wilson (1)](../articles_physics/wilson-loops-in-biquaternionic-form.html)<br>[Confinement (1)](../articles_physics/confinement-and-the-loss-of-partonic-information-in-biquaternionic-form.html) |
| | **inner conjugation, total** | | **9** | **7** | |
| signed Hermitian | odd elements | $\alpha(Q)\,X\,Q^{*}$ | 5 | 1 | [Graded Signed Hermitian (5)](../articles_physics/the-graded-algebra-fermion-parity-and-the-two-sectors-with-signed-hermitian-adjoint-in-biquaternionic-form.html) |
| signed inner conjugation | odd elements | $\alpha(Q)\,X\,Q^{-1}$ | 5 | 2 | [Graded Signed Hermitian (2)](../articles_physics/the-graded-algebra-fermion-parity-and-the-two-sectors-with-signed-hermitian-adjoint-in-biquaternionic-form.html)<br>[Graded Signed Inner (3)](../articles_physics/the-graded-algebra-fermion-parity-and-the-two-sectors-with-signed-inner-conjugation-in-biquaternionic-form.html) |
| **total outside the one-parameter sandwich** | | | **19** | **9** | 10 class assignments |

The reference form stands outside the table: the Hermitian sandwich $Q\,X\,Q^{*}$ is the form against which the other classes are measured.

An article can carry two classes. The article column counts an article once in the row where its occurrences are listed, so the rows sum to 10 article assignments over 9 distinct articles: *The Graded Algebra with Signed Hermitian Adjoint* carries a signed Hermitian and a signed inner conjugation. The sesquilinear form occurs nowhere as a map on the algebra. The natural sandwich has no remaining occurrences: the reflection in *Frames, Rotations and the Lorentz Group* is the Hermitian sandwich $v\,X\,v^{*}$ by a real spatial unit vector, because the conjugate $v^{*}$ equals $v$ there. The three formulas that once looked like occurrences, in *The Relativistic Two-Body Problem* and its exercise, carry the rest-frame label on a four-momentum, now written $\tilde P^{\rm CM}$; each is an ordinary Hermitian sandwich, $\Theta_{\tilde U_{\rm b}}(\tilde P_a^{\rm CM})$, not a conjugate-linear map. The Hermitian row counts the one-symbol spelling $Q\,X\,Q^{*}$, so they are not additional entries there.

Of the 19, nine are conceptually different and ten are structurally impossible. Each is entered below with its sentence, its parameter and its obstruction.

Three shapes are outside the count because the middle factor is not an element of the algebra: $\tilde R\,d\tilde R^{\natural}$ in *Noether's Theorem* and *The Relativistic Particle*, where the middle factor is the exterior derivative; $\lambda\,D\,\lambda^{-1}$ in *Gauge Redundancy and the Information in the Gauge Orbit*, where it is a covariant derivative; and $\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, where the inverse stands on the left. Three further products are not operators on $\mathbb B$: $C\,N\,C^{-1}$ in *The Time-Harmonic Maxwell Operator*, $U\,G\,U^{-1}$ in *Chiral Fermions*, and $T\,H\,T^{-1}$ in *Kramers Degeneracy*.

## The Occurrences That Remain

The nineteen occurrences that remain, in nine articles, fail the conceptual test. Nine of them are **conceptually different**: the parameter is unitary, the two maps agree numerically, and the formula nevertheless states an automorphism. Ten are **structurally impossible**: no parameter gives the map, or the claim ranges over a domain on which the two differ.

The groups below follow the concept, not the syntax. The first is the gauge field strength, the archetype of the conceptual class and the one case where the replacement would require a new theory. The second is the odd element, where the sign is the physics.

### The gauge field strength: the adjoint representation

Six of the seven articles use $F\mapsto UFU^{-1}$ as the adjoint law of a gauge group; the seventh averages the same action over the group. The inverse is not a notation for the sandwich, because the law is derived from the Lie algebra and not posited. The field strength is $F=dA+i\kappa\,A\wedge A$; under $A\mapsto UAU^{-1}+U\,dU^{-1}$ the commutator term transforms as $U[A,A]U^{-1}$ only because $U$ preserves the product. A congruence preserves the Hermitian form, not the bracket, and leaves the derivation without a leg to stand on. The rewrite that would license the replacement is a different theory — a gauge theory whose group acts by congruences of the Hermitian form — and no article in the corpus undertakes it. On $SU(2)$ the numbers are identical; that is precisely why the confusion is possible.

#### 1. [Non-Abelian Gauge Fields in Biquaternionic Form](../articles_physics/non-abelian-gauge-fields-in-biquaternionic-form.html)

**Use.** The field strength transforms in the adjoint representation, $F_{\mathrm g,\mu\nu}=\tilde U F_{\mu\nu}\tilde U^{-1}$ with $\tilde U=\tilde U(\tilde Q)\in SU(2)$; stated at the definition, again in the body, and once in the summary.

**Why not the sandwich.** The article derives the law from the requirement that $D_\mu$ be covariant. The derivation uses $U(ab)U^{-1}=(UaU^{-1})(UbU^{-1})$ at every step.

**Verdict.** Conceptually different, 3/3. Numerically equal on $SU(2)$; interchangeable in substance only after a rewrite in which the gauge group acts by congruences.

#### 2. [The Yang–Mills Equation in Biquaternionic Form](../articles_physics/the-yang-mills-equation-in-biquaternionic-form.html)

**Use.** The componentwise adjoint law $F_{2,\mu\nu}=\tilde U F_{\mu\nu}\tilde U^{-1}$ with $\tilde U\in SU(2)$. The article also proves that the packaged object $\mathcal F_2$ is *not* $\tilde U\mathcal F\tilde U^{-1}$, because the inverse does not pass through the basis product $\bar e_\mu e_\nu$.

**Why not the sandwich.** The negative result is itself a statement about the adjoint action: it compares two orderings of the same automorphism. Replacing the written law by a congruence would leave the comparison without its terms.

**Verdict.** Conceptually different, 1/1.

#### 3. [Gauge Curvature and the Bianchi Identity in Biquaternionic Form](../articles_physics/gauge-curvature-and-the-bianchi-identity-in-biquaternionic-form.html)

**Use.** The transformation law of $F_{\mu\nu}$ under a local $\tilde U(\tilde Q)\in SU(2)$, used to prove the covariance of the Bianchi identity and to show that only gauge-invariant polynomials are observables.

**Why not the sandwich.** Covariance of $D_\lambda F_{\mu\nu}$ is covariance of a commutator, and the Bianchi identity is the Jacobi identity of that commutator. Both are properties of the automorphism, not of the congruence.

**Verdict.** Conceptually different, 1/1.

#### 4. [Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda](../articles_physics/quantum-chromodynamics-under-the-biquaternion-framework-a-research-agenda.html)

**Use.** The adjoint law $F_{2,\mu\nu}=\tilde U F_{\mu\nu}\tilde U^{-1}$, with the matrix trace on the $\mathrm{SU}(2)$ factor. The article's point is that the available factor is $SU(2)$ and not colour.

**Why not the sandwich.** The article is an inventory of what a gauge theory requires. One item of that inventory is an adjoint action; writing a congruence would remove the item from the list.

**Verdict.** Conceptually different, 1/1.

#### 5. [The Standard Model under the Biquaternion Framework — A Research Agenda](../articles_physics/the-standard-model-under-the-biquaternion-framework-a-research-agenda.html)

**Use.** The same adjoint law, in the same construction, with the trace on the $\mathrm{SU}(2)$ factor; the surrounding paragraph is about the reality class of the connection.

**Why not the sandwich.** The paragraph asks whether the connection can be placed in a fixed Hermitian eigenspace. That question is about the action of the gauge group on the reality type, which is the action of an automorphism mixing the two sectors.

**Verdict.** Conceptually different, 1/1.

#### 6. [Wilson Loops in Biquaternionic Form](../articles_physics/wilson-loops-in-biquaternionic-form.html)

**Use.** In the non-abelian theory the field strength transforms by conjugation, $\tilde F\mapsto Q\tilde F Q^{-1}$; the gauge group is realised inside $\mathbb M_+$ as unit quaternions.

**Why not the sandwich.** The loop is the trace of a holonomy, and its gauge invariance is the invariance of the trace under the adjoint action. The proof uses the cyclicity of the trace, which is a property of the automorphism.

**Verdict.** Conceptually different, 1/1.

#### 7. [Confinement and the Loss of Partonic Information in Biquaternionic Form](../articles_physics/confinement-and-the-loss-of-partonic-information-in-biquaternionic-form.html)

**Use.** The colour-singlet conditional expectation $E(\tilde Q)=\int_G dU\,U\tilde Q U^{-1}$ with the normalised Haar measure; it is the idempotent projection onto the colour-neutral subalgebra.

**Why not the sandwich.** The integral is an average of automorphisms, and its fixed-point algebra is the commutant of the group. On $SU(2)$ each integrand equals a sandwich, but replacing the integrand would turn a group average into an average of congruences, and the fixed-point set would no longer be the commutant.

**Verdict.** Conceptually different, 1/1.

### Odd elements and the parity twist

The signed forms are different operators only outside the biquaternion algebra. Every element of $\mathbb B$ is even, so $\alpha$ is the identity there and $\Theta^{\alpha}=\Theta$; the sign is visible only on the odd part of $\mathrm{Cl}_{1,3}$.

#### 8. [The Graded Algebra, Fermion Parity and the Two Sectors with Signed Hermitian Adjoint in Biquaternionic Form](../articles_physics/the-graded-algebra-fermion-parity-and-the-two-sectors-with-signed-hermitian-adjoint-in-biquaternionic-form.html)

**Use.** Seven occurrences: five of $\Theta^{\alpha}_x(y)=\alpha(x)yx^{*}$ and two of $\alpha(x)yx^{-1}$, on $\mathrm{Cl}_{1,3}=\mathrm{Cl}^{0}\oplus\mathrm{Cl}^{1}$.

**Why not the sandwich.** The odd sector is the subject, and the sign is the physics. The article states the boundary itself: on $\mathbb B$ the signed and unsigned forms coincide, and every computation inside $\mathbb B$ is a computation with the Hermitian sandwich.

**Verdict.** Structurally impossible, 0/7.

#### 9. [The Graded Algebra, Fermion Parity and the Two Sectors with Signed Inner Conjugation in Biquaternionic Form](../articles_physics/the-graded-algebra-fermion-parity-and-the-two-sectors-with-signed-inner-conjugation-in-biquaternionic-form.html)

**Use.** Three occurrences of $\mathrm{Ad}^{\alpha}_x(y)=\alpha(x)yx^{-1}=(\Omega x\Omega^{-1})yx^{-1}$, the parity-carrying conjugation by the volume element.

**Why not the sandwich.** The twist is a conjugation by the pseudoscalar on the left and an inverse on the right; neither factor is available from a Hermitian sandwich.

**Verdict.** Structurally impossible, 0/3.

## The Gauge Case in Detail

The seven gauge articles deserve a separate statement, because they are the case where the replacement is most tempting and most consequential.

The adjoint law is forced by three requirements, and each of them is a property of an automorphism.

- **Covariance.** $D_\mu=\partial_\mu+i\kappa A_\mu$ must transform as $D_\mu\mapsto U D_\mu U^{-1}$ if the equation $D_\mu\psi=0$ is to be frame-independent. This uses $U(\xi\eta)U^{-1}=(U\xi U^{-1})(U\eta U^{-1})$ on products of fields.
- **The commutator.** $F_{\mu\nu}=[D_\mu,D_\nu]/(i\kappa)$ transforms as $UF_{\mu\nu}U^{-1}$ precisely because $U$ preserves the bracket. A congruence does not: $\Theta_U([F,G])=[\Theta_U F,\Theta_U G]$ holds only when $U$ is unitary, which is the case at hand, but it is a theorem about the unitary slice and not about the map. The derivation would have to be re-run with the restricted parameter at every step.
- **The invariants.** $\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$ is invariant under the adjoint action for every unit. Under the congruence with a general unit $Q=\lambda V$ it scales by $\lvert\lambda\rvert^{4}$, so the Lagrangian would have to be rescaled or the parameter restricted.

None of this changes a number on $SU(2)$. It changes what the formula is a formula *for*. The replacement becomes available in one of two ways, and both are rewrites rather than edits.

1. **A congruence gauge theory.** Take the congruence as the primitive action, let the gauge parameter be any unit, and define the field strength, the covariant derivative, the action and the trace so that they transform by congruence. This is a different theory: its gauge group is larger, its field strength scales, and its invariants are different. No article in the corpus does this.
2. **An explicit restriction.** Keep the adjoint law but state it only for the unitary slice, where the two forms agree, and add the remark that the congruence is the continuation off the slice. This is a clarification, not a replacement, and it is the honest form of the statement "the two coincide on $SU(2)$".

Until one of these is done, the gauge occurrences stay in the adjoint form.

## Summary

**19 occurrences in 9 articles: 9 conceptually different, 10 structurally impossible.**

| # | article | occurrences | conceptual | structural |
|---|---|---:|---:|---:|
| 1 | [Non-Abelian Gauge Fields in Biquaternionic Form](../articles_physics/non-abelian-gauge-fields-in-biquaternionic-form.html) | 3 | 3 | 0 |
| 2 | [The Yang–Mills Equation in Biquaternionic Form](../articles_physics/the-yang-mills-equation-in-biquaternionic-form.html) | 1 | 1 | 0 |
| 3 | [Gauge Curvature and the Bianchi Identity in Biquaternionic Form](../articles_physics/gauge-curvature-and-the-bianchi-identity-in-biquaternionic-form.html) | 1 | 1 | 0 |
| 4 | [Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda](../articles_physics/quantum-chromodynamics-under-the-biquaternion-framework-a-research-agenda.html) | 1 | 1 | 0 |
| 5 | [The Standard Model under the Biquaternion Framework — A Research Agenda](../articles_physics/the-standard-model-under-the-biquaternion-framework-a-research-agenda.html) | 1 | 1 | 0 |
| 6 | [Wilson Loops in Biquaternionic Form](../articles_physics/wilson-loops-in-biquaternionic-form.html) | 1 | 1 | 0 |
| 7 | [Confinement and the Loss of Partonic Information in Biquaternionic Form](../articles_physics/confinement-and-the-loss-of-partonic-information-in-biquaternionic-form.html) | 1 | 1 | 0 |
| 8 | [The Graded Algebra, Fermion Parity and the Two Sectors with Signed Hermitian Adjoint in Biquaternionic Form](../articles_physics/the-graded-algebra-fermion-parity-and-the-two-sectors-with-signed-hermitian-adjoint-in-biquaternionic-form.html) | 7 | 0 | 7 |
| 9 | [The Graded Algebra, Fermion Parity and the Two Sectors with Signed Inner Conjugation in Biquaternionic Form](../articles_physics/the-graded-algebra-fermion-parity-and-the-two-sectors-with-signed-inner-conjugation-in-biquaternionic-form.html) | 3 | 0 | 3 |
| | **total** | **19** | **9** | **10** |

## Further Reading

- [The Hermitian Sandwich on a Hermitian Algebra with Hermitian Adjoint](../articles_maths/the-hermitian-sandwich-on-a-hermitian-algebra-with-hermitian-adjoint.html), for the general operator, its domain, its multiplicativity and the correction of the Clifford-group identity.
- [The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint](../articles_maths/the-hermitian-sandwich-in-the-biquaternion-algebra-with-hermitian-adjoint.html), for the biquaternion instance and its identification with the dagger sandwich of the corpus.
- [The Hermitian Sandwich on a Krein Space](../articles_maths/the-hermitian-sandwich-on-a-krein-space.html), for the indefinite adjoint and the loss of the spectral transport.
- [The Sesquilinear Sandwich Operator](../articles_maths/the-sesquilinear-sandwich-operator.html), for the conjugate-linear family and the composition law of its parameters.
- [The Inner Conjugation on the Two-Sided Operators](../articles_maths/the-inner-conjugation-on-the-two-sided-operators.html), for the two-parameter family and the statement that the inner conjugation is the only member of it that is an algebra automorphism.
- [Two-Sided Operators on a Hermitian Algebra with Signed Hermitian Adjoint](../articles_maths/two-sided-operators-on-a-hermitian-algebra-with-signed-hermitian-adjoint.html), for the signed family and its parity.
- [The Polar Decomposition of a Biquaternion](../articles_maths/the-polar-decomposition-of-a-biquaternion.html), for the four factors and the boost-free criterion in the algebra's own terms.
