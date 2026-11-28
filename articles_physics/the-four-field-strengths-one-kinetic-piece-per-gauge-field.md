# __The Four Field Strengths: One Kinetic Piece per Gauge Field__

## Introduction

**The claim.** The first four pieces of the list are the squared curvatures of the four gauge fields, $-\tfrac14G^a_{\mu\nu}G^{a\mu\nu}$, $-\tfrac14F_{\mu\nu}F^{\mu\nu}$, $-\tfrac14Z_{\mu\nu}Z^{\mu\nu}$ and $-\tfrac12W^+_{\mu\nu}W^{-\mu\nu}$. One piece per field, no cross terms, and three of the four are not linear in the fields.

**The answer.**

$$
\boxed{\;\mathcal{L}_{\mathrm{con}}=-\tfrac14G^a_{\mu\nu}G^{a\mu\nu}-\tfrac14F_{\mu\nu}F^{\mu\nu}-\tfrac14Z_{\mu\nu}Z^{\mu\nu}-\tfrac12W^+_{\mu\nu}W^{-\mu\nu}\;}
$$

**Why four and not two.** A reader who expects a Yang–Mills term for the gluons and a Maxwell term for the photon will count two. There are four, because the electroweak sector has two neutral fields and one charged pair after the rotation, and each is a separate gauge field with its own curvature.

**The standing.** All four pieces are standard. The corpus's own derivation of the connection action is [The Lagrangian and the Electroweak Theory](the-lagrangian-and-the-electroweak-theory.html) and [The Lagrangian and Quantum Chromodynamics](the-lagrangian-and-quantum-chromodynamics-the-triplet-the-octet-and-the-feynman-rules.html); this article writes the four mass-basis pieces and states the one structural difference between them.

## Conventions

**The metric and the indices.** The displays of this category use $g_{\mu\nu}=(1,-1,-1,-1)$ and $\partial_\mu=\partial/\partial x^\mu$. The corpus writes the same pieces with $\imath$ indices and the rule $\sum_{\imath}X_{\imath}Y_{\imath}=-X\cdot Y$; the dictionary is that one line, and it is stated in [The Complete Lagrangian](the-census-in-one-display-forty-seven-terms-fifty-three-vertices-twenty-blocks-and-nineteen-parameters.html).

**The covariant derivative on the charged field.** On $W^+_\mu$,

$$
D_\mu W^+_\nu=\bigl(\partial_\mu+ieA_\mu+ig\cos\theta_W\,Z_\mu\bigr)W^+_\nu ,
$$

and on $W^-_\mu$ the same with the signs reversed. The two coefficients follow from the charge of the field and its isospin: the photon couples to $Q=+1$ with $e$, and the $Z$ couples to $T_3=+1$ with $g\cos\theta_W$.

**The sign of the kinetic terms.** Each is negative, so that the Hamiltonian is positive. This is the same choice the corpus makes for its curvature term, and the sign is unchanged by the dictionary because the weight over two indices cancels the flip.

## The Four Curvatures

**Three are written with a commutator and one is not.**

$$
G^a_{\mu\nu}=\partial_\mu G^a_\nu-\partial_\nu G^a_\mu+g_s f^{abc}G^b_\mu G^c_\nu ,
$$

$$
W^a_{\mu\nu}=\partial_\mu W^a_\nu-\partial_\nu W^a_\mu+g\varepsilon^{abc}W^b_\mu W^c_\nu ,
\qquad
B_{\mu\nu}=\partial_\mu B_\nu-\partial_\nu B_\mu .
$$

**The rotation and the two neutral curvatures.** With $W^3_\mu=\cos\theta_WZ_\mu+\sin\theta_WA_\mu$ and $B_\mu=-\sin\theta_WZ_\mu+\cos\theta_WA_\mu$,

$$
F_{\mu\nu}=\sin\theta_W\,W^3_{\mu\nu}+\cos\theta_W\,B_{\mu\nu},
\qquad
Z_{\mu\nu}=\cos\theta_W\,W^3_{\mu\nu}-\sin\theta_W\,B_{\mu\nu},
$$

and since the rotation is constant, no derivative acts on it. Both neutral curvatures are linear in the fields.

**The charged curvature.** With $W^\pm_\mu=(W^1_\mu\mp iW^2_\mu)/\sqrt2$ and the $W^3$ curvature of the display above,

$$
W^+_{\mu\nu}=\partial_\mu W^+_\nu-\partial_\nu W^+_\mu+i g\bigl(W^3_\mu W^+_\nu-W^3_\nu W^+_\mu\bigr),
\qquad
W^3_{\mu\nu}=\partial_\mu W^3_\nu-\partial_\nu W^3_\mu+i g\bigl(W^-_\mu W^+_\nu-W^+_\mu W^-_\nu\bigr).
$$

**The second of these two lines is the one that is usually left out.** It carries the $W^+W^-$ bilinear in the neutral curvature, and that bilinear is where the four-vector vertex lives. A treatment that writes only $|D_\mu W^+_\nu-D_\nu W^+_\mu|^2$ with an $A$–$Z$ background will miss the $W^+W^-W^+W^-$ structure entirely, because the structure comes from the neutral curvature and not from the charged one. [The Gauge Self-Interactions](the-gauge-self-interactions-two-triple-vertices-and-four-quartic-vertices.html) enumerates all six.

