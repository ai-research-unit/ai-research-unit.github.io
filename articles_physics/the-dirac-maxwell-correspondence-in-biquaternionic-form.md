# __The Dirac–Maxwell Correspondence in Biquaternionic Form__

## Introduction

**The observation.** In the biquaternion algebra the massless Dirac equation of the member written $R$ and the source-free Maxwell equation are one equation,

$$
\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=0,
\qquad
\tilde\nabla\tilde F=0,
$$

written for two different objects. The operator is the same element, it multiplies on the same side, and the difference between the two equations is not in the equation. This article states what the coincidence carries and where it stops.

**The five statements, ordered by how much they claim.** The **identity of form** claims only what the multiplication table gives: two objects, one operator, one side. The **mass term** names the one term of the Dirac equation that has no Maxwell counterpart and the two variables in which it is written, a central left coefficient and a two-sided conjugation with a right direction. The **static medium** is a dictionary of coefficients, restricted to a class of potentials, and it matches equations and not fields. The **mass shell** is a condition under which one projection identity holds in both directions, and the condition turns out to be the relativistic dispersion relation. The **Lanczos reading** is an interpretation of the two equations as one system with feedback, and it is carried here as the source's.

**What is not claimed anywhere below.** The Dirac field and the electromagnetic field are not identified. They are different objects of one algebra — a general element carrying a value against a vector of the algebra — and no line of this article equates them. What the equations share is the operator and, in the dictionary, the coefficients. A reader who wants the fields themselves to be one object will not find that statement here, and the corpus does not make it.

**What is used, and where it is stated.** The algebra and its units are those of *Algebra and Element Conventions*, the operator $\tilde\nabla$ and its conjugate $\tilde\nabla^{\natural}$ those of *Operator and Calculus Conventions*, and the Maxwell equation in biquaternion form is stated in *Maxwell's Equations in the Biquaternionic Formulation*. The Dirac side is *The Dirac Equation in Biquaternionic Form*: the chiral pair, its two components, the value of an element read by one multiplication, and the derivation of the Klein–Gordon equation for each half. The solutions are in *Explicit Solutions of the Biquaternionic Dirac Equation*. This article uses those results and repeats none of them.

**The order.** The identity of form comes first, because every later statement is a comment on it. The mass term follows, and then the two comparisons that produce conditions rather than identities: the static medium and the time-harmonic field. The Lanczos reading closes the sequence, and the open questions state what it leaves open.

## The Structural Identity

The massless biquaternionic Dirac equation in the member written $R$ and the homogeneous biquaternion Maxwell equation have the same form:

$$
\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = 0 .
$$

The member written $L$ has the conjugate form, $\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = 0$, which is the same equation for the conjugate field. The difference is the object:

- In the Maxwell case, the field is the field-strength biquaternion $\tilde{F}$, which lives in the vector part of the algebra and describes the electromagnetic field.
- In the Dirac case, the field is the fermion field $\tilde{Ξ}_{\mathrm{sp},R}$, and it is a general element carrying the plus letter of the pair and describes the spin-$\frac{1}{2}$ particle.

The structural identity is the algebraic content of the statement that both fields are read in the same algebra. The two fields differ in **what they are**: the photon field is a vector of the algebra (spin-1), and the electron field is a general element with a value (spin-$\frac{1}{2}$).

## The Mass Term

The **mass term** is the term that distinguishes the massive Dirac equation from the massless case, and it does not appear in the Maxwell equation. In the biquaternion formulation it is the linear pairing of the pair $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = k_m\,\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\,\tilde{Ξ}_{\mathrm{sp},R}$ of §*The Massive Case* of *The Dirac Equation in Biquaternionic Form*: its coefficient $k_m$ is central and multiplies on the left, so it relates the two components and moves no value across. What is neither central nor a left multiplication is the two-sided mass term, $-i\,\overline{F}\,\vec e_z\,k_m$: it conjugates the coefficients and multiplies on the right, and those are what carry a letter across. The two forms are one mass term written in two variables, and the change of variable between them is the dictionary. In the Standard Model the mass term arises from the **Higgs mechanism**: the fermion couples to the Higgs field, and the coupling generates an effective mass term.

