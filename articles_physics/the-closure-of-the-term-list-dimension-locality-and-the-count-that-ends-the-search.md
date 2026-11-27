# __The Closure of the Term List: Dimension, Locality and the Count That Ends the Search__

## Introduction

**The claim.** The list of terms in a density closes because **locality bounds the derivative count, dimension bounds the total degree, and the carrier bounds the available contractions** — and at each dimension the number of ways to contract is finite. The search for terms therefore ends, and it ends by counting. **This is what makes "the only dimension-four invariant" a conclusion and not a boast.**

**What this article is not.** The hub's [why the quadratic and nothing else](the-invariant-density-which-pairing-the-action-can-integrate.html) is this count applied to the **curvature alone**, and it closes on dimension four. [The invariance filter](which-terms-survive-invariance-as-a-linear-condition-on-a-density.html) is what decides, term by term, which of the counted candidates survive. **This article does the count for the whole density** — connection, fermion and scalar at once — and states the three things the count does *not* close, because a closure claim that hides its exceptions is not a closure claim.

## The Three Bounds

**Locality.** The density at a point depends on the fields and finitely many of their derivatives. **This is what makes the candidate set finite at each degree**: without it, a term could carry any number of derivatives and the list would not close.

**Dimension.** With $\hbar=c=1$, a derivative has dimension one, a vector field one, a scalar one, a fermion $\tfrac32$, and the density must have dimension four. **A term's dimension is the sum over its factors**, so

$$
d=k+\sum_i p_i\,\delta_i ,
$$

with $k$ the derivative count, $p_i$ the number of fields of type $i$, and $\delta_i$ their dimensions. **Since $d=4$ and every $\delta_i>0$, the number of fields is bounded above**, and with it the number of derivatives. That is the closure, and it is arithmetic.

**The carrier's contractions.** At a given dimension and field content, the number of ways to contract the indices is finite because the carrier's invariant tensors are finitely many. **The trace, the scalar part, the Hermitian form, $\varepsilon_{\imath\jmath\kappa\lambda}$ and the generators' symmetric and antisymmetric invariant tensors** are the whole list used in this corpus. A term is a choice among these contractions, and there are finitely many choices.

**One sentence for the three.** **Locality bounds the derivatives, dimension bounds the fields, and the carrier bounds the contractions** — so the candidate space at dimension four is finite, and the filter's job is to run over a finite list rather than to invent one.

## The Count, for the Whole Density

**With one connection, one fermion and one scalar, the dimension-four candidates are these and no others:**

| candidate | dimension | admitted? | note |
|---|---|---|---|
| $\operatorname{tr}\sum F_{\imath\jmath}F_{\imath\jmath}$ | $4$ | **yes** | the gauge kinetic term |
| $\bar\Xi\,\gamma^\imath D_\imath\Xi$ | $4$ | **yes** | the fermion kinetic term |
| $\operatorname{tr}\bigl(D_\imath\Xi\bigr)^{\dagger}\bigl(D^\imath\Xi\bigr)$ | $4$ | **yes** | the scalar kinetic term |
| $(\operatorname{tr}\Xi^2)^2$ and the other quartics | $4$ | **yes** | all admitted; none selected — [the residue](what-invariance-cannot-decide-declared-coefficients-signs-and-normalisations.html) |
| $\bar\Xi\,\Xi\,\Xi$ (Yukawa) | $4$ | **yes** | with the scalar insertion |
| $\varepsilon^{\imath\jmath\kappa\lambda}\operatorname{tr}F_{\imath\jmath}F_{\kappa\lambda}$ | $4$ | **yes, and inert** | a total derivative |
| $m^2\sum A_\imath A_\imath$ | $4$ | **no** | [the gauge mass](one-obstruction-four-groups-the-gauge-mass-that-is-never-admitted.html) |
| $\operatorname{tr}F^3$ | $6$ | out of range at $d=4$ | excluded by dimension **here**; at $d=6$ **the group decides** — $d_{abc}=0$ for $\mathrm{SU}(2)$ only |
| $\bar\Xi\sigma^{\imath\jmath}F_{\imath\jmath}\Xi$ | $5$ | out of range | the Pauli term; non-renormalisable |
| $(\bar\Xi\Xi)^2$ | $6$ | out of range | a four-fermion term |

**Read the table as three verdicts per row**: *there is such a term*, *it is invariant or not*, and *its dimension is admissible or not*. **The first is the count's, the second is the filter's, the third is the closure's**, and a row can fail any of the three for a different reason. That is why the corpus's sentences about excluded terms should say which of the three they are using; the $F^3$ exclusion is dimensional and the gauge-mass exclusion is invariance, and the two are not the same argument. **And the $d_{abc}$ question is a third question again, not an idle one: at dimension four it does not arise, and at dimension six it decides $\operatorname{tr}F^3$ — and decides it by group.** A closure that reported *the cubic is excluded because $d_{abc}$ vanishes* would be answering at the wrong dimension; a closure that reported *the cubic is excluded, full stop* would be hiding a survivor that exists for $\mathrm{SU}(3)$ and $\mathrm{SU}(4)$ and not for $\mathrm{SU}(2)$.

**The table is short because the field content is short.** Add a second scalar and $\Xi_1^\dagger\Xi_2$ appears; add a second fermion and a mixing Yukawa appears. **The count does not say the list is short in general; it says the list is finite for a given content**, which is the only thing a closure claim can honestly be.

## Where the Count Does Not Close, and Must Not Pretend To

**Three exceptions, and each is a real part of the corpus rather than a defect.**

