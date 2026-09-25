
# __List of Local Rings and Valuations__

## Introduction

This article lists the local rings, the valuation rings and the completions of the corpus, with the maximal ideal and the value group of each. Every entry points to the article that introduces the object.

The list separates the local rings that are not valuation rings, such as the dual numbers and the truncated polynomial rings, from the valuation rings, which are exactly the local domains whose ideals are totally ordered; among the valuation rings it separates the discrete ones, with value group $\mathbb{Z}$, from the non-discrete and higher-rank ones; and it records the completions, which preserve the value group and the residue field in the non-Archimedean case.

The article introduces nothing and proves nothing. It records examples and non-examples side by side.

## Local Rings

| Local ring | Maximal ideal | Residue field | Valuation ring? | Introduced in |
|---|---|---|---|---|
| $\mathbb{D}' = \mathbb{R}[\varepsilon]/(\varepsilon^2)$ | $(\varepsilon)$ | $\mathbb{R}$ | no | *Dual-Numbers Algebra* |
| $\mathbb{Z}/4\mathbb{Z}$ | $(2)$ | $\mathbb{F}_2$ | no | *Reduced Rings and the Nilradical* |
| $k[x]/(x^n)$ | $(x)$ | $k$ | no for $n \geq 2$ | *Noetherian and Artinian Rings* |
| $\mathbb{F}_2[C_2]$ | the augmentation ideal | $\mathbb{F}_2$ | no | *Examples of Rings and Fields* |
| $\mathbb{Z}_{(p)}$ | $(p)$ | $\mathbb{F}_p$ | yes, discrete | *Localization and the Fraction Field* |
| $k[t]_{(t)}$ | $(t)$ | $k$ | yes, discrete | *Absolute Values, Valuations and Completions* |
| $k[[x]]$ | $(x)$ | $k$ | yes, discrete | *Examples of Rings and Fields* |
| $\mathbb{Z}_p$ | $(p)$ | $\mathbb{F}_p$ | yes, discrete | *Absolute Values, Valuations and Completions* |
| $\mathbb{F}_p$, $\mathbb{Q}_p$, $\mathbb{R}$, $\mathbb{C}$ | $(0)$ | the field itself | yes, the trivial valuation | *Finite Fields*, *The Real Numbers*, *The Complex Numbers*, *Absolute Values, Valuations and Completions* |
| $\mathcal{O}_v$, a general valuation ring | $\mathfrak{m}_v = \{x : v(x) > 0\}$ | $k(v) = \mathcal{O}_v/\mathfrak{m}_v$ | yes, by definition | *Valuation Theory and Henselian Rings* |
| $\overline{\mathbb{Z}_p}$ | the extension of $p\mathbb{Z}_p$ | $\overline{\mathbb{F}_p}$ | yes, value group $\mathbb{Q}$ | *Absolute Values, Valuations and Completions* |
| $R^h$, the henselization of a local ring | the maximal ideal of $R$ extended | the residue field of $R$ | when $R$ is a valuation ring | *Valuation Theory and Henselian Rings* |

A field is local with maximal ideal $(0)$, so the fields appear in the list for completeness and are not counted as proper local rings. Among the local rings of this list those that are not valuation rings are exactly those that are not integral domains: the dual numbers, $\mathbb{Z}/4\mathbb{Z}$, the truncated polynomial rings and the local group ring all have zero divisors, and a valuation ring is an integral domain. The matrix ring $M_2(\mathbb{R})$ is the standard local-ring failure on the non-commutative side and is recorded in the warnings. The rings that are expected here and are not local are $\mathbb{Z}$, $\mathbb{Z}[x]$ and $k[x]$, each with infinitely many maximal ideals.

## Discrete Valuation Rings

A discrete valuation ring is a valuation ring whose value group is $\mathbb{Z}$; equivalently, as recorded in *Dedekind Domains and Ideal Class Groups*, it is a local principal ideal domain that is not a field, and it is exactly the valuation ring of a discrete valuation of its fraction field.

| Discrete valuation ring | Maximal ideal | Value group | Residue field | Introduced in |
|---|---|---|---|---|
| $\mathbb{Z}_{(p)}$ | $p\mathbb{Z}_{(p)}$ | $\mathbb{Z}$ | $\mathbb{F}_p$ | *Localization and the Fraction Field* |
| $k[t]_{(t)}$ | $(t)$ | $\mathbb{Z}$ | $k$ | *Absolute Values, Valuations and Completions* |
| $k[[x]]$ | $(x)$ | $\mathbb{Z}$ | $k$ | *Examples of Rings and Fields* |
| $\mathbb{Z}_p$ | $p\mathbb{Z}_p$ | $\mathbb{Z}$ | $\mathbb{F}_p$ | *Absolute Values, Valuations and Completions* |
| $\mathcal{O}_{K,\mathfrak{p}}$, the localisation of $\mathcal{O}_K$ at a prime | $\mathfrak{p}$ | $\mathbb{Z}$ | $\mathcal{O}_K/\mathfrak{p}$ | *Dedekind Domains and Ideal Class Groups* |