The biquaternion framework does not derive the Higgs mechanism; it simply provides a compact notation for the mass term once the mechanism is assumed. The conjugation $\flat$ is a separate object — the algebra's real structure, discussed in §*The Massive Case* of *The Dirac Equation in Biquaternionic Form* — and is not the mass term.

## The Static Maxwell Field of an Inhomogeneous Medium as a Dirac Potential

The dictionary gives one more interpretation of the massive equation, in which its potential *is* a Maxwell medium. The static sourceless Maxwell system of an isotropic inhomogeneous medium,

$$
\mathrm{rot}\,\vec H = 0, \qquad \mathrm{rot}\,\vec E = 0, \qquad \mathrm{div}(\epsilon\vec E) = 0, \qquad \mathrm{div}(\mu\vec H) = 0 ,
$$

carries its position dependence only through the two divergence equations, and on the normalised fields $\vec E_{\mathrm n} := \sqrt{\epsilon}\,\vec E$, $\vec H_{\mathrm n} := \sqrt{\mu}\,\vec H$ it becomes the pair of first-order equations with constant-free leading part,

$$
D\vec E_{\mathrm n} + \vec E_{\mathrm n}\vec{\nu} = 0, \qquad D\vec H_{\mathrm n} + \vec H_{\mathrm n}\vec{\nu}_2 = 0,
\qquad
\vec{\nu} := \frac{\mathrm{grad}\sqrt{\epsilon}}{\sqrt{\epsilon}}, \quad \vec{\nu}_2 := \frac{\mathrm{grad}\sqrt{\mu}}{\sqrt{\mu}} ,
$$

which is the **carrier identity** of *Electromagnetism in Media — The Local Complex Structure at Work*, read in the static case, where no time coordinate is present and the operator is the Moisil–Theodorescu operator $D$ alone, in the corpus's normalization $D=i\vec\nabla$. The Dirac side has the same shape: the massive equation with an electric potential, and separately with a scalar potential, becomes after the dictionary a first-order equation whose only position dependence is a coefficient multiplying one basis direction, as recorded in *The Dirac Equation in Biquaternionic Form*, §*The Dirac Operator with Potentials in Quaternionic Form*. Matching the two shapes, the 2003 paper concludes that a solution of the Dirac equation with an electric or a scalar potential is a solution of the static Maxwell system of an isotropic inhomogeneous medium, the medium being the potential read as a parameter:

$$
\epsilon = \exp(\,2G(r_x)), \qquad G(r_x) = \int g(r_x)\,dr_x ,
$$

with $g$ the Dirac potential. The identification is a statement about **coefficients** and not about fields: the potential is the logarithmic derivative of the square root of the permittivity, $\vec{\nu} = \mathrm{grad}\,G$, which is checked at once from $\sqrt{\epsilon} = \exp(G)$. What the correspondence does not do is identify the Dirac field with the electromagnetic field — the Dirac biquaternion and the field-strength biquaternion are different objects, and the matching is at the level of the equations they solve, with the restriction $\mathrm{Sc} = 0$ on the Maxwell side. The corpus records it because both ends already exist here, the carrier function of the media article and the potential coupling of the Dirac article, and this is the statement that joins them.

**What is quoted.** The source's own forms of the two reduced operators, for the electric and for the scalar potential, are partly illegible in the scan. What is legible, and what is recorded above, is the shape of the reduction, the normalisation by $\sqrt{\epsilon}$, and the parameter $\epsilon = \exp(2G)$ with $\vec\nu = \mathrm{grad}\,G$; the identification of the potential with an inhomogeneity of that form is the source's statement, carried here as such.

## The Mass Shell as the Condition on the Dirac–Maxwell Correspondence

The time-harmonic comparison is the paper's last section, and its conclusion is a condition rather than an identity. Let the massive quaternionic equation be read on a time-harmonic field, as in *The Dirac Equation in Biquaternionic Form*, §*The Harmonic Field: Two Projections, and the Helicity Reading*. There the frequency is the Dirac frequency; write it $\omega_D$, and write $E=\hbar\,\omega_{D}$ for the particle energy. The amplitude obeys the shifted equation $\vec\nabla f+f\alpha=0$ at the parameter

