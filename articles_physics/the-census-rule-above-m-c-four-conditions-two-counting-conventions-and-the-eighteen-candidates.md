# __The Census Rule Above $M_C$: Four Conditions, Two Counting Conventions and the Eighteen Candidates__

## Introduction

**The question.** [The census](the-census-above-m-c-nineteen-structures-eighteen-admissible-eleven-written.html) reports nineteen candidates and eighteen admissible. **What test separates them, and where does the test come from?** This article states the test and runs it once.

**The answer.**

$$
19\ \xrightarrow{\ \text{not a total derivative}\ }\ 18 .
$$

**The rule is [the broken phase's rule](the-census-rule-dimension-four-residual-invariance-and-one-canonical-term-per-field.html) applied to a smaller content**, and the one structure it removes here is $\theta_4$. **The removal is not a judgement about importance; it is a statement that a total derivative integrates to a surface term.**

## The Four Conditions

**A structure is admissible when all four hold.**

| condition | what it excludes | example excluded |
|---|---|---|
| Lorentz scalar | anything carrying a free vector or spinor index | $A_{\imath}$ alone |
| local $\mathrm{SU}(4)$ invariance | anything not a singlet | $A_{\imath}$ alone again |
| dimension $\le4$ | higher-dimension operators | $F^{3}$, the Pauli term |
| **not a total derivative** | surface terms | $\theta_4$ |

**The fourth condition is the one that does work here.** The first three are shared with every effective field theory; **the fourth is what makes the census a list of operators rather than a list of integrands**, and it is applied identically above and below $M_C$.

**Dimension four or below, and the bound is a counting fact.** A derivative has dimension one, a vector field one, a scalar one, a fermion $\tfrac32$. **With $d\le4$ the field count is bounded**, and [the closure article](the-closure-of-the-term-list-dimension-locality-and-the-count-that-ends-the-search.html) shows the candidate set to be finite.

**Locality is the hidden fourth-and-a-half.** The density depends on the fields and finitely many derivatives, **which is what stops an infinite tower of $\partial^{n}$ terms from qualifying.**

## The Two Counting Conventions

**Two conventions sit on top of the four conditions, and neither is a condition.**

**The hermitian conjugate counts once.** $\mathcal{O}^{\dagger}$ is not a second structure; **it is the same structure's conjugate, and the pair is written as one row with $+\text{h.c.}$**

**A structure counts once per field it can be built on, and the coefficient is not looked at.** A row exists because the group admits it; **whether its coefficient is zero is a second question, answered in a different column.** That is why the census can print six zeros as rows and still be a count of what exists.

**These two conventions are where most miscounts happen.** A count that double-counted conjugates would report thirty-eight; **a count that dropped zero-coefficient rows would report eleven and call it the group's number**, which is the error the census's ladder is designed to expose.

## The Eighteen, by Class

**Nineteen candidates decompose into seven classes, and the total derivative is one of them.**

| class | count | rows |
|---|---|---|
| curvature square | $1$ | $1$ |
| **total derivative** | $1$ | $\theta_4$ |
| fermion kinetic | $1$ | $2$ |
| fermion mass | $1$ | $12$ |
| scalar kinetic | $2$ | $3$, and $(\partial\operatorname{tr}\Xi)^{2}$ |
| scalar potential | $11$ | $4$–$9$, $13$–$17$ |
| Yukawa | $2$ | $10$, $11$ |
| **total** | $\mathbf{19}$ | |

**The potential is eleven of the nineteen and that is the whole story of the count.** A doublet's potential has two monomials at degree four or below; **a Hermitian $4\times4$ has eleven**, by the partition count $1,2,3,5$.

**Two kinetic terms for one scalar, and only one survives normalisation.** Both are invariant, both are dimension four, **neither is a total derivative** — so both are admissible and the second is removed at the next rung. **The rule admits it; the normalisation declines it**; [the canonical basis](the-canonical-basis-above-m-c-one-rescaling-three-costs-and-the-numbers-that-are-not-invariants.html) shows the two to be related by one field redefinition.

## The One Removal

**$\theta_4$ is admissible by three conditions and excluded by the fourth.**

$$
\mathcal{L}_{\theta}=\theta_{4}\,\varepsilon^{\imath\jmath\kappa\lambda}\operatorname{tr}F_{\imath\jmath}F_{\kappa\lambda}
=\theta_{4}\,\partial_{\imath}K^{\imath},
\qquad
K^{\imath}=2\varepsilon^{\imath\jmath\kappa\lambda}\operatorname{tr}\bigl(A_{\jmath}\partial_{\kappa}A_{\lambda}-\tfrac{2i}{3}g_{4}A_{\jmath}A_{\kappa}A_{\lambda}\bigr).
$$

**It is a Lorentz scalar, it is invariant, and it is dimension four.** It is also **a total derivative, so it integrates to a surface term**, and a surface term is a boundary condition and not a coupling.

**The broken phase does exactly the same thing with $\theta_{\mathrm{QCD}}$.** There, the parameter is "present as a parameter and absent as a row"; **$\theta_4$ is that object above $M_C$**, and the phrase transfers unchanged.

**So the parameter stays and the row goes, and the two statements are consistent.** A reader who asks "where did $\theta_4$ go" is answered by [the coefficients article](the-coefficients-above-m-c-fifteen-constants-one-gauge-parameter-and-one-angle-without-a-row.html): **it is one of the parameters and none of the rows.**

## Why the Rule Is Not Modified Here

**A temptation, and why it is refused.** One could add a fifth condition — "not a topological term" — or subtract the fourth — "total derivatives allowed". **Both would produce a different census, and neither would be this one.**

**The rule is stated once and applied twice.** Above $M_C$ and below it, **the same four conditions run on different content**, and the difference in the answer comes from the content and not from the rule. **That is what makes the two censuses comparable**, and a rule that changed with the phase would make them incomparable.

**The rule's provenance is the broken phase's, and the article says so rather than deriving it again.** A derivation would be a derivation of the census rule as such, **and that article already exists**; this one applies it.

## Checks

1. The four conditions. Scalar, invariant, dimension $\le4$, not a total derivative.
2. The two conventions. Conjugates once; coefficient-blind.
3. The class sum. $1+1+1+1+2+11+2=19$.
4. The removal. $\theta_4$ is a total derivative and the fourth condition excludes it.
5. The one removal. $19-1=18$.
6. The potential. $1,2,3,5$ for degrees $1,2,3,4$, so $11$.
7. The parallel. $\theta_4$ above $M_C$ is $\theta_{\mathrm{QCD}}$ below it.

## Summary

**Four conditions define admissibility, and the fourth — not a total derivative — is the one that moves the count.** Nineteen candidates become eighteen when $\theta_4$ goes, **and $\theta_4$ goes because it integrates to a surface term.**

**Two conventions sit on top and are not conditions**: conjugates count once, and a row exists regardless of its coefficient. **Both are where counts go wrong.**

**The rule is the broken phase's, unmodified.** The same four conditions run on smaller content, **and the difference in the answer is the content's and not the rule's** — which is what lets the two censuses be compared.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\theta_4$ | the vacuum angle; a total derivative; a parameter with no row |
| $F_{\imath\jmath}$ | the $\mathrm{SU}(4)$ field strength |
| $K^{\imath}$ | the Chern–Simons current whose divergence is $\operatorname{tr}F\tilde F$ |
| candidate | a structure meeting the first three conditions |
| admissible | a candidate that is not a total derivative |

## Further Reading

- [The Census Above $M_C$](the-census-above-m-c-nineteen-structures-eighteen-admissible-eleven-written.html). The full ladder from nineteen to eleven.
- [The Census Rule](the-census-rule-dimension-four-residual-invariance-and-one-canonical-term-per-field.html). The broken phase's statement of the same rule.
- [The Closure of the Term List](the-closure-of-the-term-list-dimension-locality-and-the-count-that-ends-the-search.html). Why the candidate set is finite.
- [The Coefficients Above $M_C$](the-coefficients-above-m-c-fifteen-constants-one-gauge-parameter-and-one-angle-without-a-row.html). $\theta_4$ as a parameter with no row.
- [The Canonical Basis Above $M_C$](the-canonical-basis-above-m-c-one-rescaling-three-costs-and-the-numbers-that-are-not-invariants.html). Why the second kinetic term is admissible and still removed.
