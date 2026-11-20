# __Two Readings of One Transformation: A Comparison__

## Introduction

One group, two slices, two actions. The element that carries one frame to another is a single unit-norm biquaternion, and it acts on the material slice and on the informational slice by the same formula, $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{*}$. The article sets the two readings side by side, states which comparisons are exact identities of the algebra, and states where the comparison stops.

**The comparison has a spine, and it is a statement about isometry groups.**

- The transformations that preserve the **interval** — the quaternionic norm of the material slice — are the **rotors**, the unit-norm biquaternions. That is a six-dimensional group, and every element of it is an isometry of the material reading.
- The transformations that preserve the **trace** — the doubled scalar part of the informational slice — are the **$*$-unitary** elements, $\tilde U\tilde U^{*}=e_t$. That is a four-dimensional group, $U(2)$, and every element of it is a channel.
- The two groups **intersect in the rotations**, the real unit quaternions, of dimension three. There, and only there, one element is an isometry of both readings.

**Everything else follows from those three lines.** A boost is in the first group and not the second, so it is a symmetry of the interval and not a channel. A phase $e^{i\theta}$ is in the second and not the first, so it is a channel and not a symmetry of the interval. Neither is an isometry of both, and no element of either group is a symmetry of both readings except the rotation.

**What the article refuses.** It refuses a duality: the two readings are two actions of one group on two subspaces of one algebra, not two theories that a map identifies. It refuses a translation of states into four-vectors: the map that carries the congruence carries neither the product nor the interpretation. And it refuses to call the comparison a result of physics: it is a comparison of two mathematical readings whose physical vocabularies are fixed elsewhere.

The article uses [The Two Sectors: the Hermitian Split and the Four Bridges](the-two-sectors-the-hermitian-split-and-the-four-bridges.html) for the split, [The Sector Map and Its Exact Parts](the-sector-map-and-its-exact-parts.html) for the map between them, [The Four Forms and the Four Norms](the-four-forms-and-the-four-norms.html) for the measures, and the group articles of the previous section for the two isometry groups.

## The Same Element, Two Actions

**One element.** The Lorentz transformation is one unit-norm biquaternion, and its two readings are two congruences:

$$
\text{material:}\quad \tilde P_\Phi\longmapsto\tilde U\tilde P_\Phi\tilde U^{*},
\qquad
\text{informational:}\quad \tilde{Ϛ}_\Psi\longmapsto\tilde U\tilde{Ϛ}_\Psi\tilde U^{*}.
$$

The formula is the same; the elements acted on are not. A four-momentum is anti-Hermitian of norm $-m^{2}c^{2}$; a state is Hermitian of trace one. Nothing in the congruence knows the difference, and that is the point: the group acts on the whole algebra and the two slices are two invariant subspaces.

**Both slices are invariant because the star commutes with the congruence.** For $\tilde Q$ Hermitian, $(\tilde U\tilde Q\tilde U^{*})^{*}=\tilde U\tilde Q\tilde U^{*}$; for $\tilde Q$ anti-Hermitian, the same computation with the two signs gives an anti-Hermitian element. So the action never mixes the slices, and a reader may compute on either one and know where the answer lives.

**The invariants are not the same invariant.** The material action preserves $\langle\tilde Q\rangle_\natural=\tilde Q\tilde Q^{\natural}$; the informational action preserves $\mathrm{Sc}\,\tilde Q$ and the doubled scalar part. For a general element neither is preserved, and the two failures are the subject of the next section.

## The Catalogue

| | material reading | informational reading |
| --- | --- | --- |
| the object acted on | a four-vector $\tilde P_\Phi$, anti-Hermitian | a state $\tilde{Ϛ}_\Psi$, Hermitian of trace one |
| the space | Minkowski space, inertia $(3,1)$ | the Bloch ball, radius below one |
| the invariant | $\langle\tilde Q\rangle_\natural$, the interval | $2\,\mathrm{Sc}$, the trace, and the radius |
| the isometry group | the rotors, unit-norm, dimension six | the $*$-unitary elements, dimension four |
| the intersection | the rotations, real unit quaternions, dimension three | the same |
| a boost | an isometry | not a channel; moves the slice |
| a phase $e^{i\theta}$ | not an isometry | a channel; fixes every state |
| the compact part | $SU(2)$, a double cover of $SO(3)$ | $SU(2)$, acting by the same matrices |
| what a measurement reads | an interval, an energy, a momentum | a weight, a probability, a distance |
| the physical name of the group | the Lorentz group | the same group, acting on states |

**The table is the article in one object.** Every row is one of the three isometry statements above, or a consequence of one.

**Two rows deserve the derivation.** The first is that a boost preserves the interval: it is an element of $SU(2)$, so $\tilde U\tilde P_\Phi\tilde U^{*}$ has the same natural norm, and the mass shell is preserved identically — not by a cancellation but because the norm is multiplicative and the rotor has norm one. The second is that a phase fixes every state: $\tilde U=e^{i\theta}e_t$ is central, so $\tilde U\tilde{Ϛ}_\Psi\tilde U^{*}=e^{i\theta}e^{-i\theta}\tilde{Ϛ}_\Psi=\tilde{Ϛ}_\Psi$. A transformation that fixes every state is a channel and carries no information, which is the exact sense in which the centre of $U(2)$ acts trivially on the ball.

## The Exact Correspondences