$$
\alpha = -\left(\frac{i\,E}{\hbar\,c}\,\vec e_x + \vec e_y\,k_m\right),
$$

and the massless case of the same equation is the vacuum Maxwell equation. The time-harmonic Maxwell field of a homogeneous isotropic medium is likewise a pair of Beltrami fields, with its own frequency $\omega$ and wave number $k_\Phi=\omega\sqrt{\epsilon\mu}=\omega/c$, and the projection identity that relates the two pairs,

$$
\vec\nabla f+f\alpha = \tfrac12\bigl(\vec\nabla f+fk_\Phi\bigr)\bigl(e_t+\alpha/k_\Phi\bigr) + \tfrac12\bigl(\vec\nabla f-fk_\Phi\bigr)\bigl(e_t-\alpha/k_\Phi\bigr),
$$

holds in both directions, with the two terms genuine projections of the two Maxwell pairs, **if and only if** the Maxwell wave number and the Dirac parameter agree,

$$
k_\Phi^2 = \alpha^2 .
$$

The parameter's square is central, because the two units anticommute:

$$
\alpha^2 =\frac{E^{2}}{\hbar^{2}\,c^{2}} - k_m^{2} .
$$

The condition is therefore

$$
\boxed{\;\frac{\omega^2}{c^2} =\frac{E^{2}}{\hbar^{2}\,c^{2}} - k_m^{2}
\quad\Longleftrightarrow\quad
E^2 =\hbar^{2}\,\omega^{2}+m^{2}\,c^{4}},
$$

which, with the de Broglie relation $\hbar\,\omega=pc$ for the Maxwell wave number, is the relativistic dispersion relation $E^2=p^2c^2+m^{2}\,c^{4}$. With the constants carried it reads $k_{t}^{\prime\,2}=k_{\Phi}^{2}+k_m^{2}$, the same statement in the three wave numbers. The paper draws attention to the agreement — the condition on which its Dirac–Maxwell equivalence rests is the same relation that defines the particle's mass — and the corpus records it as what ties the parametric statements together: the parameter that makes the shifted equation solvable is the parameter that puts the field on shell.

The same interpretation is why the massless (neutrino) case of §*The Harmonic Field: Two Projections, and the Helicity Reading* of *The Dirac Equation in Biquaternionic Form* needs no condition at all: at $m=0$, that is $k_m=0$, the parameter is $\alpha=-(i\,k_{t}^{\prime})\,\vec e_x$ with $\alpha^2=E^2/(\hbar^{2}\,c^{2})$, and $k_\Phi^2=\alpha^2$ becomes $\omega^2=\frac{E^{2}}{\hbar^{2}}$, i.e., $\omega=\omega_D$ — the two frequencies coincide, the vacuum null-wave relation $\omega=k_\Phi$, the case the source calls the neutrino, and the one the corpus records as Imaeda's vacuum Maxwell equation.

**What is quoted.** The source's intermediate equations, which restore $c$ and $\hbar$ at a different point of the reduction, are quoted as its own; the printed power of $c$ in them could not be read from the scan. The two statements used above — the condition $k_\Phi^2=\alpha^2$ and the central value of $\alpha^2$ in terms of the energy and the mass — are legible, and the mass-shell interpretation follows from them.

## The Lanczos Route: Maxwell with Feedback

The identity of form is not an artifact of the notation, and Lanczos read it as a statement about matter. In his 1929 articles he derived Dirac's equation from the coupled biquaternion system

$$
\tilde{\nabla}\tilde{Q}_1 = \tilde{Q}_2\,k_m, \qquad \tilde{\nabla}\tilde{Q}_2 = \tilde{Q}_1\,k_m,
$$

comparing it with the biquaternion Maxwell equation $\tilde{\nabla}\tilde{F} = -4\pi\tilde{J}_{\Phi}$ of the companion article. The first equation is then Maxwell's equation, and the second is a **feedback**: the field $\tilde{Q}_2$ acts back on the object that generates it, with the strength $k_m$. The feedback is the mass; the massless case $m=0$ breaks the coupling and leaves two independent field equations, of which the Maxwell equation is one. This is the source's interpretation, and it answers the question at the end of this article: what the Dirac and Maxwell equations share is the **operator** — the single first-order operator $\tilde{\nabla}$, a square root of $\Box$ — and what separates them is the **closure**, the Dirac field obeying the operator in the closed, self-acting way and the Maxwell field in the sourced way.

