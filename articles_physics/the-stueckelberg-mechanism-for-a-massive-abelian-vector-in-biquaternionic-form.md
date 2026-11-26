# __The Stueckelberg Mechanism for a Massive Abelian Vector in Biquaternionic Form__

## Introduction

**The object.** A mass term $-\tfrac12\mu^2 A_{\imath} A_{\imath}$ is not invariant under an abelian local transformation $A_{\imath}\mapsto A_{\imath}-\partial_{\imath}\Gamma$. A massive vector is therefore either a connection whose symmetry has been broken by hand, or a connection whose mass is carried by an extra field. The **Stueckelberg mechanism** is the second route: a scalar is introduced that shifts under the same transformation, the combination

$$
A_{\imath,\mathrm u}=A_{\imath}-\partial_{\imath}\xi
$$

is invariant, and the mass term written in that combination costs no symmetry.

**What this article is.** The general construction, with no sector attached. It states the obstruction, the invariant mass term, the fixing the representative, the degree-of-freedom count, and the relation to the abelian Higgs. The construction applies to any abelian connection, and this category contains one such field.

**Where the applications are.**

- The electroweak sector, where the massive $W$ and $Z$ are the case in point. The mechanism used there is not this one: the sector uses the Higgs, and the Stueckelberg route is the alternative it does not take. The application article is [The Stueckelberg Mechanism in Biquaternionic Form](the-stueckelberg-mechanism-in-biquaternionic-form.html), which works the construction in the framework's own notation and states which of the two routes the algebra can host.
- The strong sector, nowhere. $SU(3)$ is unbroken and its connections are massless.

## The Proca Obstruction

The Lagrangian of a massive vector with no scalar,

$$
\mathcal{L}_{\mathrm{P}}=-\tfrac12\langle\tilde F\rangle_{\natural}-\tfrac12\mu^2\langle\tilde A_\Phi\rangle_{\natural},
$$

is not invariant under $\tilde A_\Phi\mapsto\tilde A_\Phi-\tilde\nabla_\Phi\Gamma$, because the mass term is quadratic in the connection while the transformation is affine. The obstruction is not a technicality of notation: a mass term is a length, and a local symmetry forbids one.

**The consequences that follow from the obstruction.** The propagator of the Proca field has the form $(-g_{\imath\jmath}+k_{\imath} k_{\jmath}/\mu^2)/(k^2-\mu^2)$, whose longitudinal part grows with energy; the theory is not renormalisable by power counting; and the longitudinal mode is put in by hand as a third polarisation rather than arising from a field.

## The Invariant Mass Term

Introduce a scalar $\xi$ that shifts under the local transformation,

$$
\tilde A_\Phi\mapsto\tilde A_\Phi-\tilde\nabla_\Phi\Gamma,
\qquad
\xi\mapsto\xi+\Gamma .
$$

Then

$$
\boxed{\;\tilde A_{\Phi,\mathrm u}=\tilde A_{\Phi}-\tilde\nabla_\Phi\xi\;}
$$

is invariant, and the mass term written in it,

$$
\boxed{\;\mathcal{L}_{\mathrm{S}}=-\tfrac12\mathrm{Re}\langle\tilde F\rangle_{\natural}-\tfrac12\mu^2\langle\tilde A_{\Phi,\mathrm u}\rangle_{\natural}\;}
$$

is invariant for every $\Gamma$. The symmetry group is unchanged — the scalar shifts with the same parameter as the connection, so no new symmetry is introduced — and the mass is now compatible with it.

**The equations.** Variation with respect to the vector gives

$$
\boxed{\;\tilde\nabla_\Phi\tilde F-\mu^2\tilde A_{\Phi,\mathrm u}=0\;}
$$

and variation with respect to the scalar gives the constraint $\tilde\nabla_\Phi\tilde A_{\Phi,\mathrm u}=0$, so the invariant combination is transverse. The four components of $A$ and the one of $\xi$ reduce to three propagating polarisations: the scalar is eaten.

**The counting.** A massless vector has two polarisations and a shift scalar has one; a massive vector has three. The count is preserved, and nothing is lost — the scalar's degree of freedom has become the longitudinal polarisation.

## Choice of Representative and the Relation to the Abelian Higgs

**The unitary fixing condition.** Setting $\xi=0$ removes the scalar from the Lagrangian and leaves the Proca form, at the price of making the representative non-manifest. This is why the mechanism is often described as "the scalar is removed by a choice of representative": the description is correct in that representative and misleading outside it.

**The relation to the abelian Higgs.** The two Lagrangians are the same object. In the Higgs case a complex scalar acquires a vacuum expectation value $v$, the phase is the Goldstone, the radial field is the physical scalar, and the mass is $\mu=gv$. In the Stueckelberg case the scalar is not a Higgs, has no potential, and the mass is a parameter. The difference is interpretive and observable: the Higgs leaves a physical scalar and a symmetry-breaking vacuum, the Stueckelberg leaves neither.

**Renormalisability.** The abelian Stueckelberg theory is renormalisable. The non-abelian version is not, in the same form, because the shift field in a non-abelian theory is not a standard field and does not improve the power counting. The boundary is the abelian case, and it is the case that arises here.

## What the Framework Supplies

- **Supplied.** The invariant $\langle\tilde A_\Phi\rangle_{\natural}$ and the covariant derivative $\tilde\nabla_\Phi$, which are what the construction is written in, and a central phase that is abelian, so the abelian restriction is the framework's own situation.
- **Imported.** The mechanism itself, the shift field and the counting. These are standard field theory, transcribed.
- **Not supplied.** A broken symmetry. The framework's scalar is a singlet of its compact factor and a central scalar cannot break the compact group, so the Higgs route is not available and this is the route that is.

**Where the application is.** [The Stueckelberg Mechanism in Biquaternionic Form](the-stueckelberg-mechanism-in-biquaternionic-form.html) carries the construction in the framework's notation, fixes the representative, counts the degrees of freedom and states which parts of the algebra's reading carry over and which do not.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde A_\Phi$ | the abelian connection |
| $\Gamma$ | the parameter |
| $\xi$ | the shift scalar |
| $\tilde A_{\Phi,\mathrm u}$ | the invariant combination |
| $\mu$ | the vector mass |
| $v$ | the Higgs vacuum expectation value, for comparison only |

## Further Reading

- E. C. G. Stueckelberg, "Die Wechselwirkungskräfte in der Elektrodynamik und in der Feldtheorie der Kernkräfte," *Helvetica Physica Acta* **11** (1938) 225, the original.
- H. Ruegg and M. Ruiz-Altaba, "The Stueckelberg Field," *International Journal of Modern Physics A* **19** (2004) 3265–3347, the modern treatment.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory*, Chapter 21, for the counting against the Higgs.