The valuation is the exponent of the maximal ideal: $v_p(a/b)$ is the exponent of $p$ in $a$ minus the exponent in $b$, and the same rule with an irreducible element replaces $p$ in the other rows. Every DVR has the ideal chain $\mathcal{O} \supsetneq \mathfrak{m} \supsetneq \mathfrak{m}^2 \supsetneq \cdots$, and the localisation of a Dedekind domain at each of its nonzero prime ideals is a discrete valuation ring, as recorded in *Dedekind Domains and Ideal Class Groups*.

## Non-Discrete and Higher-Rank Valuations

| Valuation | Field | Value group | Rank | Valuation ring | Introduced in |
|---|---|---|---|---|---|
| the $p$-adic valuation $v_p$ | $\mathbb{Q}$ | $\mathbb{Z}$ | $1$ | $\mathbb{Z}_{(p)}$ | *Absolute Values, Valuations and Completions* |
| the $t$-adic valuation | $k(t)$ | $\mathbb{Z}$ | $1$ | $k[t]_{(t)}$ | *Absolute Values, Valuations and Completions* |
| a non-discrete order valuation at a transcendental $\alpha$ | $k(x)$ | a dense subgroup of $\mathbb{R}$ | $1$ | not Noetherian | *Valuation Theory and Henselian Rings* |
| the lexicographic rank-two valuation | $k(x,y)$ | $\mathbb{Z} \oplus \mathbb{Z}$, lexicographic | $2$ | dominates $k[x,y]_{(x,y)}$ | *Valuation Theory and Henselian Rings* |
| the extended valuation on the algebraic closure | $\overline{\mathbb{Q}_p}$ | $\mathbb{Q}$ | $1$ | $\overline{\mathbb{Z}_p}$ | *Absolute Values, Valuations and Completions* |
| the trivial valuation | any field | $0$ | $0$ | the field | *Valuation Theory and Henselian Rings* |

The rank of a valuation is the order rank of its value group, and the prime ideals of the valuation ring correspond to the convex subgroups of the value group; consequently the Krull dimension of the valuation ring equals the rank of the valuation. The rank-two example is the one the corpus records in detail: its value group is $\mathbb{Z} \oplus \mathbb{Z}$ with the lexicographic order, its convex subgroups are $0$, $\{0\} \oplus \mathbb{Z}$ and the whole group, and its valuation ring has dimension $2$. The non-discrete rank-one example is the reason a rank-one valuation ring need not be Noetherian; the Noetherian case is exactly the discrete one.

## Completions

| Field | Valuation or absolute value | Completion | Value group | Residue field | Introduced in |
|---|---|---|---|---|---|
| $\mathbb{Q}$ | $\lvert \cdot \rvert_p$ | $\mathbb{Q}_p$ | $\mathbb{Z}$ | $\mathbb{F}_p$ | *Absolute Values, Valuations and Completions* |
| $\mathbb{Q}$ | $\lvert \cdot \rvert_\infty$ | $\mathbb{R}$ | — | — | *The Real Numbers* |
| $k(t)$ | the $t$-adic valuation | $k((t))$ | $\mathbb{Z}$ | $k$ | *Absolute Values, Valuations and Completions* |
| $\overline{\mathbb{Q}_p}$ | the extended $p$-adic valuation | $\mathbb{C}_p$ | $\mathbb{Q}$ | $\overline{\mathbb{F}_p}$ | *Absolute Values, Valuations and Completions* |
| $\mathbb{Z}_{(p)}$ | the $p$-adic filtration | $\mathbb{Z}_p$ | $\mathbb{Z}$ | $\mathbb{F}_p$ | *Absolute Values, Valuations and Completions* |

In the non-Archimedean case the completion preserves both invariants: the value group of $\widehat{F}$ equals that of $F$, and the residue field is unchanged, so the completion of a DVR is again a DVR with the same value group and residue field. The completion of $\mathbb{Q}$ at the Archimedean place is $\mathbb{R}$, where the value set can grow and the value group is no longer the right invariant. The henselization sits inside the completion, $R^h \subseteq \widehat{R}$, with equality exactly when the valuation ring is already Henselian, as recorded in *Valuation Theory and Henselian Rings*.

## The Value Group as an Invariant