The corpus's chiral pair $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = k_m\,\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\,\tilde{Ξ}_{\mathrm{sp},R}$ is the same equation in the chiral variables — the second member carries $\tilde{\nabla}^{\natural}$ because the field written $L$ is the conjugate of the Lanczos $\tilde{Q}_2$ — and it displays the field split into its two parts, but not the direction that the Lanczos form makes explicit. Lanczos reached the Dirac equation from the pair by a superposition along an arbitrary axis (in the displays of this paragraph the letter $D$ is Lanczos's name for the Dirac field, not the spatial operator $D=i\vec\nabla$ of *An Explicit Dictionary with Conjugation in the Mass Term*)

$$
D = \tilde{Q}_1\tilde{\Pi} + \tilde{Q}_2^{*}\bar{\tilde{\Pi}},
$$

with $\tilde{\Pi}$ the projection along a unit vector $\vec{\nu}$ and $\bar{\tilde{\Pi}}$ its conjugate — so that one half of $\tilde{Q}_1$ and half of the conjugate of $\tilde{Q}_2$ are carried into the two **different** parts of the field, which is what makes the superposition a field carrying both values and not a field carrying one; the resulting single equation

$$
\boxed{\;\tilde{\nabla}D = D^{*}i\vec{\nu}\,k_m\;}
$$

is strictly equivalent to Dirac's equation. The unit vector on the right is the point of the display: it is the **spin quantization axis**, and it shows that Dirac's equation singles out an arbitrary but unique direction in ordinary space. The corpus's pair is written for a fixed frame and does not exhibit the axis; the Lanczos form shows that the axis is carried by the projection itself, and that any unit vector will do. The complex conjugation on the right-hand side is a second such fact: it is what makes the Dirac field **fermionic**, in contrast with the Maxwell and Proca fields, which are bosonic. The superposition is not unique: the source's second and equally covariant combination — Gürsey's, which the isospin reading makes the neutron to the proton — is recorded in *The Standard Model under the Biquaternion Framework — A Research Agenda*; the fermionic character above is what the two share.

**The other road to the same halving.** The superposition along the axis is not the only way the doubled system becomes Dirac's, and the source records a second one. "One can go from (1) to (3) by simply requiring that $A$ and $B$ are singular quaternions" — an observation the authors attribute to Blaton (1935), where (3) is the two-field pair $\partial L = mR$, $\partial R = mL$. The two routes reach the same place by different means: the superposition splits each field into its two parts and adds the halves *across* the two parts, whereas the singularity condition degenerates the fields themselves. The destination, however, is the corpus's own object — a singular biquaternion is a zero divisor — so this interpretation of the reduction says that the Dirac field is what the doubled Lanczos system becomes when both of its fields are confined to the singular set. The source is careful about what the halving alone does not buy: Dirac's system "does not only involve half as many components as Lanczos's system (1), it also incorporates the ingredients that make fermions essentially different from bosons", which are the complex conjugation and the singled-out direction recorded just above. That distinction is why the corpus keeps *N-Regularity and N-Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors* and *The Dirac Equation in Biquaternionic Form* apart: the halving is a fact about the algebra, while the fermionic character is a fact about the superposition.

## Open Questions

1. **The relation to the biquaternion Maxwell equation.** The two equations have the same form. Is there a deeper sense in which the photon and the electron are the same biquaternion field in different representations, or is the identity purely formal? **Partly answered**, in §*The Lanczos Route: Maxwell with Feedback* above: the shared object is the **operator** and the Dirac equation is the **closed** (feedback) way of obeying it, so the identity is structural rather than merely formal, and the fermionic statistics follow from the complex conjugation in the Lanczos form. What remains open is the feedback itself — the framework represents the mass feedback but does not derive it.

2. **The minimal coupling to electromagnetism.** The standard Dirac equation couples to the electromagnetic field through the minimal coupling $\partial/\partial R_\mu \to \partial/\partial R_\mu -\frac{iqA_{\mu}}{\hbar}$. How this coupling reads in the biquaternion framework, given the biquaternion form of the four-potential $\tilde{A}_{\Phi} = i\,a'_t\,e_t + \vec A$, is treated in the companion article *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*.

