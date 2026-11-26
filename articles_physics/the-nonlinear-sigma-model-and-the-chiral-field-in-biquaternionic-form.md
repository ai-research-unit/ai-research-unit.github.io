# __The Nonlinear Sigma Model and the Chiral Field in Biquaternionic Form__

## Introduction

The object. A nonlinear sigma model is a field theory whose field takes values in a curved target manifold, with a Lagrangian that is the kinetic energy of the map from spacetime into that manifold. The simplest instance has target the sphere $\mathbb{S}^{N-1}$; the case that appears in particle physics has target a group, and the field is the chiral field.

What this article is. The general construction, with no sector attached: the nonlinear realisation of a broken symmetry, the passage from a linear model to a nonlinear one, the geometric Lagrangian, the flat current and its conservation, power counting, and the effective-field-theory reading. It names no force.

Where the applications are.

- The strong sector, in two places. The pion is the Goldstone of the spontaneously broken chiral symmetry and its low-energy dynamics is this model: [The Chiral Theory and the Lagrangian: The Pion and the Decay Constant](the-chiral-theory-and-the-lagrangian-the-pion-and-the-decay-constant.html). The baryon as a soliton of that field is [The Skyrme Model and the Topological Baryon in Biquaternionic Form](the-skyrme-model-and-the-topological-baryon-in-biquaternionic-form.html).
- The electroweak sector, nowhere. The electroweak scalar is a doublet with a potential, not a group-valued field, and the sigma model is not its low-energy limit in this corpus.

Why the general form is separable. The model is a statement about a target manifold and a symmetry that is realised nonlinearly. The force enters only when the target and the symmetry are named: $SU(2)_L\times SU(2)_R\to SU(2)_V$ for the pion, and nothing else here.

## The Nonlinear Realisation

The setup. A symmetry group $G$ is broken spontaneously to a subgroup $H$. The Goldstone fields are coordinates on the coset $G/H$, and the field is a map

$$
\tilde U:\ \mathbb{R}^{3,1}\longrightarrow G/H,
$$

written as a group element modulo the right action of $H$.

The transformation. $G$ acts by left multiplication, $\tilde U\mapsto g\,\tilde U$, and the action is nonlinear in the coordinates because the coset is not a group. The nonlinearity is the content: it is what encodes the broken symmetry in a theory with no potential.

**The counting.** $\dim(G/H)$ Goldstone fields, one per broken generator, and no more. A linear model with the same symmetry contains the same number of Goldstones plus a heavy radial field, and the nonlinear model is the limit in which the radial field is removed.

## From the Linear to the Nonlinear Model

The limit. A linear model with a potential whose minimum is not at the origin has a radial mode of mass $m$ and Goldstones of zero mass. Taking $m\to\infty$ at fixed Goldstone decay constant freezes the radial coordinate to the minimum and leaves a field valued in the coset.

**What survives.** The Goldstones, their low-energy theorems, and the derivative couplings that the symmetry fixes. What is lost is the radial field and everything above its mass.

The decay constant. The scale of the freezing is a parameter, $f$, with dimensions of mass, and every amplitude is a series in $E/f$. The parameter is not fixed by the symmetry; it is measured.

## The Geometric Lagrangian

The leading term. With $\tilde U$ group-valued and the trace written as $2\,\mathrm{Sc}$,

$$
\boxed{\;\mathcal{L}_2 = -\,\frac{f^2}{2}\,\mathrm{Sc}\!\left(\overline{\partial_{\imath}\tilde U}\,\partial_{\imath}\tilde U\right)\;}
$$

which at quadratic order is the canonical kinetic term for the Goldstones.

The currents. The left and right currents $j_{\imath}=\tilde U^{\dagger}\partial_{\imath}\tilde U$ and $\tilde U\partial_{\imath}\tilde U^{\dagger}$ are pure connections, so their field strength vanishes:

$$
\boxed{\;\partial_{\imath} j_{\jmath}-\partial_{\jmath} j_{\imath}+\left[j_{\imath},j_{\jmath}\right]=0\;}
$$

The identity is algebraic, not dynamical: the dynamics of a group-valued field is that of a connection constrained to be pure gradient, and the equation of motion is the conservation of the flat current.

**The higher terms.** Terms with four derivatives are not fixed by the symmetry and are organised by power counting; the term that stabilises the soliton is the first of them.

## Power Counting and the Effective Theory

The expansion parameter. Each derivative costs a power of the momentum, so the Lagrangian is a series

$$
\mathcal{L}=\mathcal{L}_2+\frac{1}{\Lambda^2}\mathcal{L}_4+\cdots
$$

with $\Lambda$ the scale of the physics that has been integrated out, of order $4\pi f$.

The predictive content. At low energy only the leading term matters, so the model makes statements that are exact in the symmetry and approximate in the energy. This is the defining property of an effective field theory, and it is why the model is the correct low-energy description of a broken symmetry whatever the ultraviolet completion.

**The limit of the method.** At energies comparable to $\Lambda$ the series must be truncated by new physics, and a loop expansion of the model alone is not renormalisable in the ordinary sense; the counterterms are the higher terms, order by order.

## What the Framework Supplies

- **Supplied.** The group-valued target and the trace. The algebra's unit quaternions are $S^3=\mathrm{SU}(2)$, so the simplest non-abelian target is the algebra's own sphere, and $\mathrm{Sc}$ is the trace the Lagrangian needs.
- **Imported.** The coset construction, the power counting and the effective-field-theory reading. These are standard, transcribed.
- **Not supplied.** A force. The target, the symmetry and the decay constant are the sector's to name.

Where the applications are. [The Chiral Theory and the Lagrangian: The Pion and the Decay Constant](the-chiral-theory-and-the-lagrangian-the-pion-and-the-decay-constant.html) names the target and the symmetry for the pion. [The Skyrme Model and the Topological Baryon in Biquaternionic Form](the-skyrme-model-and-the-topological-baryon-in-biquaternionic-form.html) adds the fourth-order term and reads baryon number as a winding number.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde U$ | the group-valued chiral field |
| $G,H$ | the symmetry group and the unbroken subgroup |
| $f$ | the decay constant |
| $j_{\imath}$ | the flat current |
| $\Lambda$ | the scale of the integrated-out physics |

## Further Reading

- S. Weinberg, "Nonlinear Realizations of Chiral Symmetry," *Physical Review* **166** (1968) 1568, the nonlinear realisation.
- J. Gasser and H. Leutwyler, "Chiral Perturbation Theory to One Loop," *Annals of Physics* **158** (1984) 142–210, the power counting.
- S. Weinberg, *The Quantum Theory of Fields*, Volume II, Chapter 19, for the effective-field-theory reading.