| Value group | The rings and fields that carry it | Introduced in |
|---|---|---|
| $0$ | every field, with the trivial valuation | *Valuation Theory and Henselian Rings* |
| $\mathbb{Z}$ | every discrete valuation ring: $\mathbb{Z}_{(p)}$, $k[t]_{(t)}$, $k[[x]]$, $\mathbb{Z}_p$, $\mathcal{O}_{K,\mathfrak{p}}$, and the fields $\mathbb{Q}_p$, $k((t))$ | *Absolute Values, Valuations and Completions*, *Examples of Rings and Fields*, *Dedekind Domains and Ideal Class Groups* |
| a dense subgroup of $\mathbb{R}$ | the non-discrete rank-one valuation ring of $k(x)$ | *Valuation Theory and Henselian Rings* |
| $\mathbb{Q}$ | the valuation ring of $\overline{\mathbb{Q}_p}$ and of $\mathbb{C}_p$ | *Absolute Values, Valuations and Completions* |
| $\mathbb{Z} \oplus \mathbb{Z}$, lexicographic | the rank-two valuation ring of $k(x,y)$ | *Valuation Theory and Henselian Rings* |
| $\Gamma$, arbitrary | the general valuation ring $\mathcal{O}_v$ | *Valuation Theory and Henselian Rings* |

## Warnings

| Object | Why it is not a local ring of this list | Introduced in |
|---|---|---|
| $\mathbb{Z}$ | not local: every prime is a maximal ideal | *The Integers* |
| $\mathbb{Z}[x]$, $k[x]$ | not local, and not valuation rings | *Polynomial Rings and Rational Functions* |
| $M_2(\mathbb{R})$ | not commutative, so outside the commutative local theory | *Matrix Algebras* |
| $\mathbb{H}$ | a division ring; its only maximal ideal is $(0)$, but the local theory here is commutative | *Quaternion Algebra* |
| $\mathbb{O}$ | not a ring | *Octonion Algebra* |
| $\mathbb{Z}/6\mathbb{Z}$ | not local: it has the two maximal ideals $(2)$ and $(3)$ | *Modular Arithmetic and the Ring of Residues* |
| a Boolean ring | not local unless it is $\mathbb{F}_2$: its prime ideals are maximal, and there is one for every ultrafilter | *Von Neumann Regular Rings* |

## Summary

This article has listed the local rings, the valuation rings and the completions of the corpus with their maximal ideals and their value groups. The local rings that are not valuation rings are the dual numbers, the truncated polynomial rings and the local group ring; the discrete valuation rings are the localisations of $\mathbb{Z}$ and $k[t]$, the power series ring $k[[x]]$, the $p$-adic integers $\mathbb{Z}_p$ and the localisations of a Dedekind domain; the non-discrete and rank-two examples are the dense-rank-one valuation on $k(x)$ and the lexicographic valuation on $k(x,y)$ with value group $\mathbb{Z} \oplus \mathbb{Z}$; and the completions are $\mathbb{Q}_p$, $\mathbb{R}$, $k((t))$, $\mathbb{C}_p$ and $\mathbb{Z}_p$, with the value group and the residue field preserved in the non-Archimedean case.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following.

| Symbol | Meaning |
|---|---|
| $\mathcal{O}$, $\mathcal{O}_v$ | Valuation ring of the valuation $v$ |
| $\mathfrak{m}$, $\mathfrak{m}_v$ | Maximal ideal of a local ring or valuation ring |
| $k(v)$ | Residue field $\mathcal{O}_v/\mathfrak{m}_v$ |
| $\Gamma$, $\Gamma_v$ | Value group, written additively |
| $v_p$ | The $p$-adic valuation |
| $\mathbb{Z}_{(p)}$, $\mathbb{Z}_p$ | Localisation at $p$, $p$-adic integers |
| $\mathbb{Q}_p$, $\mathbb{C}_p$ | $p$-adic numbers, completed algebraic closure |
| $k((t))$, $k[[x]]$ | Laurent series field, power series ring |
| $\mathcal{O}_{K,\mathfrak{p}}$, $\mathcal{O}_K$ | Localisation of the ring of integers, ring of integers |
| $\overline{\mathbb{Q}_p}$, $\overline{\mathbb{Z}_p}$, $\overline{\mathbb{F}_p}$ | Algebraic closures and their valuation ring |
| $\widehat{F}$, $R^h$ | Completion, henselization |
| $\mathbb{D}'$ | The dual numbers, a local ring that is not a valuation ring |

## Further Reading

- Jean-Pierre Serre, *Local Fields* (Springer, 1979), for discrete valuation rings, their completions and the ramification invariants.
- Oscar Zariski and Pierre Samuel, *Commutative Algebra*, Volume II (Van Nostrand, 1960), for valuation rings of arbitrary rank, their value groups and their ideals.
- Neal Koblitz, *p-adic Numbers, p-adic Analysis, and Zeta-Functions* (Springer, 2nd ed. 1984), for the completions $\mathbb{Q}_p$ and $\mathbb{Z}_p$ and their residue fields.