These questions are open.

## Summary

**The operator is shared; the objects are not.** The massless Dirac member and the source-free Maxwell equation are $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=0$ and $\tilde\nabla\tilde F=0$, one operator acting on the left, and the fields differ: $\tilde F$ lives in the vector part of the algebra and carries spin $1$, while $\tilde{Ξ}_{\mathrm{sp},R}$ is a general element carrying a value and spin $\frac12$. The identity of form is a statement about the multiplication and not about the objects.

**The mass is the term that has no Maxwell counterpart.** It is central and multiplies on the left, so it relates the two components of the Dirac pair and moves no value across; written with the direction on the right, $-i\overline{F}\,\vec e_z\,k_m$, it conjugates the coefficients and multiplies on the right, and those are the operations that carry a letter across. The two writings are one term in two variables, and the change of variable between them is the dictionary of the main article.

**Two comparisons, one dictionary and one condition.** A massive Dirac field with an electric or a scalar potential is, after the dictionary, the static sourceless Maxwell system of an isotropic inhomogeneous medium whose permittivity is $\epsilon=\exp(2G)$ with $dG/dr_x=g$, the potential being the logarithmic derivative of $\sqrt\epsilon$; the match is at the level of coefficients and carries the restriction $\mathrm{Sc}=0$ on the Maxwell side. On time-harmonic fields the Dirac pair and the Maxwell pair of a homogeneous medium share one projection identity exactly when $k_\Phi^2=\alpha^2$, and that condition, with $\alpha^2=\frac{E^{2}}{\hbar^{2}\,c^{2}}-k_m^{2}$, is $E^2=\hbar^{2}\,\omega^{2}+m^{2}c^{4}$, the relativistic dispersion relation.

**The Lanczos reading names the shared object.** Lanczos derived the Dirac equation from the coupled system $\tilde\nabla\tilde Q_1=\tilde Q_2k_m$, $\tilde\nabla\tilde Q_2=\tilde Q_1k_m$, whose first member is Maxwell's equation and whose second is a feedback of strength $k_m$, the mass. The Dirac field obeys the operator in the closed, self-acting way and the Maxwell field in the sourced way. The superposition along an axis, $\tilde\nabla_\Phi D=D^{*}i\vec\nu\,k_m$, adds the spin-quantization axis and the complex conjugation that make the field fermionic, and it is equivalent to Dirac's equation. What remains open is the feedback itself: the framework represents it and does not derive it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | The biquaternion algebra, $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $\tilde\nabla$, $\tilde\nabla^{\natural}$, $\Box$ | The gradient, its quaternion conjugate and their product $\tilde\nabla\tilde\nabla^{\natural}=\Box$ |
| $\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde{Ξ}_{\mathrm{sp},R}$ | The two components of the Dirac field, named by the letters of the pair |
| $k_m=\dfrac{mc}{\hbar}$ | The mass wave number, the coefficient of the mass term |
| $\tilde F$ | The field-strength biquaternion, the vector part of $\mathbb{B}$ |
| $\tilde J_\Phi$ | The source biquaternion of the inhomogeneous Maxwell equation |
| $k_\Phi=\omega\sqrt{\epsilon\mu}$ | The Maxwell wave number of the medium |
| $\epsilon$, $\mu$, $\vec\nu$ | Permittivity, permeability and the logarithmic derivative $\vec\nu=\mathrm{grad}\sqrt\epsilon/\sqrt\epsilon$ |
| $G(r_x)$, $g(r_x)$ | The Dirac potential as an integral and as its derivative, $\epsilon=\exp(2G)$, $dG/dr_x=g$ |
| $\alpha$ | The biquaternionic parameter of the shifted amplitude equation, an inverse length |
| $E$, $p$ | Particle energy and momentum; $E=\hbar\,\omega_D$ and $E=pc$ for the Maxwell wave number |
| $\tilde Q_1$, $\tilde Q_2$ | Lanczos's two biquaternion fields |
| $D$ | In §*The Lanczos Route* only, Lanczos's name for the Dirac field, not the spatial operator $D=i\vec\nabla$ |
| $\tilde\Pi$, $\bar{\tilde\Pi}$ | The projection along the unit vector $\vec\nu$ of the Lanczos superposition and its conjugate |