**The congruence is carried by the sector map.** With $J(\tilde Q)=i\tilde Q$ from the companion, $J(\tilde U\tilde Q\tilde U^{*})=\tilde U(i\tilde Q)\tilde U^{*}$, because $i$ is central and fixed by the star. So any statement about the orbits of the group on one slice is a statement about the orbits on the other, and the two orbit spaces are the same set. This is the strongest exact statement available, and it is a statement about actions, not about algebras.

**The Hermitian form is carried, the natural norm is negated.** $H(J\tilde Q)=H(\tilde Q)$ and $\langle J\tilde Q\rangle_\natural=-\langle\tilde Q\rangle_\natural$. So an amplitude computed on one side is a weight on the other, and an interval computed on one side becomes the negative of itself. The second identity is the reason the material interval is indefinite and the informational weight definite: they are one number and its negative, read at two points of one map.

**The compact part acts identically.** For a real unit quaternion $\tilde u$, $\tilde u^{*}=\tilde u^{\natural}=\tilde u^{-1}$, so the congruence by $\tilde u$ is simultaneously an isometry of both forms. This is why the rotation subgroup is the bridge, why the gyration of a boost pair is the one piece of a frame change that both readings can see, and why $SU(2)$ appears on both rows of the table with the same matrices.

**The two group elements that are not in the intersection are the two asymmetries.** A boost is in $SU(2)$ and not in $U(2)$: it preserves the interval and moves the trace. A phase is in $U(2)$ and not in $SU(2)$: it preserves the trace and changes the natural norm by $e^{2i\theta}$. Each reading is blind to what the other one sees, and the blindness is a group-theoretic fact and not a limitation of a calculation.

## Where the Readings Diverge

**They diverge on composition, and the divergence is a sign.** The sector map reverses the product, $J(\tilde Q\tilde Q')=-J(\tilde Q)J(\tilde Q')$, so a composite computed on one side and carried to the other arrives with a sign per factor. A reader who composes two maps across the comparison will get the wrong answer unless the sign is inserted, and the corpus's rule is therefore to compare invariants and never to compose across the map.

**They diverge on what a measurement is.** The material reading measures an interval; the informational reading measures a weight. The two are different functionals of the same element, and no experiment measures both on one object: an interval is read from a clock and a ruler, a weight from a counting statistic.

**They diverge on the exceptional locus.** The material degeneration — the Jordan part — needs a complex momentum and is unreachable on the real slice. The informational one is the centre of the ball, real, semi-simple and present in every frame. One sector's degenerate point is a calculation and the other's is a place.

**They agree on the angle.** The one quantity that both readings compute from the same element and report as the same number is the compact factor: the rotation that a product of two boosts contains. The material reading sees it as the holonomy of the velocity ball, the informational one as a unitary channel on the Bloch ball, and the matrix is the same matrix. This is the sharpest positive statement of the comparison, and it is a consequence of the intersection being non-trivial.

## What the Comparison Does Not Claim

**It does not claim a duality of theories.** A duality would be a map that carries every statement of one theory to a statement of another, including composition. The sector map fails on composition, so no duality follows from it.

**It does not claim that a state is a four-vector.** The map carries elements; it does not carry interpretations. The image of a four-momentum is an element, not a state, and the corpus never writes it as one.

**It does not claim that the two readings are two physical effects.** A single experiment is read in one vocabulary. The comparison is a statement about the algebra, and its physical content is exactly the three-group structure of the first section.

## Summary

One unit-norm biquaternion acts on two slices by one congruence. The material reading is the action on four-vectors preserving the natural norm; the informational reading is the action on states preserving the trace. The two isometry groups are the rotors, of dimension six, and the $*$-unitary elements, of dimension four, and they intersect exactly in the rotations, of dimension three. The sector map carries the action and the Hermitian form, negates the natural norm, and reverses the product. Boosts are isometries of one reading and not the other; phases are the reverse; rotations are both. Every agreement and every divergence in the table follows from that.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\langle\tilde Q\rangle_\natural=\tilde Q\tilde Q^{\natural}$ | the natural norm, the interval on the material slice |
| $H(\tilde Q)=\mathrm{Sc}(\tilde Q\tilde Q^{*})$ | the Hermitian form |
| $2\,\mathrm{Sc}$ | the trace of the $2\times2$ image |
| $\mathrm{Cg}_{\tilde U}$ | the congruence $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{*}$ |
| $SU(2)$ | unit-norm biquaternions, $\cong SL(2,\mathbb{C})$, dimension six |
| $U(\mathbb{B})$ | the $*$-unitary group, $\cong U(2)$, dimension four |
| $J(\tilde Q)=i\tilde Q$ | the sector map |

## Further Reading

**In this category.** [The Two Sectors: the Hermitian Split and the Four Bridges](the-two-sectors-the-hermitian-split-and-the-four-bridges.html) fixes the split. [The Sector Map and Its Exact Parts](the-sector-map-and-its-exact-parts.html) proves the four identities used above. [The Four Forms and the Four Norms](the-four-forms-and-the-four-norms.html) supplies the measures. [The H Norm: Amplitude and Frame](the-h-norm-amplitude-and-frame.html) identifies $U(\mathbb{B})$ as the group of H-isometries. [The Group of Unit-Norm Biquaternions](the-group-of-unit-norm-biquaternions.html) is the material isometry group. [The Lorentz Group on the Bloch Ball: Projective Action and Two Metrics](the-lorentz-group-on-the-bloch-ball.html) is the informational one. [The Informational Reading of the Wigner Angle](the-informational-reading-of-the-wigner-angle.html) and [Velocity Space as Hyperbolic Geometry in Biquaternionic Form](velocity-space-as-hyperbolic-geometry-in-biquaternionic-form.html) are the two readings of the one angle.