**First, lower-dimension terms are not excluded by dimension, only by symmetry.** A scalar mass $\operatorname{tr}\Xi^2$ has dimension two, a fermion mass $\bar\Xi\Xi$ dimension three, a cubic $\operatorname{tr}\Xi^2\operatorname{tr}\Xi$ dimension three. **A dimension-four count does not forbid them and never claimed to** — it forbids dimension five and above. Whether they appear is decided by the symmetry the corpus chooses to impose. The primordial potential writes two cubics, which is exactly this: **no $\Xi\mapsto-\Xi$ symmetry is imposed on that matrix, so the cubics are admitted and written.** A potential that "has only quartics" is a potential with a discrete symmetry, and the symmetry is a choice.

**Second, the topological term is admitted, dimension-four and inert.** $\varepsilon\operatorname{tr}FF$ is the one further invariant at dimension four, its integral is quantised, and its coefficient is a free parameter — the primordial article says so and calls $\theta_4$ "a free parameter of the Lagrangian and not a function of the group". **The count finds it and invariance admits it; nothing in either excludes it.** Its coefficient is [the residue](what-invariance-cannot-decide-declared-coefficients-signs-and-normalisations.html), and its physical status is a separate question.

**Third, the count is silent about terms built from objects the corpus has not introduced.** A term with a dual curvature, a term with a second connection, a term with a torsion — each is dimension-four or not, and none is in the table because the object is not in the theory. **The closure is relative to the field content, and the field content is the corpus's choice.** That is the honest form of the claim, and it is weaker than *nothing else can be written* and stronger than *these are the terms we happen to use*.

## Why the Count Is What Ends the Search

**Because a filter without a finite domain is not a procedure.** The invariance test is linear and computable, but *computable over what* has to be answered first. **The count answers it**: the candidate space is finite at dimension four, so the filter runs to completion, and the short list of admitted terms is a result rather than an impression.

**This is the sense in which the two filters are ordered.** The count and the carrier fix the domain; invariance selects inside it. **Neither can substitute for the other**: a count without invariance gives every admissible-dimension contraction, and invariance without a count has nothing finite to run on. **The corpus's *one action per force* is the composition of the two**, and it is why four sectors with four groups arrive at the same short list — the domain is the same, and the selection is the same.

**And the honest ceiling.** The count proves finiteness and not uniqueness. **Several admitted terms of the same dimension remain, and their coefficients are declared** — which is the next article's subject, and the reason this article's title says *the count that ends the search* and not *the count that fixes the answer*.

## Summary

The term list closes on three bounds: **locality** bounds the derivative count, **dimension** bounds the total field content, and **the carrier** bounds the contractions. At dimension four with one connection, one fermion and one scalar the candidates are the curvature square, the two kinetic terms, the potential's quartics, the Yukawa and the topological density; the gauge mass is a candidate and fails invariance; $F^3$, the Pauli term and the four-fermion term fail dimension.

**Each row fails for one of three different reasons — no such term, not invariant, out of range — and the corpus should name which.** The $F^3$ exclusion is dimensional *at dimension four*, the gauge-mass exclusion is invariance, and treating them as one argument is the error this article exists to prevent. **The $d_{abc}$ question is a third and it is where the group enters the count: at dimension six, $\operatorname{tr}F^3$ is admitted by $\mathrm{SU}(3)$ and $\mathrm{SU}(4)$ and forbidden by $\mathrm{SU}(2)$ — the same candidate, the same dimension, a group-dependent verdict.** That is the section's first claim appearing inside the closure, and the count must leave room for it.

The count does not close everything and does not claim to. **Lower-dimension terms are excluded by symmetry and not by dimension**, which is why the primordial potential writes two cubics — no discrete symmetry is imposed there. **The topological term is admitted and inert**, its coefficient a free parameter. **And the closure is relative to the field content**, which is the corpus's choice.

**The count's job is to make the invariance filter runnable**: it supplies the finite domain, invariance selects inside it, and their composition is the short list the sectors share. **The count proves finiteness; it does not prove uniqueness** — the residue is declared, and that is the next article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | The derivative count of a term |
| $p_i$, $\delta_i$ | The number of fields of type $i$, and that type's dimension |
| $\delta$ | Field dimensions: $1$ (scalar, vector), $\tfrac32$ (fermion) |
| $\varepsilon^{\imath\jmath\kappa\lambda}$ | The Levi-Civita symbol, the fourth invariant tensor used |
| $\theta_4$ | The topological term's coefficient; a free parameter, not a function of the group |
| $\operatorname{tr}\Xi^2\operatorname{tr}\Xi$ | A dimension-three cubic; admitted where no discrete symmetry excludes it |

## Further Reading

- [The Invariant Density: Which Pairing the Action Can Integrate](the-invariant-density-which-pairing-the-action-can-integrate.html) — the same count for the curvature alone, and why the cubic is excluded by dimension *at $d=4$* and not by $d_{abc}$ — with $d_{abc}$ deferred to dimension six, where it does decide.
- [Which Terms Survive: Invariance as a Linear Condition on a Density](which-terms-survive-invariance-as-a-linear-condition-on-a-density.html) — the filter that runs on the counted list.
- [One Obstruction, Four Groups: The Gauge Mass That Is Never Admitted](one-obstruction-four-groups-the-gauge-mass-that-is-never-admitted.html) — the exclusion that is invariance and not dimension.
- [What Invariance Cannot Decide: Declared Coefficients, Signs and Normalisations](what-invariance-cannot-decide-declared-coefficients-signs-and-normalisations.html) — the residue the count leaves.
- [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html) — the potential with cubics, and $\theta_4$ as a free parameter.
- [The Lagrangian and Quantum Chromodynamics: The Triplet, the Octet and the Feynman Rules](the-lagrangian-and-quantum-chromodynamics-the-triplet-the-octet-and-the-feynman-rules.html) — "the square shown to be the only dimension-four invariant".