## Further Reading

- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), for the chiral pair, the two components, the value of an element and the two-sided dictionary that this article uses.
- [Explicit Solutions of the Biquaternionic Dirac Equation](explicit-solutions-of-the-biquaternionic-dirac-equation.html), for the plane waves, the completed spherical and cylindrical solutions and the scalar-potential completion.
- [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html), for the source-free equation $\tilde\nabla\tilde F=0$ and the sourced one $\tilde\nabla\tilde F=-4\pi\tilde J_\Phi$.
- [Electromagnetism in Media — The Local Complex Structure at Work](electromagnetism-in-media-the-local-complex-structure-at-work.html), for the carrier identity that the static case of the dictionary reads.
- [The Time-Harmonic Maxwell Operator and the Quaternionic Cauchy Integral](the-time-harmonic-maxwell-operator-and-the-quaternionic-cauchy-integral.html), for the parametric system that is Maxwell's at one value of its parameter and Dirac's at another.

- K. Imaeda, "A new formulation of classical electrodynamics," *Il Nuovo Cimento B* **32** (1976) 138–162, for the quaternionic vacuum Maxwell equation $i\partial/\partial r'_tF+DF=0$, the equation the dictionary reduces to at vanishing mass.
- C. Lanczos, "Die tensoranalytischen Beziehungen der Diracschen Gleichung," *Zeitschrift für Physik* **57** (1929) 447–473, 474–483, 484–493 (arXiv:physics/0508002, physics/0508012, physics/0508013), for the coupled biquaternion system from which the Dirac equation descends and for the superposition along an axis that produces it.
- F. Gürsey, "Applications of Quaternions to Field Equations," PhD thesis, University of London, 1950, for the review of Lanczos's quaternionic theory and for the treatment of the scalar, vector, pseudoscalar and pseudovector equations as degenerate cases of it.
- A. Gsponer and J.-P. Hurni, "The physical heritage of Sir W. R. Hamilton," arXiv:math-ph/0201058, §8, for the interpretation of Lanczos's system as Maxwell's equation with feedback, for the spin-quantization-axis form $\tilde{\nabla}D=mD^{*}i\vec{\nu}$ of the Dirac–Lanczos equation, and for the complex-conjugation origin of the fermionic character.
- A. Gsponer and J.-P. Hurni, "Lanczos's Equation to Replace Dirac's Equation?", *Proceedings of the Cornelius Lanczos International Centenary Conference* (SIAM, 1994) 509–512 (arXiv:hep-ph/0112317), for Lanczos's coupled system as "Maxwell's equations with feed-back" and for the second route to Dirac's equation, the reduction by requiring the two fields to be singular quaternions, attributed there to J. Blaton, *Zeitschrift für Physik* **95** (1935) 337–354. Recorded as a claim: four pages, no derivation exhibited, and the title is a question; the arXiv version carries a *Note added in 1996* withdrawing the authors' charge-quantisation mechanism, which is recorded in *The Standard Model under the Biquaternion Framework — A Research Agenda*.
- V. V. Kravchenko and M. P. Ramirez Tachiquin, "On a quaternionic reformulation of the Dirac equation and its relationship with Maxwell's system," *Bulletin de la Société des Sciences et des Lettres de Łódź* **53** (2003) 101–114, for the correspondence between the massive Dirac equation with an electric or a scalar potential and the static sourceless Maxwell system of an isotropic inhomogeneous medium, with the permittivity $\epsilon=\exp(2G(r_x))$, $dG/dr_x=g$; for the condition $k_\Phi^2=\alpha^2$ under which the massive Dirac field and the time-harmonic Maxwell field share the same projection identity, that condition being the mass shell; and, in the same paper, for the reality of the conjugation-free quaternionic Dirac operator and the current-conservation equation recorded in *The Dirac Equation in Biquaternionic Form*, §*The Conjugation-Free Operator and Its Reality*. The paper's factors $u^{\pm}$ and its explicit action of $A^{-1}$ on $\mathrm{Re}\,F$ are quoted, not reproduced: the available copy is a scan without a text layer.