**Why the $Z$ curvature has no commutator of its own and still produces self-interactions.** The neutral field's non-abelian self-coupling is carried by the covariant derivative of the charged field and by the commutator in $W^3_{\mu\nu}$. A commutator written directly in $Z_{\mu\nu}$ would require $Z$ to rotate into something, and in the mass basis the residual group is $U(1)_{\mathrm{em}}$, under which $Z$ is neutral and inert. The self-interactions are still there; they have moved into the charged sector.

## The Four Pieces

**Normalisation.** The charged piece carries $\tfrac12$ and the neutral ones $\tfrac14$, because $W^+_{\mu\nu}W^{-\mu\nu}$ counts the two real components of the complex field twice.

| Piece | Field | Linearity | Self-interactions |
|---|---|---|---|
| $-\tfrac14G^aG^a$ | gluon | non-abelian | three-gluon, four-gluon |
| $-\tfrac14FF$ | photon | abelian | none |
| $-\tfrac14ZZ$ | $Z$ | linear in the mass basis | none, in this piece |
| $-\tfrac12W^+W^-$ | $W^\pm$ | non-abelian | the six structures, with the neutral curvature |

**The splitting of the neutral kinetic terms.** Before the rotation the two neutral pieces are $-\tfrac14W^3_{\mu\nu}W^{3\mu\nu}-\tfrac14B_{\mu\nu}B^{\mu\nu}$ and no mixed term exists. After it the same two pieces are $-\tfrac14F_{\mu\nu}F^{\mu\nu}-\tfrac14Z_{\mu\nu}Z^{\mu\nu}$, because the rotation is orthogonal. The absence of a $Z_{\mu\nu}F^{\mu\nu}$ piece is the orthogonality of the rotation, not a separate dynamical statement.

**No cross term between different fields.** A term $G^a_{\mu\nu}W^{a\mu\nu}$ is forbidden by colour, and $W^+_{\mu\nu}F^{\mu\nu}$ by charge. The four pieces are separate because the residual group is a product and each curvature transforms in a different representation.

## Checks

1. The count. Four pieces, twelve fields, and one piece per field type.
2. The linearity. $F_{\mu\nu}$ and $Z_{\mu\nu}$ are linear in the fields; $G^a_{\mu\nu}$ and $W^a_{\mu\nu}$ are not.
3. The rotation's orthogonality. $\sin^2\theta_W+\cos^2\theta_W=1$, so the neutral quadratic form is preserved and no mixed piece appears.
4. The charged curvature's charge. $W^+_{\mu\nu}$ carries $Q=+1$: the covariant derivative's photon term is $+ieA_\mu$, and the $W^3$ term is neutral, so the charge is the field's.
5. The coupling ratio. The $Z$ coefficient of the charged field is $g\cos\theta_W$ and its photon coefficient is $e=g\sin\theta_W$, so the ratio is $\cot\theta_W$.
6. The $W$-only quartic. Setting $A=Z=0$ in the two curvature displays leaves the $W^3$ commutator, which squares to the four-$W$ structure; setting $W^\pm=0$ leaves nothing, which is why there is no three-$W$ vertex.
7. The degree-of-freedom count. Twelve massless fields times two polarisations is twenty-four, before the masses are added.
8. The sign. Each piece is negative, and each gives a positive energy density after the Legendre transform.

## Summary

The four kinetic pieces are the squared curvatures of the four gauge fields, with coefficients $-\tfrac14$ for the three real fields and $-\tfrac12$ for the complex pair. The gluon and the charged field have non-abelian curvatures; the photon and the $Z$ have linear ones, because the rotation to the mass basis is constant and the residual group is abelian.

The charged curvature carries the $A$ and $Z$ couplings through a covariant derivative, and the neutral curvature carries a $W^+W^-$ bilinear. The second fact is the one a shortened treatment drops, and dropping it loses the four-$W$ vertex.

No cross term exists between the four pieces, for reasons of colour and charge. The absence of a $Z_{\mu\nu}F^{\mu\nu}$ piece is the orthogonality of the rotation and not a separate assumption.

The four pieces are the first four rows of the forty-seven and the beginning of the lineage: they descend from two ancestors, the strong kinetic term and the two electroweak kinetic terms.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G^a_{\mu\nu}$ | Gluon curvature, adjoint of $SU(3)_c$ |
| $F_{\mu\nu}$ | Photon curvature of $U(1)_{\mathrm{em}}$ |
| $Z_{\mu\nu}$ | $Z$ curvature, linear in the mass basis |
| $W^\pm_{\mu\nu}$ | Charged curvature, with the $A$ and $Z$ couplings |
| $W^3_{\mu\nu}$ | Neutral $SU(2)$ curvature, carrying the $W^+W^-$ bilinear |
| $f^{abc}$, $\varepsilon^{abc}$ | Structure constants of the two non-abelian factors |
| $\theta_W$ | The rotation angle between $(W^3,B)$ and $(Z,A)$ |

## Further Reading

- [The Lagrangian and the Electroweak Theory](the-lagrangian-and-the-electroweak-theory.html). The connection action before the rotation.
- [The Lagrangian and Quantum Chromodynamics: The Triplet, the Octet and the Feynman Rules](the-lagrangian-and-quantum-chromodynamics-the-triplet-the-octet-and-the-feynman-rules.html). The strong curvature and its two self-interactions.
- [The Minimal Coupling in Biquaternionic Form](the-minimal-coupling-in-biquaternionic-form.html). The curvature as the vector part of a product.
- [The Weinberg Angle and the Three Neutral States](the-weinberg-angle-and-the-three-neutral-states.html). The rotation used above.
- [The Gauge Self-Interactions](the-gauge-self-interactions-two-triple-vertices-and-four-quartic-vertices.html). The six structures contained in these four pieces.
